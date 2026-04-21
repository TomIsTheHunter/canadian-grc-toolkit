from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


SENSITIVE_DATA_TYPES = {
    "sin",
    "social_insurance_number",
    "account_number",
    "card_number",
    "credit_card",
    "credentials",
    "password",
    "dob",
    "date_of_birth",
    "health",
    "biometric",
}

OSFI_REPORTABLE_EVENT_TYPES = {
    "ransomware",
    "data_breach",
    "credential_compromise",
    "ddos",
    "payment_outage",
    "core_banking_outage",
    "fraud_campaign",
    "third_party_breach",
    "unauthorized_access",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Classify mock security logs for OSFI and PIPEDA obligations and "
            "generate a structured notification draft."
        )
    )
    parser.add_argument(
        "--input", required=True, help="Path to input CSV or JSON log file."
    )
    parser.add_argument(
        "--format",
        choices=["auto", "csv", "json"],
        default="auto",
        help="Input format. Defaults to auto-detect from file extension.",
    )
    parser.add_argument(
        "--output",
        default="notification_draft.json",
        help="Output path for structured notification draft JSON.",
    )
    parser.add_argument(
        "--institution",
        default="Example Bank of Canada",
        help="Institution name to pre-populate in notification draft.",
    )
    parser.add_argument(
        "--prepared-by",
        default="SOC Incident Commander",
        help="Name or team preparing the notification draft.",
    )
    return parser.parse_args()


def parse_datetime(value: str) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def parse_float(value: Any) -> float:
    if value in (None, ""):
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def parse_int(value: Any) -> int:
    if value in (None, ""):
        return 0
    try:
        return int(float(value))
    except (TypeError, ValueError):
        return 0


def parse_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip().lower() for item in value if str(item).strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [part.strip().lower() for part in value.split(";") if part.strip()]
    return [str(value).strip().lower()]


def detect_format(path: Path, requested: str) -> str:
    if requested != "auto":
        return requested
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".json":
        return "json"
    raise ValueError(
        "Unable to auto-detect input format. Use --format csv or --format json."
    )


def load_events(path: Path, file_format: str) -> list[dict[str, Any]]:
    if file_format == "csv":
        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)

    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("events"), list):
        return payload["events"]

    raise ValueError(
        "JSON input must be either a list of events or an object with an 'events' array."
    )


def normalize_event(raw_event: dict[str, Any], index: int) -> dict[str, Any]:
    event_id = str(raw_event.get("event_id") or f"EVT-{index:04d}")
    detected_at = parse_datetime(str(raw_event.get("detected_at") or ""))

    return {
        "event_id": event_id,
        "detected_at": detected_at,
        "contained_at": (
            parse_datetime(str(raw_event.get("contained_at") or ""))
            if raw_event.get("contained_at")
            else None
        ),
        "event_type": str(raw_event.get("event_type") or "unknown").strip().lower(),
        "severity": str(raw_event.get("severity") or "medium").strip().lower(),
        "systems_affected": parse_list(raw_event.get("systems_affected")),
        "service_disruption_minutes": parse_int(
            raw_event.get("service_disruption_minutes")
        ),
        "financial_loss_cad": parse_float(raw_event.get("financial_loss_cad")),
        "third_party_involved": parse_bool(raw_event.get("third_party_involved")),
        "personal_data_compromised": parse_bool(
            raw_event.get("personal_data_compromised")
        ),
        "exfiltration_confirmed": parse_bool(raw_event.get("exfiltration_confirmed")),
        "records_affected": parse_int(raw_event.get("records_affected")),
        "data_types": parse_list(raw_event.get("data_types")),
        "critical_operation_impacted": parse_bool(
            raw_event.get("critical_operation_impacted")
        ),
        "description": str(raw_event.get("description") or "").strip(),
    }


