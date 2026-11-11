# What the project holds

## Purpose
This file says what is in the DairyChain project, from the supplied sources only. It is for a reader who wants the contents in one place: the dataset, the Python, the database layers, the analytics, the Power BI model, and the tests and debugging.

## In this file
- Dataset
- Python
- Database layers
- Analytics
- Power BI
- Tests and debugging

## Dataset
The dataset ZIP (Source 28, 2026-11-11) holds 10 CSV files, 99,584 records: suppliers 200, collection_centres 20, products 12, milk_procurement 18,000, quality_tests 18,000, production_batches 4,000, production_inputs 9,352, production_outputs 8,000, sales_orders 14,000, sales_order_lines 28,000. All SHA256 checksums match SHA256SUMS.txt, and the headers match the documented Bronze columns exactly (82 columns, 0 differences). The dataset is synthetic, made for this project, covering 2025-11-01 to 2026-10-31. The validation report lists 29 checks, all PASS. Five intentional data-quality scenarios are documented in the manifest: DQ-01 suppliers SUP-0015 lowercase status, DQ-02 suppliers SUP-0042 whitespace in village, DQ-03 milk_procurement PRC-000500 non-ISO timestamp, DQ-04 milk_procurement PRC-001000 total purchase cost inflated by 25 percent, DQ-05 quality_tests QCT-000250 NULL temperature_c. The CSVs are in `data/raw/`; the manifest, dictionary, validation report, and checksums are in `data/`; the ZIP is in `docs/13_Project_Evidence/`.

## Python
The Python implementation was developed in Google Colab, not as separate local Python scripts (Source 14). One notebook, `dairychain.ipynb`, was received and inspected (Source 15, 2026-11-11): 148 code cells, 0 markdown cells, imports pandas, os, zipfile, google.colab.files, and matplotlib.pyplot only. It reads the 10 CSV files, profiles them, validates them, and builds summaries and charts. Its stored outputs show 0 duplicates in all 10 datasets, 1 missing temperature (QCT-000250), 607 missing delivery dates all Cancelled, 1 cost mismatch (PRC-001000, 6,657.17), 0 procurement-quality status mismatches in 18,000, 0 rejection-rule inconsistencies, and 0 line-total mismatches. The notebook is in `scripts/`.

## Database layers
The database is `dairychain` on PostgreSQL 18.6 (Sources 8, 17). The connection command `psql -h localhost -p 5432 -U postgres -d dairychain` reaches the `dairychain=#` prompt, and the server version row reads PostgreSQL 18.6 on x86_64-windows, compiled by msvc-19.44.35229, 64-bit (Source 17). Schemas: bronze, gold, pg_toast, public, silver. Table inventory, 26 rows: bronze 10 and silver 10 with identical names, gold 6 (Source 17). Column dump, 238 rows: Bronze 82 columns, all `text`; Silver 83 columns, typed; Gold 73 columns, typed (Source 18). Gold column names match the Source 10 documented lists exactly. Silver `suppliers` has 7 columns against Bronze 9; `status` and `contact_reference` are not in silver.suppliers. All 238 columns are nullable YES, with no column default. Gold row counts from a UNION ALL COUNT(*) query: procurement_quality_summary 18,000, collection_centre_performance 20, supplier_performance 200, production_performance 4,000, sales_product_performance 12, sales_daily_summary 364, total 22,596 (Source 19). Bronze and Silver row totals from Source 25: 10 tables each, 99,584 rows each, so cleaning dropped 0 rows from Bronze (99,584 in, 99,584 out). A pg_constraint query over bronze, silver, and gold returns 0 rows: no primary key, foreign key, unique, or check constraint on any of the 26 tables (Source 20). A pg_index query returns 0 rows: no indexes on any table (Source 21).

