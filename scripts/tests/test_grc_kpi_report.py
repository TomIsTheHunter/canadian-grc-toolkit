"""Tests for grc_kpi_report.py."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from scripts.grc_kpi_report import analyze_kpis, render_markdown, write_markdown_report
from scripts.risk_register import process_register


def _make_entry(**overrides) -> dict:
    base = {
        "id": "RISK-001",
        "title": "Legacy Core Platform",
        "description": "Legacy platform requires compensating controls.",
        "category": "technology",
        "inherent_risk": {"likelihood": 4, "impact": 5},
        "controls": ["Segmentation", "Compensating monitoring"],
        "residual_risk": {"likelihood": 2, "impact": 5},
        "owner": "CISO",
        "review_date": "2026-06-30",
    }
    base.update(overrides)
    return base


def _make_register(*entries) -> dict:
    return {
        "register_metadata": {
            "title": "GRC KPI Test Register",
            "version": "1.0",
            "created_by": "Test Suite",
            "review_cycle": "quarterly",
        },
        "risks": list(entries),
    }


def test_analyze_kpis_calculates_control_effectiveness() -> None:
    enriched = process_register(
        _make_register(
            _make_entry(
                id="RISK-001",
                inherent_risk={"likelihood": 4, "impact": 5},
                residual_risk={"likelihood": 2, "impact": 5},
            ),
            _make_entry(
                id="RISK-002",
                category="cyber",
                inherent_risk={"likelihood": 3, "impact": 5},
                residual_risk={"likelihood": 1, "impact": 5},
                review_date="2026-09-30",
            ),
        )
    )

    kpis = analyze_kpis(enriched, as_of=date(2026, 10, 21))

    assert kpis["summary"]["control_effectiveness"] == 57.1
    assert kpis["summary"]["open_findings"] == 2
    assert kpis["summary"]["high_or_critical_findings"] == 1


def test_analyze_kpis_groups_findings_by_severity_and_age() -> None:
    enriched = process_register(
        _make_register(
            _make_entry(
                id="RISK-001",
                residual_risk={"likelihood": 2, "impact": 5},
                review_date="2026-10-30",
            ),
            _make_entry(
                id="RISK-002",
                category="data",
                residual_risk={"likelihood": 1, "impact": 4},
                review_date="2026-06-30",
            ),
        )
    )

    kpis = analyze_kpis(enriched, as_of=date(2026, 10, 21))

    assert kpis["severity_age"]["High"]["61-90 days"] == 1
    assert kpis["severity_age"]["Low"][">90 days"] == 1


def test_analyze_kpis_flags_overdue_items_with_owner_action() -> None:
    enriched = process_register(
        _make_register(
            _make_entry(id="RISK-001", review_date="2026-06-30"),
            _make_entry(
                id="RISK-002", review_date="2026-12-31", category="third-party"
            ),
        )
    )

    kpis = analyze_kpis(enriched, as_of=date(2026, 10, 21))

    assert len(kpis["overdue_items"]) == 1
    assert kpis["overdue_items"][0]["id"] == "RISK-001"
    assert kpis["overdue_items"][0]["flag"] == "Owner action required"


def test_render_markdown_contains_required_sections() -> None:
    enriched = process_register(_make_register(_make_entry()))
    content = render_markdown(analyze_kpis(enriched, as_of=date(2026, 10, 21)))

    assert "Executive Summary" in content
    assert "Control Effectiveness" in content
    assert "Open Findings By Severity And Age" in content
    assert "Overdue Items" in content
    assert "Trend Vs Prior Period" in content
    assert "prior-period trend values are mock baselines" in content


def test_write_markdown_report_creates_file(tmp_path: Path) -> None:
    enriched = process_register(_make_register(_make_entry()))
    output_path = tmp_path / "grc_kpi_dashboard.md"

    write_markdown_report(
        analyze_kpis(enriched, as_of=date(2026, 10, 21)),
        output_path,
    )

    assert output_path.exists()
    assert "Owner action required" in output_path.read_text(encoding="utf-8")
