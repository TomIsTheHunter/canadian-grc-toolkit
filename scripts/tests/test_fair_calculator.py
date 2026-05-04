"""Tests for FAIR scenario parsing, simulation, and CLI output behavior."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import pytest

from scripts.fair_calculator import aggregate, main, parse_scenario, simulate


def test_parse_scenario_rejects_invalid_vulnerability_range() -> None:
    with pytest.raises(ValueError):
        parse_scenario(
            {
                "name": "Invalid",
                "tef": {"min": 1, "most_likely": 2, "max": 3},
                "vulnerability": {"min": 0.1, "most_likely": 0.2, "max": 1.2},
                "plm": {"min": 1000, "most_likely": 2000, "max": 3000},
            }
        )


def test_simulate_and_aggregate_produces_expected_shape() -> None:
    scenario = parse_scenario(
        {
            "name": "Credential Stuffing",
            "description": "Sample scenario",
            "tef": {"min": 1, "most_likely": 2, "max": 4},
            "vulnerability": {"min": 0.05, "most_likely": 0.15, "max": 0.30},
            "plm": {"min": 50000, "most_likely": 150000, "max": 500000},
            "slm": {"min": 10000, "most_likely": 25000, "max": 100000},
        }
    )

    samples = simulate(scenario, iterations=250, seed=7)
    result = aggregate(samples, scenario)

    assert len(samples) == 250
    assert result["simulation"]["iterations"] == 250
    assert (
        result["annualised_loss_exposure_cad"]["maximum_P90"]
        >= result["annualised_loss_exposure_cad"]["minimum_P10"]
    )
    assert result["risk_tier"] in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}


def test_fair_cli_output_parent_directory_is_created(tmp_path: Path) -> None:
    scenario_path = tmp_path / "scenario.json"
    scenario_path.write_text(
        json.dumps(
            {
                "name": "Demo",
                "tef": {"min": 1, "most_likely": 1, "max": 2},
                "vulnerability": {"min": 0.1, "most_likely": 0.2, "max": 0.3},
                "plm": {"min": 1000, "most_likely": 2000, "max": 4000},
            }
        ),
        encoding="utf-8",
    )

    output_path = tmp_path / "nested" / "fair_results.json"

    old_argv = sys.argv
    sys.argv = [
        "fair_calculator.py",
        "--scenario",
        str(scenario_path),
        "--iterations",
        "10",
        "--output",
        str(output_path),
    ]
    try:
        assert main() == 0
    finally:
        sys.argv = old_argv

    assert output_path.exists()
