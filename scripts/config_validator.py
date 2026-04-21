from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_config(config_path: Path, schema_path: Path) -> list[str]:
    config = _load_yaml(config_path)
    schema = _load_yaml(schema_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(config), key=lambda e: list(e.path))

    findings: list[str] = []
    for error in errors:
        location = ".".join([str(part) for part in error.absolute_path]) or "root"
        findings.append(f"{location}: {error.message}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a YAML configuration against the OSFI B-13 policy schema."
    )
    parser.add_argument(
        "--config", required=True, type=Path, help="Path to YAML config file"
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).parent / "schema" / "osfi_b13_policy_schema.yaml",
        help="Path to YAML schema file",
    )
    args = parser.parse_args()

    findings = validate_config(args.config, args.schema)
    if findings:
        print(json.dumps({"valid": False, "findings": findings}, indent=2))
        return 1

    print(json.dumps({"valid": True, "findings": []}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
