"""
FAIR (Factor Analysis of Information Risk) Quantitative Risk Calculator
=======================================================================
Implements a Monte Carlo simulation over the core FAIR taxonomy:

    TEF  (Threat Event Frequency)      — how often a threat agent acts (events/year)
    VULN (Vulnerability)               — probability that a threat event becomes a loss event (0–1)
    LEF  (Loss Event Frequency)        = TEF × VULN  (derived, also sampled)
    PLM  (Primary Loss Magnitude)      — financial impact per loss event (CAD)
    SLM  (Secondary Loss Magnitude)    — regulatory / reputational loss per loss event (CAD)
    ALE  (Annualised Loss Exposure)    = LEF × (PLM + SLM)  (the board-facing risk number)

Each input is expressed as a (min, most-likely, max) PERT triplet.  A
Beta-PERT distribution is fitted to each triplet and sampled in the
simulation, which produces stable, bell-shaped results even with a
small iteration count.

Usage examples
--------------
# Run with a scenario JSON file (recommended):
    python fair_calculator.py --scenario fair_scenario.json

# Override iterations and output path:
    python fair_calculator.py --scenario fair_scenario.json --iterations 100000 --output fair_results.json

# Run the built-in demo scenario without any file:
    python fair_calculator.py --demo
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from pathlib import Path
from typing import Any, Dict, List, Tuple


# ---------------------------------------------------------------------------
# Beta-PERT sampling
# ---------------------------------------------------------------------------


def _pert_alpha_beta(
    minimum: float, mode: float, maximum: float, gamma: float = 4.0
) -> Tuple[float, float]:
    """Return (alpha, beta) shape parameters for the Beta-PERT distribution.

    Standard derivation:
        v    = gamma + 2                         (concentration, default 6)
        mean = (min + gamma * mode + max) / v
        alpha = v * (mean - min) / (max - min)
        beta  = v * (max - mean) / (max - min)
    """
    v = gamma + 2.0
    mean = (minimum + gamma * mode + maximum) / v
    if abs(maximum - minimum) < 1e-10:
        return 1.0, 1.0
    alpha = v * (mean - minimum) / (maximum - minimum)
    beta = v * (maximum - mean) / (maximum - minimum)
    return max(alpha, 1e-6), max(beta, 1e-6)


def sample_pert(
    minimum: float, mode: float, maximum: float, rng: random.Random
) -> float:
    """Draw one sample from the Beta-PERT distribution for the given triplet."""
    if abs(maximum - minimum) < 1e-10:
        return minimum
    alpha, beta = _pert_alpha_beta(minimum, mode, maximum)
    scaled = rng.betavariate(alpha, beta)
    return minimum + scaled * (maximum - minimum)


# ---------------------------------------------------------------------------
# Scenario parsing
# ---------------------------------------------------------------------------

_REQUIRED_TRIPLET_FIELDS = {"min", "most_likely", "max"}
_SCENARIO_FIELDS = {
    "tef": "Threat Event Frequency (events/year)",
    "vulnerability": "Vulnerability – probability of action succeeding (0–1)",
    "plm": "Primary Loss Magnitude per event (CAD)",
}
_OPTIONAL_SCENARIO_FIELDS = {
    "slm": "Secondary Loss Magnitude per event (CAD) – e.g. fines, reputational loss",
}


def _parse_triplet(
    data: Dict[str, Any], field: str, label: str
) -> Tuple[float, float, float]:
    block = data.get(field)
    if block is None:
        raise ValueError(f"Missing required scenario field: '{field}' ({label})")
    if not _REQUIRED_TRIPLET_FIELDS.issubset(block.keys()):
        raise ValueError(
            f"Field '{field}' must contain 'min', 'most_likely', and 'max'. Got: {list(block.keys())}"
        )
    low = float(block["min"])
    ml = float(block["most_likely"])
    high = float(block["max"])
    if not (low <= ml <= high):
        raise ValueError(
            f"Field '{field}': values must satisfy min <= most_likely <= max. "
            f"Got {low}, {ml}, {high}."
        )
    if field == "vulnerability" and not (0.0 <= low and high <= 1.0):
        raise ValueError(
            f"Field '{field}': all values must be in [0, 1]. Got {low}, {ml}, {high}."
        )
    return low, ml, high


def parse_scenario(data: Dict[str, Any]) -> Dict[str, Any]:
    scenario: Dict[str, Any] = {
        "name": str(data.get("name", "Unnamed Scenario")),
        "description": str(data.get("description", "")),
    }
    for field, label in _SCENARIO_FIELDS.items():
        scenario[field] = _parse_triplet(data, field, label)
    # Optional secondary loss magnitude
    if "slm" in data:
        scenario["slm"] = _parse_triplet(data, "slm", _OPTIONAL_SCENARIO_FIELDS["slm"])
    else:
        scenario["slm"] = (0.0, 0.0, 0.0)
    return scenario


# ---------------------------------------------------------------------------
# Monte Carlo simulation engine
# ---------------------------------------------------------------------------


def simulate(
    scenario: Dict[str, Any], iterations: int = 100_000, seed: int | None = 42
) -> List[float]:
    """
    Run the FAIR simulation.
    Returns a list of `iterations` ALE (Annualised Loss Exposure) samples in CAD.
    """
    rng = random.Random(seed)
    ale_samples: List[float] = []

    tef_min, tef_ml, tef_max = scenario["tef"]
    vuln_min, vuln_ml, vuln_max = scenario["vulnerability"]
    plm_min, plm_ml, plm_max = scenario["plm"]
    slm_min, slm_ml, slm_max = scenario["slm"]

    for _ in range(iterations):
        tef = sample_pert(tef_min, tef_ml, tef_max, rng)
        vuln = sample_pert(vuln_min, vuln_ml, vuln_max, rng)
        lef = tef * vuln
        plm = sample_pert(plm_min, plm_ml, plm_max, rng)
        slm = sample_pert(slm_min, slm_ml, slm_max, rng)
        ale = lef * (plm + slm)
        ale_samples.append(ale)

    return ale_samples


# ---------------------------------------------------------------------------
# Result aggregation
# ---------------------------------------------------------------------------


def _percentile(sorted_data: List[float], pct: float) -> float:
    if not sorted_data:
        return 0.0
    index = (len(sorted_data) - 1) * pct / 100.0
    lower = int(index)
    upper = min(lower + 1, len(sorted_data) - 1)
    fraction = index - lower
    return sorted_data[lower] + fraction * (sorted_data[upper] - sorted_data[lower])


def _find_mode(sorted_data: List[float], bins: int = 200) -> float:
    """Estimate the mode via a histogram on the sorted samples."""
    if len(sorted_data) < 2:
        return sorted_data[0] if sorted_data else 0.0
    low, high = sorted_data[0], sorted_data[-1]
    if abs(high - low) < 1e-10:
        return low
    width = (high - low) / bins
    counts = [0] * bins
    for value in sorted_data:
        bucket = min(int((value - low) / width), bins - 1)
        counts[bucket] += 1
    peak_bucket = max(range(bins), key=lambda b: counts[b])
    return low + (peak_bucket + 0.5) * width


def aggregate(ale_samples: List[float], scenario: Dict[str, Any]) -> Dict[str, Any]:
    sorted_samples = sorted(ale_samples)
    mean = statistics.mean(ale_samples)
    stdev = statistics.stdev(ale_samples) if len(ale_samples) > 1 else 0.0

    p10 = _percentile(sorted_samples, 10)
    p50 = _percentile(sorted_samples, 50)
    p90 = _percentile(sorted_samples, 90)
    p95 = _percentile(sorted_samples, 95)
    mode = _find_mode(sorted_samples)

    # Risk tier based on 90th-percentile ALE (CAD) — typical board thresholds
    if p90 >= 50_000_000:
        risk_tier = "CRITICAL"
    elif p90 >= 10_000_000:
        risk_tier = "HIGH"
    elif p90 >= 1_000_000:
        risk_tier = "MEDIUM"
    else:
        risk_tier = "LOW"

    def fmt(value: float) -> str:
        return f"${value:,.0f} CAD"

    return {
        "scenario_name": scenario["name"],
        "scenario_description": scenario["description"],
        "simulation": {
            "iterations": len(ale_samples),
        },
        "inputs": {
            "threat_event_frequency_per_year": {
                "min": scenario["tef"][0],
                "most_likely": scenario["tef"][1],
                "max": scenario["tef"][2],
            },
            "vulnerability_probability": {
                "min": scenario["vulnerability"][0],
                "most_likely": scenario["vulnerability"][1],
                "max": scenario["vulnerability"][2],
            },
            "primary_loss_magnitude_cad": {
                "min": scenario["plm"][0],
                "most_likely": scenario["plm"][1],
                "max": scenario["plm"][2],
            },
            "secondary_loss_magnitude_cad": {
                "min": scenario["slm"][0],
                "most_likely": scenario["slm"][1],
                "max": scenario["slm"][2],
            },
        },
        "annualised_loss_exposure_cad": {
            "minimum_P10": round(p10, 2),
            "most_likely_mode": round(mode, 2),
            "median_P50": round(p50, 2),
            "maximum_P90": round(p90, 2),
            "tail_P95": round(p95, 2),
            "mean": round(mean, 2),
            "standard_deviation": round(stdev, 2),
        },
        "risk_tier": risk_tier,
        "board_summary": {
            "exposure_range": f"{fmt(p10)} to {fmt(p90)} per year",
            "most_likely_annual_loss": fmt(mode),
            "mean_annual_loss": fmt(mean),
            "risk_tier": risk_tier,
        },
    }


# ---------------------------------------------------------------------------
# Console reporting
# ---------------------------------------------------------------------------


def print_report(result: Dict[str, Any]) -> None:
    ale = result["annualised_loss_exposure_cad"]
    bs = result["board_summary"]

    width = 60
    bar = "=" * width

    print(f"\n{bar}")
    print("  FAIR Quantitative Risk Report")
    print(bar)
    print(f"  Scenario : {result['scenario_name']}")
    if result["scenario_description"]:
        print(f"  Details  : {result['scenario_description']}")
    print(f"  Iterations: {result['simulation']['iterations']:,}")
    print()
    print("  Annualised Loss Exposure (ALE) — CAD")
    print(f"  {'10th Percentile (minimum exposure)':<40} ${ale['minimum_P10']:>15,.0f}")
    print(f"  {'Mode (most likely)':<40} ${ale['most_likely_mode']:>15,.0f}")
    print(f"  {'50th Percentile (median)':<40} ${ale['median_P50']:>15,.0f}")
    print(f"  {'90th Percentile (maximum planning)':<40} ${ale['maximum_P90']:>15,.0f}")
    print(f"  {'95th Percentile (tail risk)':<40} ${ale['tail_P95']:>15,.0f}")
    print(f"  {'Mean':<40} ${ale['mean']:>15,.0f}")
    print(f"  {'Std Dev':<40} ${ale['standard_deviation']:>15,.0f}")
    print()
    print(f"  Board-level range : {bs['exposure_range']}")
    print(f"  Risk Tier         : {bs['risk_tier']}")
    print(bar)
    print()


# ---------------------------------------------------------------------------
# Built-in demo scenario
# ---------------------------------------------------------------------------

DEMO_SCENARIO = {
    "name": "Ransomware Attack on Core Banking Platform",
    "description": (
        "OSFI-reportable ransomware event targeting the bank's core payment "
        "processing infrastructure. Includes regulatory fines under OSFI and "
        "PIPEDA as secondary loss."
    ),
    "tef": {"min": 0.1, "most_likely": 0.5, "max": 2.0},
    "vulnerability": {"min": 0.05, "most_likely": 0.20, "max": 0.40},
    "plm": {"min": 500_000, "most_likely": 3_500_000, "max": 15_000_000},
    "slm": {"min": 100_000, "most_likely": 750_000, "max": 5_000_000},
}


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="FAIR quantitative risk calculator using Monte Carlo simulation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--scenario",
        metavar="FILE",
        help="Path to scenario JSON file.",
    )
    group.add_argument(
        "--demo",
        action="store_true",
        help="Run the built-in demo scenario (ransomware on core banking).",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=100_000,
        help="Number of Monte Carlo iterations (default: 100,000).",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42).",
    )
    parser.add_argument(
        "--output",
        metavar="FILE",
        default=None,
        help="Optional path to write result JSON (e.g. fair_results.json).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.iterations <= 0:
        raise ValueError("--iterations must be greater than zero")

    if args.demo:
        raw = DEMO_SCENARIO
    else:
        path = Path(args.scenario)
        if not path.exists():
            raise FileNotFoundError(f"Scenario file not found: {path}")
        raw = json.loads(path.read_text(encoding="utf-8"))

    scenario = parse_scenario(raw)
    print(f"Running {args.iterations:,} iterations for '{scenario['name']}'...")

    samples = simulate(scenario, iterations=args.iterations, seed=args.seed)
    result = aggregate(samples, scenario)

    print_report(result)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"Full results written to: {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
