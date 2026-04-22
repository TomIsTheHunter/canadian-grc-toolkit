from __future__ import annotations

import json
from pathlib import Path

from scripts.osfi_b10_vendor_risk import assess_vendor, assess_vendor_risk_file


def test_assess_vendor_returns_rag_and_tier() -> None:
    result = assess_vendor(
        {
            "vendor_id": "V-1",
            "vendor_name": "Critical Provider",
            "criticality": "critical",
            "data_sensitivity": "high",
            "concentration_risk": "high",
            "fourth_party_dependency": True,
            "incident_history_count": 2,
            "financial_health": "weak",
            "exit_plan_tested": False,
            "contract_has_osfi_b10_clauses": False,
        }
    )

    assert result["rag_status"] in {"Red", "Amber", "Green"}
    assert result["risk_tier"] in {"low", "medium", "high", "critical"}
    assert isinstance(result["required_actions"], list)


def test_assess_vendor_risk_file_aggregates_summary(tmp_path: Path) -> None:
    input_path = tmp_path / "vendors.json"
    input_path.write_text(
        json.dumps(
            {
                "vendors": [
                    {
                        "vendor_id": "V-1",
                        "vendor_name": "Safe Vendor",
                        "criticality": "low",
                        "data_sensitivity": "low",
                        "concentration_risk": "low",
                        "fourth_party_dependency": False,
                        "incident_history_count": 0,
                        "financial_health": "strong",
                        "exit_plan_tested": True,
                        "contract_has_osfi_b10_clauses": True,
                    },
                    {
                        "vendor_id": "V-2",
                        "vendor_name": "Risky Vendor",
                        "criticality": "critical",
                        "data_sensitivity": "critical",
                        "concentration_risk": "high",
                        "fourth_party_dependency": True,
                        "incident_history_count": 4,
                        "financial_health": "distressed",
                        "exit_plan_tested": False,
                        "contract_has_osfi_b10_clauses": False,
                    },
                ]
            }
        ),
        encoding="utf-8",
    )

    result = assess_vendor_risk_file(input_path)

    assert result["summary"]["vendor_count"] == 2
    assert set(result["summary"]["rag_counts"].keys()) == {"Red", "Amber", "Green"}
    assert len(result["vendors"]) == 2
