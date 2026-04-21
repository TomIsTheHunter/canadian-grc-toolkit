#!/usr/bin/env python3
"""Generate a board-ready GRC KPI dashboard from the risk register JSON.

The risk register schema in this repository tracks risks, controls, owners,
residual scores, and next review dates. It does not model issue-management
workflow states directly, so this dashboard derives operational KPI views using
transparent assumptions suitable for a sample reporting pack:

- Each risk is treated as an open monitoring item until it is removed from the
  register.
- Control effectiveness is measured as weighted residual risk reduction across
  the portfolio.
- Finding severity is derived from residual score bands.
- Finding age is inferred from the review cycle and next review date.
- Prior-period trend values are deterministic mock baselines and are labeled as
  such in the report.

Usage:
  python scripts/grc_kpi_report.py \
    --input scripts/sample_risk_register.json \
    --output reports/grc_kpi_dashboard.md \
    --as-of 2026-10-21
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

try:
    from scripts.risk_register import process_register
except ModuleNotFoundError:
    from risk_register import process_register

_DEFAULT_OUTPUT = Path("reports") / "grc_kpi_dashboard.md"

_REVIEW_CYCLE_DAYS = {
    "quarterly": 90,
    "semi-annual": 180,
    "annual": 365,
}

_SEVERITY_BANDS = (
    (15, "Critical"),
    (10, "High"),
    (5, "Medium"),
    (0, "Low"),
)

_AGE_BUCKETS = (
    (30, "0-30 days"),
    (60, "31-60 days"),
    (90, "61-90 days"),
)

_SEVERITY_ORDER = ["Critical", "High", "Medium", "Low"]
_AGE_ORDER = ["0-30 days", "31-60 days", "61-90 days", ">90 days"]
_TREATMENT_ORDER = ["Complete", "In Progress", "Planned", "Behind Schedule"]


def _parse_iso_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _safe_pct(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return round((numerator / denominator) * 100, 1)


def _severity_from_score(score: int) -> str:
    for threshold, label in _SEVERITY_BANDS:
        if score >= threshold:
            return label
    return "Low"


def _age_bucket(age_days: int) -> str:
    for ceiling, label in _AGE_BUCKETS:
        if age_days <= ceiling:
            return label
    return ">90 days"


def _infer_open_date(review_date: date, review_cycle_days: int) -> date:
    return review_date - timedelta(days=review_cycle_days)


def _risk_treatment_completion(risk: dict[str, Any]) -> float:
    inherent_score = risk["inherent_risk"]["score"]
    residual_score = risk["residual_risk"]["score"]
    reduction = max(inherent_score - residual_score, 0)
    return _safe_pct(reduction, inherent_score)


def _risk_treatment_status(risk: dict[str, Any], as_of: date) -> str:
    completion = _risk_treatment_completion(risk)
    review_date = _parse_iso_date(risk["review_date"])
    overdue = as_of > review_date

    if overdue and risk["rag_status"] != "Green":
        return "Behind Schedule"
    if completion >= 50 and risk["rag_status"] == "Green":
        return "Complete"
    if completion >= 25:
        return "In Progress"
    return "Planned"


def analyze_kpis(enriched: dict[str, Any], as_of: date | None = None) -> dict[str, Any]:
    """Return derived KPI data for the supplied enriched risk register."""
    as_of = as_of or date.today()
    meta = enriched["register_metadata"]
    risks = enriched["risks"]
    review_cycle_days = _REVIEW_CYCLE_DAYS[meta["review_cycle"]]

    total_inherent = sum(risk["inherent_risk"]["score"] for risk in risks)
    total_residual = sum(risk["residual_risk"]["score"] for risk in risks)
    control_effectiveness = _safe_pct(total_inherent - total_residual, total_inherent)

    findings: list[dict[str, Any]] = []
    category_rollup: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "risk_count": 0,
            "completion_total": 0.0,
            "status_counts": Counter(),
            "inherent_total": 0,
            "residual_total": 0,
        }
    )
    severity_age_counts: dict[str, Counter[str]] = {
        severity: Counter() for severity in _SEVERITY_ORDER
    }

    overdue_items: list[dict[str, Any]] = []

    for risk in risks:
        review_date = _parse_iso_date(risk["review_date"])
        open_date = _infer_open_date(review_date, review_cycle_days)
        age_days = max((as_of - open_date).days, 0)
        overdue_days = max((as_of - review_date).days, 0)
        severity = _severity_from_score(risk["residual_risk"]["score"])
        completion = _risk_treatment_completion(risk)
        treatment_status = _risk_treatment_status(risk, as_of)

        finding = {
            "id": risk["id"],
            "title": risk["title"],
            "category": risk["category"],
            "owner": risk["owner"],
            "severity": severity,
            "age_days": age_days,
            "age_bucket": _age_bucket(age_days),
            "review_date": review_date.isoformat(),
            "overdue_days": overdue_days,
            "residual_score": risk["residual_risk"]["score"],
            "treatment_completion": completion,
            "treatment_status": treatment_status,
        }
        findings.append(finding)
        severity_age_counts[severity][finding["age_bucket"]] += 1

        category_metrics = category_rollup[risk["category"]]
        category_metrics["risk_count"] += 1
        category_metrics["completion_total"] += completion
        category_metrics["status_counts"][treatment_status] += 1
        category_metrics["inherent_total"] += risk["inherent_risk"]["score"]
        category_metrics["residual_total"] += risk["residual_risk"]["score"]

        if overdue_days > 0:
            overdue_items.append(
                {
                    "id": risk["id"],
                    "title": risk["title"],
                    "owner": risk["owner"],
                    "category": risk["category"],
                    "review_date": review_date.isoformat(),
                    "overdue_days": overdue_days,
                    "residual_score": risk["residual_risk"]["score"],
                    "flag": "Owner action required",
                }
            )

    category_progress = []
    for category in sorted(category_rollup):
        data = category_rollup[category]
        reduction_pct = _safe_pct(
            data["inherent_total"] - data["residual_total"],
            data["inherent_total"],
        )
        category_progress.append(
            {
                "category": category,
                "risk_count": data["risk_count"],
                "avg_completion": round(
                    data["completion_total"] / data["risk_count"], 1
                ),
                "reduction_pct": reduction_pct,
                "complete": data["status_counts"]["Complete"],
                "in_progress": data["status_counts"]["In Progress"],
                "planned": data["status_counts"]["Planned"],
                "behind_schedule": data["status_counts"]["Behind Schedule"],
            }
        )

    open_findings = len(findings)
    high_or_critical = sum(
        1 for finding in findings if finding["severity"] in {"High", "Critical"}
    )
    avg_treatment_completion = round(
        sum(finding["treatment_completion"] for finding in findings) / open_findings,
        1,
    )

    trend_metrics = _mock_prior_period(
        current={
            "control_effectiveness": control_effectiveness,
            "high_or_critical_findings": high_or_critical,
            "overdue_items": len(overdue_items),
            "avg_treatment_completion": avg_treatment_completion,
        }
    )

    return {
        "metadata": {
            "title": meta["title"],
            "version": meta.get("version", "—"),
            "created_by": meta.get("created_by", "—"),
            "review_cycle": meta["review_cycle"],
            "description": meta.get("description", ""),
            "as_of": as_of.isoformat(),
        },
        "summary": {
            "control_effectiveness": control_effectiveness,
            "open_findings": open_findings,
            "high_or_critical_findings": high_or_critical,
            "overdue_items": len(overdue_items),
            "avg_treatment_completion": avg_treatment_completion,
        },
        "severity_age": severity_age_counts,
        "category_progress": category_progress,
        "overdue_items": sorted(
            overdue_items, key=lambda item: item["overdue_days"], reverse=True
        ),
        "findings": findings,
        "trend": trend_metrics,
    }


def _mock_prior_period(current: dict[str, Any]) -> list[dict[str, Any]]:
    """Return deterministic mock prior-period values for trend reporting."""
    prior = {
        "control_effectiveness": max(
            round(current["control_effectiveness"] - 7.4, 1), 0.0
        ),
        "high_or_critical_findings": current["high_or_critical_findings"] + 1,
        "overdue_items": current["overdue_items"] + 2,
        "avg_treatment_completion": max(
            round(current["avg_treatment_completion"] - 9.6, 1), 0.0
        ),
    }

    definitions = [
        ("Control effectiveness rate", "control_effectiveness", True, "%"),
        ("High / critical findings", "high_or_critical_findings", False, "count"),
        ("Overdue review items", "overdue_items", False, "count"),
        ("Average treatment completion", "avg_treatment_completion", True, "%"),
    ]

    rows = []
    for label, key, higher_is_better, unit in definitions:
        current_value = current[key]
        prior_value = prior[key]
        delta = round(current_value - prior_value, 1)
        if delta == 0:
            trend = "Flat"
        elif (delta > 0 and higher_is_better) or (delta < 0 and not higher_is_better):
            trend = "Improved"
        else:
            trend = "Deteriorated"

        rows.append(
            {
                "metric": label,
                "current": current_value,
                "prior": prior_value,
                "delta": delta,
                "trend": trend,
                "unit": unit,
            }
        )

    return rows


def render_markdown(kpis: dict[str, Any]) -> str:
    """Render KPI data to a Markdown dashboard."""
    meta = kpis["metadata"]
    summary = kpis["summary"]

    lines = [
        f"# GRC KPI Dashboard — {meta['title']}",
        "",
        "| Field | Value |",
        "|-------|-------|",
        f"| Version | {meta['version']} |",
        f"| Created by | {meta['created_by']} |",
        f"| Review cycle | {meta['review_cycle']} |",
        f"| Reporting date | {meta['as_of']} |",
        "",
    ]

    if meta["description"]:
        lines.extend([f"> {meta['description']}", ""])

    lines.extend(
        [
            "> Assumptions: risks are treated as open monitoring items, control effectiveness is measured as weighted residual risk reduction, finding age is inferred from the review cycle, and prior-period trend values are mock baselines for demonstration only.",
            "",
            "## Executive Summary",
            "",
            "| KPI | Current Period |",
            "|-----|----------------|",
            f"| Control effectiveness rate | {summary['control_effectiveness']:.1f}% |",
            f"| Open findings | {summary['open_findings']} |",
            f"| High / critical findings | {summary['high_or_critical_findings']} |",
            f"| Overdue review items | {summary['overdue_items']} |",
            f"| Average treatment completion | {summary['avg_treatment_completion']:.1f}% |",
            "",
            "## Control Effectiveness",
            "",
            "| Category | Risks | Avg treatment completion | Portfolio risk reduction | Complete | In progress | Planned | Behind schedule |",
            "|----------|------:|-------------------------:|-------------------------:|---------:|------------:|--------:|----------------:|",
        ]
    )

    for category in kpis["category_progress"]:
        lines.append(
            f"| {category['category']} | {category['risk_count']} | {category['avg_completion']:.1f}% | "
            f"{category['reduction_pct']:.1f}% | {category['complete']} | {category['in_progress']} | "
            f"{category['planned']} | {category['behind_schedule']} |"
        )

    lines.extend(
        [
            "",
            "## Open Findings By Severity And Age",
            "",
            "| Severity | 0-30 days | 31-60 days | 61-90 days | >90 days | Total |",
            "|----------|----------:|-----------:|-----------:|----------:|------:|",
        ]
    )

    for severity in _SEVERITY_ORDER:
        age_counts = kpis["severity_age"][severity]
        total = sum(age_counts[bucket] for bucket in _AGE_ORDER)
        lines.append(
            f"| {severity} | {age_counts['0-30 days']} | {age_counts['31-60 days']} | "
            f"{age_counts['61-90 days']} | {age_counts['>90 days']} | {total} |"
        )

    lines.extend(
        [
            "",
            "## Overdue Items",
            "",
        ]
    )

    if kpis["overdue_items"]:
        lines.extend(
            [
                "| ID | Title | Category | Owner | Review date | Days overdue | Residual score | Flag |",
                "|----|-------|----------|-------|-------------|-------------:|---------------:|------|",
            ]
        )
        for item in kpis["overdue_items"]:
            lines.append(
                f"| {item['id']} | {item['title']} | {item['category']} | {item['owner']} | "
                f"{item['review_date']} | {item['overdue_days']} | {item['residual_score']} | {item['flag']} |"
            )
    else:
        lines.extend(
            [
                "All review items are within the scheduled review date window.",
            ]
        )

    lines.extend(
        [
            "",
            "## Trend Vs Prior Period",
            "",
            "| Metric | Current | Prior period (mock) | Delta | Direction |",
            "|--------|--------:|--------------------:|------:|-----------|",
        ]
    )

    for row in kpis["trend"]:
        if row["unit"] == "%":
            current_value = f"{row['current']:.1f}%"
            prior_value = f"{row['prior']:.1f}%"
            delta_value = f"{row['delta']:+.1f} pts"
        else:
            current_value = str(int(row["current"]))
            prior_value = str(int(row["prior"]))
            delta_value = f"{int(row['delta']):+d}"

        lines.append(
            f"| {row['metric']} | {current_value} | {prior_value} | {delta_value} | {row['trend']} |"
        )

    return "\n".join(lines) + "\n"


def write_markdown_report(kpis: dict[str, Any], output_path: Path) -> None:
    """Write a Markdown dashboard to disk."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(kpis), encoding="utf-8")
    print(f"[✓] KPI dashboard written → {output_path}")


def _load_register(input_path: Path) -> dict[str, Any]:
    with input_path.open(encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("scripts") / "sample_risk_register.json",
        help="Path to the risk register JSON file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=_DEFAULT_OUTPUT,
        help="Path to write the Markdown KPI dashboard.",
    )
    parser.add_argument(
        "--as-of",
        type=_parse_iso_date,
        default=date.today(),
        help="Reporting date in YYYY-MM-DD format. Defaults to today.",
    )
    args = parser.parse_args(argv)

    enriched = process_register(_load_register(args.input))
    kpis = analyze_kpis(enriched, as_of=args.as_of)
    write_markdown_report(kpis, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
