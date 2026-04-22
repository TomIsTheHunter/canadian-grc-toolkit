from __future__ import annotations

import json
from pathlib import Path

import main


def test_orchestrate_aggregates_stage_compliance(monkeypatch, tmp_path: Path) -> None:
    iac_dir = tmp_path / "iac"
    iac_dir.mkdir()
    opa_input = tmp_path / "input.json"
    opa_input.write_text("{}", encoding="utf-8")
    vendor_data = tmp_path / "vendor.json"
    vendor_data.write_text('{"vendors": []}', encoding="utf-8")
    risk = tmp_path / "risk.json"
    risk.write_text("{}", encoding="utf-8")
    policy_dir = tmp_path / "policies"
    policy_dir.mkdir()

    monkeypatch.setattr(
        main,
        "run_preflight_stage",
        lambda: {
            "stage": "preflight",
            "ok": True,
            "compliant": True,
            "checks": [],
        },
    )
    monkeypatch.setattr(
        main,
        "run_checkov_stage",
        lambda _iac: {
            "stage": "checkov_iac_scan",
            "ok": True,
            "compliant": True,
            "summary": {"failed": 0},
        },
    )
    monkeypatch.setattr(
        main,
        "run_opa_stage",
        lambda policy_dir, config_input: {
            "stage": "opa_policy_evaluation",
            "ok": True,
            "compliant": True,
            "decisions": [],
        },
    )
    monkeypatch.setattr(
        main,
        "run_vendor_stage",
        lambda _vendor_data: {
            "stage": "osfi_b10_vendor_risk_assessment",
            "ok": True,
            "compliant": True,
            "assessment": {"summary": {"vendor_count": 0, "high_or_critical_count": 0}},
        },
    )
    monkeypatch.setattr(
        main,
        "run_risk_register_stage",
        lambda _risk: {
            "stage": "risk_register_scoring",
            "ok": True,
            "compliant": True,
            "summary": {
                "risk_count": 0,
                "rag_counts": {"Red": 0, "Amber": 0, "Green": 0},
            },
        },
    )

    result = main.orchestrate(
        iac_dir=iac_dir,
        opa_input=opa_input,
        vendor_data=vendor_data,
        risk_register=risk,
        policy_dir=policy_dir,
    )

    assert result["overall"]["ok"] is True
    assert result["overall"]["compliant"] is True
    assert len(result["stages"]) == 5


def test_orchestrate_fails_fast_on_preflight(monkeypatch, tmp_path: Path) -> None:
    iac_dir = tmp_path / "iac"
    iac_dir.mkdir()
    opa_input = tmp_path / "input.json"
    opa_input.write_text("{}", encoding="utf-8")
    vendor_data = tmp_path / "vendor.json"
    vendor_data.write_text('{"vendors": []}', encoding="utf-8")
    risk = tmp_path / "risk.json"
    risk.write_text("{}", encoding="utf-8")
    policy_dir = tmp_path / "policies"
    policy_dir.mkdir()

    monkeypatch.setattr(
        main,
        "run_preflight_stage",
        lambda: {
            "stage": "preflight",
            "ok": False,
            "compliant": False,
            "checks": [{"tool": "checkov", "available": False}],
            "error": "Missing required tool(s): checkov",
        },
    )

    result = main.orchestrate(
        iac_dir=iac_dir,
        opa_input=opa_input,
        vendor_data=vendor_data,
        risk_register=risk,
        policy_dir=policy_dir,
    )

    assert result["overall"]["ok"] is False
    assert result["overall"]["compliant"] is False
    assert len(result["stages"]) == 1
    assert result["stages"][0]["stage"] == "preflight"


def test_write_report_outputs_json_and_markdown(tmp_path: Path) -> None:
    report = {
        "generated_at_utc": "2026-04-21T00:00:00+00:00",
        "overall": {"ok": True, "compliant": False},
        "stages": [
            {
                "stage": "checkov_iac_scan",
                "ok": True,
                "compliant": False,
                "summary": {"passed": 1, "failed": 2, "skipped": 0},
            }
        ],
    }
    out_json = tmp_path / "report.json"
    out_md = tmp_path / "report.md"

    main._write_report(report, out_json, out_md)

    parsed = json.loads(out_json.read_text(encoding="utf-8"))
    assert parsed["overall"]["compliant"] is False
    assert "Consolidated Compliance Report" in out_md.read_text(encoding="utf-8")
