#!/usr/bin/env python3
"""OSFI B-10 third-party vendor risk assessment helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


_LEVEL_SCORES = {
    "low": 15,
    "medium": 45,
    "high": 75,
    "critical": 90,
    "strong": 20,
    "stable": 40,
    "weak": 70,
    "distressed": 90,
}


def _normalize_level(value: Any, default: str = "medium") -> str:
    if value is None:
        return default
    text = str(value).strip().lower()
    return text if text else default


def _bool_score(value: Any, true_score: int, false_score: int) -> int:
    return true_score if bool(value) else false_score


def _level_score(level: str, default: int = 45) -> int:
    return _LEVEL_SCORES.get(level, default)


def _rag(score: float) -> str:
    if score >= 70:
        return "Red"
    if score >= 40:
        return "Amber"
    return "Green"


def _tier(score: float) -> str:
    if score >= 85:
        return "critical"
    if score >= 70:
        return "high"
    if score >= 40:
        return "medium"
    return "low"


def _required_actions(vendor: dict[str, Any], score: float) -> list[str]:
    actions: list[str] = []
    if score >= 70:
        actions.append("Escalate to Third-Party Risk Committee")
    if not vendor.get("contract_has_osfi_b10_clauses", False):
        actions.append("Update contract to include mandatory OSFI B-10 clauses")
    if not vendor.get("exit_plan_tested", False):
        actions.append("Test and document third-party exit strategy")
    if int(vendor.get("incident_history_count", 0)) >= 2:
        actions.append("Increase oversight cadence and incident review frequency")
    return actions


def assess_vendor(vendor: dict[str, Any]) -> dict[str, Any]:
    criticality = _normalize_level(vendor.get("criticality"), "medium")
    data_sensitivity = _normalize_level(vendor.get("data_sensitivity"), "medium")
    concentration = _normalize_level(vendor.get("concentration_risk"), "medium")
    financial = _normalize_level(vendor.get("financial_health"), "stable")

    incident_history = int(vendor.get("incident_history_count", 0))
    incident_score = min(incident_history * 12, 90)

    factors = {
        "criticality": _level_score(criticality),
        "data_sensitivity": _level_score(data_sensitivity),
        "concentration_risk": _level_score(concentration),
        "fourth_party_dependency": _bool_score(
            vendor.get("fourth_party_dependency", False), true_score=75, false_score=20
        ),
        "incident_history": incident_score,
        "financial_health": _level_score(financial),
        "exit_plan_tested": _bool_score(
            vendor.get("exit_plan_tested", False), true_score=20, false_score=80
        ),
        "contract_has_osfi_b10_clauses": _bool_score(
            vendor.get("contract_has_osfi_b10_clauses", False),
            true_score=20,
            false_score=85,
        ),
    }

    weights = {
        "criticality": 0.22,
        "data_sensitivity": 0.16,
        "concentration_risk": 0.14,
        "fourth_party_dependency": 0.10,
        "incident_history": 0.10,
        "financial_health": 0.10,
        "exit_plan_tested": 0.08,
        "contract_has_osfi_b10_clauses": 0.10,
    }

    score = round(sum(factors[key] * weights[key] for key in factors), 1)
    return {
        "vendor_id": vendor.get("vendor_id", "unknown"),
        "vendor_name": vendor.get("vendor_name", "Unknown Vendor"),
        "criticality": criticality,
        "risk_score": score,
        "risk_tier": _tier(score),
        "rag_status": _rag(score),
        "factor_scores": factors,
        "required_actions": _required_actions(vendor, score),
    }


def _load_vendor_payload(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("vendors"), list):
        return payload["vendors"]
    raise ValueError(
        "Vendor data must be a JSON list or an object with a 'vendors' list"
    )


def assess_vendor_risk_file(path: Path) -> dict[str, Any]:
    vendors = _load_vendor_payload(path)
    assessed = [assess_vendor(vendor) for vendor in vendors]
    rag = {
        "Red": sum(1 for v in assessed if v["rag_status"] == "Red"),
        "Amber": sum(1 for v in assessed if v["rag_status"] == "Amber"),
        "Green": sum(1 for v in assessed if v["rag_status"] == "Green"),
    }
    high_or_critical = sum(
        1 for v in assessed if v["risk_tier"] in {"high", "critical"}
    )

    return {
        "summary": {
            "vendor_count": len(assessed),
            "rag_counts": rag,
            "high_or_critical_count": high_or_critical,
        },
        "vendors": assessed,
    }
