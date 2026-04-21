"""Tests for risk_register.py.

Covers:
- RAG status calculation across all threshold boundaries
- Inherent and residual score computation (likelihood × impact)
- OSFI reference inference by category
- JSON schema validation (valid entries, and all rejection cases)
- JSON export produces parseable output with computed fields
- Markdown export contains all required sections and risk IDs
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from scripts.risk_register import (
    _enrich_entry,
    calculate_rag,
    process_register,
    to_json,
    to_markdown,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_entry(**overrides) -> dict:
    """Return a minimal valid risk entry, with optional field overrides."""
    base = {
        "id": "RISK-001",
        "title": "Unpatched Systems",
        "description": "Critical systems running end-of-life software.",
        "category": "technology",
        "inherent_risk": {"likelihood": 4, "impact": 5},
        "controls": ["Automated patch management", "Monthly vulnerability scanning"],
        "residual_risk": {"likelihood": 2, "impact": 3},
        "owner": "CISO",
        "review_date": "2026-09-30",
    }
    base.update(overrides)
    return base


def _make_register(*entries) -> dict:
    """Wrap one or more entries in a valid register envelope."""
    return {
        "register_metadata": {
            "title": "Test Risk Register",
            "version": "1.0",
            "created_by": "Test Suite",
            "review_cycle": "quarterly",
        },
        "risks": list(entries),
    }


# ---------------------------------------------------------------------------
# calculate_rag — boundary tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "score,expected",
    [
        (1, "Green"),
        (7, "Green"),
        (8, "Amber"),
        (14, "Amber"),
        (15, "Red"),
        (25, "Red"),
    ],
)
def test_calculate_rag_boundaries(score: int, expected: str) -> None:
    assert calculate_rag(score) == expected


# ---------------------------------------------------------------------------
# _enrich_entry — score computation and derived fields
# ---------------------------------------------------------------------------


def test_enrich_entry_inherent_score() -> None:
    result = _enrich_entry(_make_entry(inherent_risk={"likelihood": 4, "impact": 5}))
    assert result["inherent_risk"]["score"] == 20  # 4 × 5


def test_enrich_entry_residual_score_and_rag_green() -> None:
    result = _enrich_entry(_make_entry(residual_risk={"likelihood": 2, "impact": 3}))
    assert result["residual_risk"]["score"] == 6  # 2 × 3
    assert result["rag_status"] == "Green"


def test_enrich_entry_residual_rag_amber() -> None:
    result = _enrich_entry(_make_entry(residual_risk={"likelihood": 2, "impact": 5}))
    assert result["residual_risk"]["score"] == 10
    assert result["rag_status"] == "Amber"


def test_enrich_entry_residual_rag_red() -> None:
    result = _enrich_entry(_make_entry(residual_risk={"likelihood": 5, "impact": 4}))
    assert result["residual_risk"]["score"] == 20
    assert result["rag_status"] == "Red"


def test_enrich_entry_osfi_reference_inferred_technology() -> None:
    result = _enrich_entry(_make_entry(category="technology"))
    assert "B-13" in result["osfi_reference"]


def test_enrich_entry_osfi_reference_inferred_third_party() -> None:
    result = _enrich_entry(_make_entry(category="third-party"))
    assert "B-10" in result["osfi_reference"]


def test_enrich_entry_osfi_reference_inferred_operational() -> None:
    result = _enrich_entry(_make_entry(category="operational"))
    assert "E-21" in result["osfi_reference"]


def test_enrich_entry_osfi_reference_preserved_when_explicit() -> None:
    result = _enrich_entry(_make_entry(osfi_reference="Custom Guideline §7"))
    assert result["osfi_reference"] == "Custom Guideline §7"


def test_enrich_entry_does_not_mutate_input() -> None:
    original = _make_entry()
    _enrich_entry(original)
    assert "score" not in original["inherent_risk"]
    assert "rag_status" not in original


# ---------------------------------------------------------------------------
# process_register — validation happy path
# ---------------------------------------------------------------------------


def test_process_register_valid_single_entry() -> None:
    register = _make_register(_make_entry())
    result = process_register(register)
    assert len(result["risks"]) == 1
    risk = result["risks"][0]
    assert risk["rag_status"] in {"Red", "Amber", "Green"}
    assert "score" in risk["inherent_risk"]
    assert "score" in risk["residual_risk"]


def test_process_register_valid_multiple_entries() -> None:
    entries = [
        _make_entry(id="RISK-001", title="Risk One"),
        _make_entry(id="RISK-002", title="Risk Two", category="cyber"),
        _make_entry(
            id="RISK-003",
            title="Risk Three",
            category="data",
            residual_risk={"likelihood": 5, "impact": 5},
        ),  # Red
    ]
    result = process_register(_make_register(*entries))
    assert len(result["risks"]) == 3
    assert result["risks"][2]["rag_status"] == "Red"


def test_process_register_preserves_metadata() -> None:
    register = _make_register(_make_entry())
    result = process_register(register)
    assert result["register_metadata"]["title"] == "Test Risk Register"


# ---------------------------------------------------------------------------
# process_register — schema rejection cases
# ---------------------------------------------------------------------------


def test_process_register_rejects_invalid_category() -> None:
    with pytest.raises(jsonschema.ValidationError):
        process_register(_make_register(_make_entry(category="financial")))


def test_process_register_rejects_likelihood_out_of_range() -> None:
    with pytest.raises(jsonschema.ValidationError):
        process_register(
            _make_register(_make_entry(inherent_risk={"likelihood": 6, "impact": 3}))
        )


def test_process_register_rejects_impact_zero() -> None:
    with pytest.raises(jsonschema.ValidationError):
        process_register(
            _make_register(_make_entry(residual_risk={"likelihood": 1, "impact": 0}))
        )


def test_process_register_rejects_bad_id_pattern() -> None:
    with pytest.raises(jsonschema.ValidationError):
        process_register(_make_register(_make_entry(id="R-001")))


def test_process_register_rejects_invalid_review_cycle() -> None:
    register = _make_register(_make_entry())
    register["register_metadata"]["review_cycle"] = "monthly"
    with pytest.raises(jsonschema.ValidationError):
        process_register(register)


def test_process_register_rejects_missing_owner() -> None:
    entry = _make_entry()
    del entry["owner"]
    with pytest.raises(jsonschema.ValidationError):
        process_register(_make_register(entry))


def test_process_register_rejects_empty_controls() -> None:
    with pytest.raises(jsonschema.ValidationError):
        process_register(_make_register(_make_entry(controls=[])))


def test_process_register_rejects_empty_risks_array() -> None:
    register = _make_register()  # no entries
    register["risks"] = []
    with pytest.raises(jsonschema.ValidationError):
        process_register(register)


# ---------------------------------------------------------------------------
# to_json export
# ---------------------------------------------------------------------------


def test_to_json_creates_file(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "out.json"
    to_json(enriched, out)
    assert out.exists()


def test_to_json_output_is_valid_json(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "out.json"
    to_json(enriched, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "risks" in data
    assert "register_metadata" in data


def test_to_json_output_contains_computed_fields(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "out.json"
    to_json(enriched, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    risk = data["risks"][0]
    assert "score" in risk["inherent_risk"]
    assert "score" in risk["residual_risk"]
    assert risk["rag_status"] in {"Red", "Amber", "Green"}


def test_to_json_creates_parent_directory(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    nested = tmp_path / "deep" / "nested" / "out.json"
    to_json(enriched, nested)
    assert nested.exists()


# ---------------------------------------------------------------------------
# to_markdown export
# ---------------------------------------------------------------------------


def test_to_markdown_creates_file(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "report.md"
    to_markdown(enriched, out)
    assert out.exists()


def test_to_markdown_contains_risk_id(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "report.md"
    to_markdown(enriched, out)
    content = out.read_text(encoding="utf-8")
    assert "RISK-001" in content


def test_to_markdown_contains_required_sections(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "report.md"
    to_markdown(enriched, out)
    content = out.read_text(encoding="utf-8")
    assert "Risk Summary" in content
    assert "Risk Detail" in content
    assert "Inherent Risk" in content
    assert "Residual Risk" in content
    assert "Controls in Place" in content


def test_to_markdown_contains_rag_status(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    out = tmp_path / "report.md"
    to_markdown(enriched, out)
    content = out.read_text(encoding="utf-8")
    assert any(status in content for status in ("Red", "Amber", "Green"))


def test_to_markdown_all_risks_present(tmp_path: Path) -> None:
    entries = [
        _make_entry(id="RISK-001", title="First Risk"),
        _make_entry(id="RISK-002", title="Second Risk", category="cyber"),
    ]
    enriched = process_register(_make_register(*entries))
    out = tmp_path / "report.md"
    to_markdown(enriched, out)
    content = out.read_text(encoding="utf-8")
    assert "RISK-001" in content
    assert "RISK-002" in content
    assert "First Risk" in content
    assert "Second Risk" in content
