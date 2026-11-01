#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

REQUIRED_FIELDS = {"vehicle_id", "vehicle_type", "status"}
VALID_STATUSES = {"operational", "maintenance", "out_of_service"}
def validate_manifest(path):
    errors = []
    seen_ids = set()

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not REQUIRED_FIELDS.issubset(reader.fieldnames):
            return ["Missing required columns: " + ", ".join(sorted(REQUIRED_FIELDS))]

        for line, row in enumerate(reader, start=2):
            if (row.get("status") or "").strip() not in VALID_STATUSES:
                errors.append(f"Line {line}: invalid vehicle status")

            vehicle_id = (row.get("vehicle_id") or "").strip()

            if not vehicle_id:
                errors.append(f"Line {line}: missing vehicle ID")
            elif vehicle_id in seen_ids:
                errors.append(f"Line {line}: duplicate vehicle ID {vehicle_id}")
            else:
                seen_ids.add(vehicle_id)

            for field in REQUIRED_FIELDS:
                if not (row.get(field) or "").strip():
                    errors.append(f"Line {line}: missing {field}")

    return errors

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fleet_validator.py <manifest.csv>")
        sys.exit(2)

    path = Path(sys.argv[1])

    if not path.is_file():
        print(f"Error: file not found: {path}")
        sys.exit(2)

    errors = validate_manifest(path)

    if errors:
        print(f"Validation failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("Manifest validation successful.")

if __name__ == "__main__":
    main()
