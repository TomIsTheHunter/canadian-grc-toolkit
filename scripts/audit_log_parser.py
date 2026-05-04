"""Parse privileged access audit logs and flag control violations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = {
    "actor_id",
    "event_type",
    "timestamp",
    "mfa_verified",
    "log_destination",
}
APPROVED_DESTINATIONS = {"siem-prod", "immutable-audit-store"}


def _read_json_lines(
    input_path: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Read JSONL events and collect record-level parsing findings."""

    events: list[dict[str, Any]] = []
    findings: list[dict[str, Any]] = []

    with input_path.open("r", encoding="utf-8") as handle:
        for index, raw in enumerate(handle, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError as exc:
                findings.append(
                    {
                        "line": index,
                        "issue": "invalid_json",
                        "detail": str(exc),
                    }
                )
                continue

            if not isinstance(payload, dict):
                findings.append(
                    {
                        "line": index,
                        "issue": "invalid_record_type",
                        "detail": "record must be a JSON object",
                    }
                )
                continue

            payload["_line"] = index
            events.append(payload)

    return events, findings


def _check_event(event: dict[str, Any]) -> list[dict[str, Any]]:
    """Validate one event against required fields and destination controls."""

    line = int(event.get("_line", -1))
    findings: list[dict[str, Any]] = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in event:
            findings.append(
                {
                    "line": line,
                    "issue": "missing_required_field",
                    "field": field,
                }
            )

    if "mfa_verified" in event and event["mfa_verified"] is not True:
        findings.append(
            {
                "line": line,
                "issue": "invalid_mfa",
                "detail": "mfa_verified must be true",
            }
        )

    if (
        "log_destination" in event
        and event["log_destination"] not in APPROVED_DESTINATIONS
    ):
        findings.append(
            {
                "line": line,
                "issue": "unapproved_log_destination",
                "detail": f"{event['log_destination']} is not in approved destinations",
            }
        )

    return findings


def parse_audit_log(input_path: Path) -> list[dict[str, Any]]:
    """Parse a JSONL audit log and return all detected findings."""

    events, findings = _read_json_lines(input_path)

    for event in events:
        findings.extend(_check_event(event))

    return findings


def main() -> int:
    """CLI entry point for privileged access audit log validation."""

    parser = argparse.ArgumentParser(
        description="Parse privileged access audit logs and flag OSFI reporting gaps."
    )
    parser.add_argument(
        "--input", required=True, type=Path, help="Path to JSONL audit log"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output JSON file for findings",
    )
    args = parser.parse_args()

    findings = parse_audit_log(args.input)
    result = {"compliant": len(findings) == 0, "findings": findings}

    output = json.dumps(result, indent=2)
    print(output)

    if args.output is not None:
        args.output.write_text(output + "\n", encoding="utf-8")

    return 0 if len(findings) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
