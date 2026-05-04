"""Tests for incident classification and event loading logic."""

from __future__ import annotations

import json
from pathlib import Path

from scripts.osfi_incident_classifier import (
    classify_osfi,
    classify_pipeda,
    compute_report,
    detect_format,
    load_events,
    normalize_event,
)


def test_detect_format_auto_uses_file_extension() -> None:
    assert detect_format(Path("events.csv"), "auto") == "csv"
    assert detect_format(Path("events.json"), "auto") == "json"


def test_classifiers_flag_expected_regulatory_conditions() -> None:
    event = normalize_event(
        {
            "event_id": "EVT-1001",
            "detected_at": "2026-04-18T08:15:00Z",
            "event_type": "credential_compromise",
            "severity": "high",
            "systems_affected": ["online_banking_api"],
            "service_disruption_minutes": 75,
            "financial_loss_cad": 150000,
            "third_party_involved": False,
            "personal_data_compromised": True,
            "exfiltration_confirmed": True,
            "records_affected": 12000,
            "data_types": ["account_number", "dob"],
            "critical_operation_impacted": True,
            "description": "Credential stuffing against online banking.",
        },
        1,
    )

    osfi = classify_osfi(event)
    pipeda = classify_pipeda(event)

    assert osfi["reportable_to_osfi"] is True
    assert "financial_loss_over_100k_cad" in osfi["reasons"]
    assert pipeda["notify_privacy_commissioner"] is True
    assert "sensitive_personal_information_involved" in pipeda["reasons"]


def test_compute_report_summarizes_events() -> None:
    events = [
        normalize_event(
            {
                "event_id": "EVT-1001",
                "detected_at": "2026-04-18T08:15:00Z",
                "contained_at": "2026-04-18T09:10:00Z",
                "event_type": "credential_compromise",
                "severity": "high",
                "systems_affected": ["online_banking_api", "ciam"],
                "service_disruption_minutes": 45,
                "financial_loss_cad": 25000,
                "third_party_involved": False,
                "personal_data_compromised": True,
                "exfiltration_confirmed": True,
                "records_affected": 12000,
                "data_types": ["email", "account_number", "dob"],
                "critical_operation_impacted": True,
                "description": "Suspicious privileged login.",
            },
            1,
        ),
        normalize_event(
            {
                "event_id": "EVT-1002",
                "detected_at": "2026-04-18T08:50:00Z",
                "contained_at": "2026-04-18T09:30:00Z",
                "event_type": "payment_outage",
                "severity": "high",
                "systems_affected": ["payments_switch"],
                "service_disruption_minutes": 95,
                "financial_loss_cad": 180000,
                "third_party_involved": False,
                "personal_data_compromised": False,
                "exfiltration_confirmed": False,
                "records_affected": 0,
                "data_types": [],
                "critical_operation_impacted": True,
                "description": "Payment authorization unavailable.",
            },
            2,
        ),
    ]

    report = compute_report(
        events, institution="Maple Bank", prepared_by="Cyber Incident Response Team"
    )

    assert (
        report["regulatory_assessment"]["osfi"]["twenty_four_hour_threshold_triggered"]
        is True
    )
    assert report["regulatory_assessment"]["osfi"]["reportable_event_count"] == 2
    assert (
        report["regulatory_assessment"]["pipeda"][
            "privacy_commissioner_notification_required"
        ]
        is True
    )
    assert report["events"][0]["event_id"] == "EVT-1001"


def test_load_events_reads_json_list(tmp_path: Path) -> None:
    payload = [{"event_id": "EVT-1", "detected_at": "2026-04-18T08:15:00Z"}]
    path = tmp_path / "events.json"
    path.write_text(json.dumps(payload), encoding="utf-8")

    assert load_events(path, "json") == payload