## Analytics
The 20 business questions are defined in Source 13: PR-01 to PR-05, QL-01 to QL-05, PRD-01 to PRD-04, S-01 to S-06. Answers from the model data (Source 23) are recorded for PR-01, PR-04, PR-05, QL-01, QL-04, PRD-01, PRD-02, PRD-03, PRD-04, S-01, S-02, S-03, S-04, and S-05. The district ranking for PR-03 comes from the Page 2 dashboard screenshot (Source 24). The trend shapes for S-06 come from the Page 1 and Page 4 dashboard screenshots (Source 24). The procurement totals: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent. Rejection reasons: Low SNF 1,303, Low Fat 513, High Acidity 491, High Temperature 4. Production totals: 4,000 batches (3,001 litre-based, 999 kg-based), raw milk 2,600,000.0 L, finished 1,484,135.25 L and 266,416.65 kg, byproduct 466,514.75 L and 402,413.85 kg, average production duration 135.03 minutes. Sales totals: revenue Rs 26,734,294.03, 14,000 orders, quantity ordered 181,804, quantity fulfilled 161,036.41, delivered 11,166, partially delivered 2,227, cancelled 607. Product revenue ranking from the model data: Pure Cow & Buffalo Ghee 5,986,642.50, Fresh Malai Paneer 5,531,071.00, Pasteurised Table Butter 5,156,439.08, Fresh Dairy Cream 2,354,907.50, Elaichi Flavoured Milk 1,799,512.50, Probiotic Lassi 1,123,028.00, Classic Set Curd 1,091,328.75, Full Cream Milk 916,687.20, Standardised Milk 851,256.00, Toned Milk 796,826.70, Double Toned Milk 694,144.80, Spiced Masala Buttermilk 432,450.00.

## Power BI
The .pbix file (Source 22) holds 4 pages named Page 1 to Page 4, 63 visuals (17, 14, 14, 18), and 11 model tables in the DiagramLayout (6 Gold tables plus 5 dimensions). The model read with pbixray (Source 23) holds 23 DAX measures (21 with formulas, 2 empty placeholders), calculated columns procurement_date and production_date, dimensions as DAX calculated tables, and Power Query loading only the 6 Gold tables from PostgreSQL localhost:5432, database dairychain. One relationship exists in the uploaded file: gold procurement_quality_summary[supplier_id] to gold supplier_performance[supplier_id]. Dashboard screenshots for all 4 pages (Source 24) are in `docs/13_Project_Evidence/`: Page 1 Executive Overview, Page 2 Procurement & Quality Analysis, Page 3 Production Performance Analysis, Page 4 Sales Analysis. Page 4 was captured with a date filter active, 01-04-2026 to 06-10-2026, so its cards are filtered values. A Model view screenshot (Source 24b) shows about 10 relationship lines between the 11 model tables.

## Tests and debugging
The notebook validation checks are listed in `docs/09_Testing_and_Validation/test_results.md`, with cell numbers and stored-output results (Source 15). The dataset validation report (Source 28) lists 29 checks, all PASS: 10 primary-key uniqueness checks, 10 foreign-key checks, and 9 business-rule checks. Four real errors from the notebook work are logged as BUG-001 to BUG-004 in `docs/08_Debugging_and_Troubleshooting/troubleshooting_log.md`, all fixed: BUG-001 KeyError `quantity_liters` (fixed in cell 36), BUG-002 FileNotFoundError `collection_centers.csv` (fixed in cell 65), BUG-003 KeyError `By-product/residual` (fixed in cells 88-89), BUG-004 a PowerShell psql command pasted as a Python cell (fixed by running the command in PowerShell, Source 17).

## Next step / Related files
- [Source list](../../VERIFICATION_AND_MISSING_INFO.md)
- [Source record](verification_record.md)
- [Test results](../09_Testing_and_Validation/test_results.md)
- [Debugging log](../08_Debugging_and_Troubleshooting/troubleshooting_log.md)
- [Screenshots and reports](screenshots_and_reports.md)
