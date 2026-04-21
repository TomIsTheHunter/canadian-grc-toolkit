from __future__ import annotations

import os
from datetime import date
from pathlib import Path

from scripts.grc_kpi_report import analyze_kpis, render_markdown
from scripts.risk_register import process_register, to_json


GOLDEN_DIR = Path(__file__).parent / "golden"


def _register_fixture() -> dict:
    return {
        "register_metadata": {
            "title": "Golden Register",
            "version": "1.0",
            "created_by": "Golden Tests",
            "review_cycle": "quarterly",
            "description": "Deterministic fixture for golden output tests.",
        },
        "risks": [
            {
                "id": "RISK-001",
                "title": "Credential Stuffing",
                "description": "Credential stuffing risk against digital channels.",
                "category": "cyber",
                "inherent_risk": {"likelihood": 3, "impact": 5},
                "controls": ["MFA", "Rate limiting"],
                "residual_risk": {"likelihood": 2, "impact": 4},
                "owner": "VP Cybersecurity",
                "review_date": "2026-06-30",
            },
            {
                "id": "RISK-002",
                "title": "Privileged Access Abuse",
                "description": "Undetected admin misuse across critical systems.",
                "category": "operational",
                "inherent_risk": {"likelihood": 4, "impact": 4},
                "controls": ["PAM", "Session logging"],
                "residual_risk": {"likelihood": 2, "impact": 2},
                "owner": "Director IAM",
                "review_date": "2026-09-30",
            },
        ],
    }


def _assert_golden(file_name: str, content: str) -> None:
    path = GOLDEN_DIR / file_name
    if os.getenv("UPDATE_GOLDENS") == "1":
        path.write_text(content, encoding="utf-8")
    expected = path.read_text(encoding="utf-8")
    assert content == expected


def test_golden_risk_register_json(tmp_path: Path) -> None:
    enriched = process_register(_register_fixture())
    out = tmp_path / "risk.json"
    to_json(enriched, out)
    rendered = out.read_text(encoding="utf-8")
    _assert_golden("expected_risk_register_output.json", rendered)


def test_golden_kpi_markdown() -> None:
    enriched = process_register(_register_fixture())
    kpis = analyze_kpis(enriched, as_of=date(2026, 10, 21))
    rendered = render_markdown(kpis)
    _assert_golden("expected_grc_kpi_dashboard.md", rendered)
