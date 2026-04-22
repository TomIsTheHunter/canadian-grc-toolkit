#!/usr/bin/env python3
"""Task runner for common local/CI workflows.

Usage:
  python scripts/task_runner.py test
  python scripts/task_runner.py lint
  python scripts/task_runner.py all-reports
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def _run(command: list[str]) -> None:
    subprocess.run(command, cwd=ROOT, check=True)


def task_test() -> None:
    _run([sys.executable, "-m", "pytest", "scripts/tests/", "-v", "--tb=short"])


def task_lint() -> None:
    _run([sys.executable, "-m", "ruff", "check", "scripts"])
    _run([sys.executable, "-m", "black", "--check", "scripts"])


def task_report_risk() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "scripts.risk_register",
            "--input",
            "scripts/sample_risk_register.json",
            "--output-json",
            "reports/risk_register_output.json",
            "--output-md",
            "reports/risk_register_report.md",
        ]
    )


def task_report_kpi() -> None:
    _run(
        [
            sys.executable,
            "scripts/grc_kpi_report.py",
            "--input",
            "scripts/sample_risk_register.json",
            "--output",
            "reports/grc_kpi_dashboard.md",
            "--as-of",
            "2026-10-21",
        ]
    )


def task_classify_incident() -> None:
    _run(
        [
            sys.executable,
            "scripts/osfi_incident_classifier.py",
            "--input",
            "scripts/mock_security_logs.csv",
            "--output",
            "reports/notification_draft.json",
            "--institution",
            "Maple Bank",
            "--prepared-by",
            "Cyber Incident Response Team",
        ]
    )


def task_fair() -> None:
    _run(
        [
            sys.executable,
            "scripts/fair_calculator.py",
            "--scenario",
            "scripts/fair_scenario.json",
            "--iterations",
            "2000",
            "--output",
            "reports/fair_results.json",
        ]
    )


def task_all_reports() -> None:
    task_report_risk()
    task_report_kpi()
    task_classify_incident()
    task_fair()


def task_full_compliance() -> None:
    _run(
        [
            sys.executable,
            "main.py",
            "--iac-dir",
            ".",
            "--opa-input",
            "scripts/fair_scenario.json",
            "--vendor-data",
            "scripts/sample_vendor_data.json",
            "--risk-register",
            "scripts/sample_risk_register.json",
            "--policy-dir",
            "policies",
        ]
    )


TASKS = {
    "test": task_test,
    "lint": task_lint,
    "report-risk": task_report_risk,
    "report-kpi": task_report_kpi,
    "classify-incident": task_classify_incident,
    "fair": task_fair,
    "all-reports": task_all_reports,
    "full-compliance": task_full_compliance,
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", choices=sorted(TASKS.keys()))
    args = parser.parse_args()

    TASKS[args.task]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