def classify_osfi(event: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []

    if event["event_type"] in OSFI_REPORTABLE_EVENT_TYPES:
        reasons.append("event_type_matches_osfi_material_incident_patterns")

    if event["critical_operation_impacted"]:
        reasons.append("critical_operations_impacted")

    if event["service_disruption_minutes"] >= 60:
        reasons.append("service_disruption_over_60_minutes")

    if event["financial_loss_cad"] >= 100000:
        reasons.append("financial_loss_over_100k_cad")

    if event["third_party_involved"] and event["severity"] in {"high", "critical"}:
        reasons.append("high_severity_third_party_incident")

    if event["exfiltration_confirmed"] and event["personal_data_compromised"]:
        reasons.append("confirmed_data_exfiltration")

    reportable = len(reasons) > 0
    return {
        "reportable_to_osfi": reportable,
        "reasons": reasons,
    }


def classify_pipeda(event: dict[str, Any]) -> dict[str, Any]:
    reasons: list[str] = []

    if not event["personal_data_compromised"]:
        return {
            "notify_privacy_commissioner": False,
            "rrsoh_assessed": False,
            "reasons": ["no_personal_information_compromised"],
        }

    sensitive_hit = any(
        data_type in SENSITIVE_DATA_TYPES for data_type in event["data_types"]
    )
    if sensitive_hit:
        reasons.append("sensitive_personal_information_involved")

    if event["exfiltration_confirmed"]:
        reasons.append("confirmed_or_likely_unauthorized_access")

    if event["records_affected"] >= 500:
        reasons.append("large_volume_of_records_affected")

    if event["event_type"] in {
        "credential_compromise",
        "fraud_campaign",
        "unauthorized_access",
    }:
        reasons.append("meaningful_risk_of_identity_or_account_fraud")

    rrsoh_assessed = True
    notify_opc = len(reasons) >= 2 or (
        sensitive_hit and event["exfiltration_confirmed"]
    )

    return {
        "notify_privacy_commissioner": notify_opc,
        "rrsoh_assessed": rrsoh_assessed,
        "reasons": reasons if reasons else ["no_rrsoh_indicators_met"],
    }


def severity_rank(level: str) -> int:
    table = {"low": 1, "medium": 2, "high": 3, "critical": 4}
    return table.get(level, 2)


def compute_report(
    events: list[dict[str, Any]], institution: str, prepared_by: str
) -> dict[str, Any]:
    enriched_events: list[dict[str, Any]] = []

    for event in events:
        osfi = classify_osfi(event)
        pipeda = classify_pipeda(event)
        enriched_events.append(
            {
                "event_id": event["event_id"],
                "detected_at": event["detected_at"].isoformat(),
                "event_type": event["event_type"],
                "severity": event["severity"],
                "systems_affected": event["systems_affected"],
                "summary": event["description"],
                "osfi": osfi,
                "pipeda": pipeda,
            }
        )

    reportable_events = [
        event
        for event, enriched in zip(events, enriched_events)
        if enriched["osfi"]["reportable_to_osfi"]
    ]
    pipeda_events = [
        enriched
        for enriched in enriched_events
        if enriched["pipeda"]["notify_privacy_commissioner"]
    ]

    now = datetime.now(timezone.utc)
    if reportable_events:
        first_trigger = min(event["detected_at"] for event in reportable_events)
        deadline = first_trigger + timedelta(hours=24)
        overdue = now > deadline
    else:
        first_trigger = None
        deadline = None
        overdue = False

    max_severity = "low"
    if events:
        max_severity = max(events, key=lambda event: severity_rank(event["severity"]))[
            "severity"
        ]

    required_osfi_fields = {
        "institution_name": institution,
        "incident_reference": f"OSFI-{now.strftime('%Y%m%d-%H%M%S')}",
        "date_time_detected_utc": first_trigger.isoformat() if first_trigger else None,
        "reporting_deadline_utc": deadline.isoformat() if deadline else None,
        "regulatory_timeframe_met": False if overdue else True,
        "incident_status": (
            "contained"
            if all(event.get("contained_at") for event in events)
            else "active"
        ),
        "highest_observed_severity": max_severity,
        "systems_affected": sorted(
            {system for event in events for system in event["systems_affected"]}
        ),
        "known_customer_impact": any(
            event["personal_data_compromised"] for event in events
        ),
        "estimated_records_affected": sum(
            event["records_affected"] for event in events
        ),
        "estimated_financial_loss_cad": round(
            sum(event["financial_loss_cad"] for event in events), 2
        ),
        "prepared_by": prepared_by,
        "prepared_at_utc": now.isoformat(),
    }

    required_pipeda_fields = {
        "institution_name": institution,
        "opc_notification_required": len(pipeda_events) > 0,
        "privacy_breach_reference": f"PIPEDA-{now.strftime('%Y%m%d-%H%M%S')}",
        "real_risk_of_significant_harm_assessed": len(pipeda_events) > 0,
        "individual_notification_required": len(pipeda_events) > 0,
        "total_records_with_personal_information": sum(
            event["records_affected"]
            for event in events
            if event["personal_data_compromised"]
        ),
        "data_elements_impacted": sorted(
            {
                dtype
                for event in events
                for dtype in event["data_types"]
                if event["personal_data_compromised"]
            }
        ),
        "prepared_by": prepared_by,
        "prepared_at_utc": now.isoformat(),
    }

    return {
        "classification_version": "1.0",
        "generated_at_utc": now.isoformat(),
        "incident_window": {
            "first_detected_utc": (
                min(event["detected_at"] for event in events).isoformat()
                if events
                else None
            ),
            "latest_detected_utc": (
                max(event["detected_at"] for event in events).isoformat()
                if events
                else None
            ),
        },
        "regulatory_assessment": {
            "osfi": {
                "twenty_four_hour_threshold_triggered": first_trigger is not None,
                "clock_start_utc": first_trigger.isoformat() if first_trigger else None,
                "reporting_deadline_utc": deadline.isoformat() if deadline else None,
                "deadline_overdue": overdue,
                "reportable_event_count": len(reportable_events),
                "notification_draft": required_osfi_fields,
            },
            "pipeda": {
                "privacy_commissioner_notification_required": len(pipeda_events) > 0,
                "triggering_event_count": len(pipeda_events),
                "notification_draft": required_pipeda_fields,
            },
        },
        "events": enriched_events,
    }


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    file_format = detect_format(input_path, args.format)
    raw_events = load_events(input_path, file_format)
    events = [
        normalize_event(raw_event, index + 1)
        for index, raw_event in enumerate(raw_events)
    ]

    report = compute_report(events, args.institution, args.prepared_by)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    osfi = report["regulatory_assessment"]["osfi"]
    pipeda = report["regulatory_assessment"]["pipeda"]

    print(f"Processed events: {len(events)}")
    print(
        f"OSFI 24-hour threshold triggered: {osfi['twenty_four_hour_threshold_triggered']}"
    )
    print(f"OSFI reporting deadline (UTC): {osfi['reporting_deadline_utc']}")
    print(
        "PIPEDA OPC notification required: "
        f"{pipeda['privacy_commissioner_notification_required']}"
    )
    print(f"Notification draft written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
