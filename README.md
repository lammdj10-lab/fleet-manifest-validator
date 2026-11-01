# Fleet Manifest Validator

A Python command-line tool for validating fleet vehicle manifests stored as CSV files.

## Requirements

- Python 3
- No external dependencies

## Manifest Format

The CSV must contain these columns:

- `vehicle_id`
- `vehicle_type`
- `status`

Accepted vehicle statuses:

- `operational`
- `maintenance`
- `out_of_service`

## Usage

Run the validator:

```bash
python3 fleet_validator.py manifests/example.csv
The validator checks for:
- Missing required columns
- Missing vehicle IDs or fields
- Duplicate vehicle IDs
- Invalid vehicle status values

A successful manifest returns a validation confirmation. Invalid manifests return specific errors and a nonzero exit code.
