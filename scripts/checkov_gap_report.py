#!/usr/bin/env python3
"""
checkov_gap_report.py
---------------------
Parse Checkov JSON output and produce a formatted compliance gap report.

Usage:
    python checkov_gap_report.py results.json
    python checkov_gap_report.py results.json --output gap_report.csv
    python checkov_gap_report.py results.json --framework terraform
    python checkov_gap_report.py results.json --severity HIGH
    python checkov_gap_report.py results.json --framework terraform --output out.csv --severity CRITICAL
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("Missing dependency: pandas.  Run: pip install pandas")

try:
    from tabulate import tabulate
except ImportError:
    sys.exit("Missing dependency: tabulate.  Run: pip install tabulate")


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

STATUS_PASSED = "PASSED"
STATUS_FAILED = "FAILED"
STATUS_SKIPPED = "SKIPPED"

HIGH_SEVERITY_LEVELS = {"HIGH", "CRITICAL"}

TABULATE_FMT = "simple"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_checks(raw_results: dict, status: str) -> list[dict]:
    """
    Return a flat list of normalised check dicts from a results bucket.

    Checkov nests checks under ``results.passed_checks``,
    ``results.failed_checks``, and ``results.skipped_checks``.
    Each check may be a plain dict or, for multi-resource runs, wrapped inside
    a list-of-dicts at the top level.  We flatten both shapes.
    """
    key_map = {
        STATUS_PASSED: "passed_checks",
        STATUS_FAILED: "failed_checks",
        STATUS_SKIPPED: "skipped_checks",
    }
    bucket_key = key_map[status]

    # Checkov can emit a single results dict or a list of them (multi-runner).
    results_list = raw_results if isinstance(raw_results, list) else [raw_results]

    records: list[dict] = []
    for runner_result in results_list:
        checks = runner_result.get("results", {}).get(bucket_key, [])
        for chk in checks:
            records.append(_normalise_check(chk, status))
    return records


def _normalise_check(chk: dict, status: str) -> dict:
    """Flatten a single Checkov check entry into a uniform record."""
    check_result = chk.get("check_result", {})

    # Severity may live under check_result.results_configuration or directly
    severity = (
        check_result.get("severity")
        or chk.get("severity")
        or ""
    )
    if isinstance(severity, str):
        severity = severity.upper()

    # Skip / suppress reason (present only on skipped checks)
    suppress_comment = check_result.get("suppress_comment", "")

    return {
        "check_id": chk.get("check_id", ""),
        "check_type": chk.get("check_type", chk.get("type", "")),
        "status": status,
        "resource": chk.get("resource", ""),
        "file_path": chk.get("file_path", ""),
        "guideline": chk.get("guideline", ""),
        "severity": severity,
        "suppress_comment": suppress_comment,
    }


def load_checkov_json(path: Path) -> dict:
    """Read and validate the Checkov JSON output file."""
    if not path.exists():
        sys.exit(f"Error: file not found – {path}")

    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        sys.exit(f"Error: malformed JSON in {path} – {exc}")

    # Accept a single runner dict or a list of runner dicts
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, list) and all(isinstance(item, dict) for item in raw):
        # Wrap list as a pseudo-results structure for unified handling
        return raw  # _extract_checks handles lists natively
    sys.exit(f"Error: unexpected top-level JSON type in {path} – expected object or array")


def build_dataframe(raw_results, framework_filter: str | None, severity_filter: str | None) -> pd.DataFrame:
    """
    Build a tidy DataFrame from all check buckets, applying optional filters.
    """
    records: list[dict] = []
    for status in (STATUS_PASSED, STATUS_FAILED, STATUS_SKIPPED):
        records.extend(_extract_checks(raw_results, status))

    if not records:
        return pd.DataFrame(columns=[
            "check_id", "check_type", "status", "resource",
            "file_path", "guideline", "severity", "suppress_comment",
        ])

    df = pd.DataFrame(records)

    # --framework filter: match against check_type (case-insensitive)
    if framework_filter:
        mask = df["check_type"].str.lower() == framework_filter.lower()
        df = df[mask].copy()

    # --severity filter: only applies to FAILED checks; keep all others intact
    if severity_filter:
        target_levels = {severity_filter.upper()} & HIGH_SEVERITY_LEVELS
        if not target_levels:
            sys.exit(
                f"Error: --severity must be HIGH or CRITICAL, got '{severity_filter}'"
            )
        failed_mask = df["status"] == STATUS_FAILED
        severity_mask = df["severity"].isin(target_levels)
        # Keep non-failed rows unchanged; keep failed rows only if severity matches
        df = df[~failed_mask | severity_mask].copy()

    return df


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def _truncate(value: str, max_len: int = 60) -> str:
    """Truncate long strings for console readability."""
    s = str(value)
    return s if len(s) <= max_len else s[: max_len - 3] + "..."


def print_summary(df: pd.DataFrame) -> None:
    total = len(df)
    passed = (df["status"] == STATUS_PASSED).sum()
    failed = (df["status"] == STATUS_FAILED).sum()
    skipped = (df["status"] == STATUS_SKIPPED).sum()
    pass_rate = (passed / total * 100) if total else 0.0

    rows = [
        ["Total Checks", total],
        ["Passed", passed],
        ["Failed", failed],
        ["Skipped", skipped],
        ["Pass Rate", f"{pass_rate:.1f}%"],
    ]
    print("\n" + "=" * 60)
    print("  SUMMARY")
    print("=" * 60)
    print(tabulate(rows, headers=["Metric", "Value"], tablefmt=TABULATE_FMT))


def print_failed(df: pd.DataFrame) -> None:
    failed = df[df["status"] == STATUS_FAILED].copy()
    print("\n" + "=" * 60)
    print("  FAILED CONTROLS")
    print("=" * 60)

    if failed.empty:
        print("  No failed controls.\n")
        return

    failed_sorted = failed.sort_values("check_id")
    display_cols = ["check_id", "resource", "file_path"]
    table_rows = [
        [
            row["check_id"],
            _truncate(row["resource"]),
            _truncate(row["file_path"]),
        ]
        for _, row in failed_sorted.iterrows()
    ]
    print(tabulate(table_rows, headers=["Check ID", "Resource", "File Path"], tablefmt=TABULATE_FMT))


def print_skipped(df: pd.DataFrame) -> None:
    skipped = df[df["status"] == STATUS_SKIPPED].copy()
    print("\n" + "=" * 60)
    print("  SKIPPED CONTROLS")
    print("=" * 60)

    if skipped.empty:
        print("  No skipped controls.\n")
        return

    table_rows = [
        [
            row["check_id"],
            _truncate(row["resource"]),
            _truncate(row["suppress_comment"]) if row["suppress_comment"] else "(no reason recorded)",
        ]
        for _, row in skipped.iterrows()
    ]
    print(tabulate(table_rows, headers=["Check ID", "Resource", "Suppress Comment"], tablefmt=TABULATE_FMT))


def print_na_note() -> None:
    print("\n" + "-" * 60)
    print(
        "N/A: Passed controls are omitted from this gap report.\n"
        "     They are counted in the Summary above but not listed\n"
        "     individually, as they represent compliant configurations\n"
        "     that require no remediation action."
    )
    print("-" * 60 + "\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Parse Checkov JSON output and produce a compliance gap report."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "input",
        metavar="CHECKOV_JSON",
        help="Path to the Checkov JSON results file.",
    )
    parser.add_argument(
        "--output",
        metavar="CSV_PATH",
        default=None,
        help="Optional path to export the full DataFrame as CSV.",
    )
    parser.add_argument(
        "--framework",
        metavar="FRAMEWORK",
        default=None,
        help=(
            "Filter results to a specific Checkov check_type "
            "(e.g. terraform, kubernetes, cloudformation)."
        ),
    )
    parser.add_argument(
        "--severity",
        metavar="LEVEL",
        default=None,
        choices=["HIGH", "CRITICAL"],
        help=(
            "When set, filter FAILED checks to only those whose severity "
            "metadata matches HIGH or CRITICAL."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)

    raw_results = load_checkov_json(input_path)
    df = build_dataframe(raw_results, args.framework, args.severity)

    if df.empty:
        print(
            "Warning: No checks found after applying filters. "
            "Verify the input file and filter options."
        )
        return

    # Console report
    print_summary(df)
    print_failed(df)
    print_skipped(df)
    print_na_note()

    # Optional CSV export
    if args.output:
        output_path = Path(args.output)
        export_cols = ["check_id", "check_type", "status", "resource", "file_path", "guideline"]
        df[export_cols].to_csv(output_path, index=False)
        print(f"CSV exported to: {output_path.resolve()}\n")


if __name__ == "__main__":
    main()
