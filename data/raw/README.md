# Raw data

This folder holds the 10 source CSV files the project was built from, 99,584 records in total. The files are present in this repo.

## The dataset is synthetic

This is a synthetic dataset, not real operational dairy data. It was made for this project, covering the period 2025-11-01 to 2026-10-31. Names, prices, rates, yields, and volumes are generated values. Do not treat them as real-world operating benchmarks. The modelling assumptions are listed in `data/README.md` and in `docs/00_Project_Overview/`.

## Files and row counts

Row counts were shown by the main agent on 2026-11-11 by recounting the CSVs after copying, and by SHA256 checksum against `data/SHA256SUMS.txt` (all 10 files OK). Total: 99,584 rows.

- Suppliers.csv - 200 rows
- Collection_centres.csv - 20 rows
- Products.csv - 12 rows
- Milk_procurement.csv - 18,000 rows
- Quality_tests.csv - 18,000 rows
- Production_batches.csv - 4,000 rows
- Production_inputs.csv - 9,352 rows
- Production_outputs.csv - 8,000 rows
- Sales_orders.csv - 14,000 rows
- Sales_order_lines.csv - 28,000 rows

## Intentional data-quality scenarios

Five data-quality problems were deliberately built into the data, so the cleaning and validation work can be shown against known faults. They are documented in the validation report at `data/validation_report.txt`:

- DQ-01: suppliers SUP-0015, lowercase status value (`active`).
- DQ-02: suppliers SUP-0042, leading and trailing whitespace in village (` Boriavi `).
- DQ-03: milk_procurement PRC-000500, non-ISO timestamp (`10/11/2025 19:19`).
- DQ-04: milk_procurement PRC-001000, total purchase cost inflated by 25 percent.
- DQ-05: quality_tests QCT-000250, NULL temperature_c.

## Supporting files

- `data/validation_report.txt` - 29 checks.
- `data/DATA_DICTIONARY.md` - column meanings for all 10 files.
- `data/SHA256SUMS.txt` - checksums for all 10 files.
- `docs/13_Project_Evidence/DairyChain_dataset_full.zip` - the original dataset ZIP, kept as evidence.

## What this does NOT prove

These CSVs were supplied as files. The database already exists and its tables were shown separately (see `docs/13_Project_Evidence/`).
