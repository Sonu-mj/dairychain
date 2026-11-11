# Implementation Status

> Status: PARTIALLY VERIFIED

## Purpose
This file answers what is implemented in DairyChain, what is partly implemented, and what is not implemented, from the supplied sources only. It is for a reviewer who needs a status table without overclaiming.

## In this file
- Status table
- How to read it
- What would change a status

## Status table
| Area | Status | Evidence |
|---|---|---|
| Source dataset, 10 CSVs, 99,584 records | VERIFIED | Dataset ZIP supplied (Source 28, 2026-11-11): all 10 CSVs SHA256-checked against SHA256SUMS.txt (all OK) and recounted with wc -l, total 99,584 rows, matching the README exactly. Generator 2.1.1-generated, seed 42, generated 2026-11-09. The dataset is SYNTHETIC, not real operational dairy data. Files are in data/raw/; generator, manifest, dictionary, validation report, and checksums in data/; ZIP in docs/13_Project_Evidence/. |
| CSV ingestion, 10 files, 99,584 records | VERIFIED | Notebook (Source 15) reads all 10 files, shapes match the README, total 99,584 rows. No load log supplied. The Bronze load into PostgreSQL is still not evidenced: the CSVs were supplied as files only. |
| Bronze layer in PostgreSQL | PARTIALLY VERIFIED | Table names VERIFIED by Source 17 (10 tables in the psql inventory). Columns and types VERIFIED by Source 18 (82 columns, all text). Row-count total now user-reported (Source 25): 10 tables, 99,584 rows, no screenshot or query output supplied, per-table counts still PENDING EVIDENCE. Notebook has no database code and no load, so no run log supplied. |
| Silver layer, 10 tables | PARTIALLY VERIFIED | Table names VERIFIED by Source 17 (10 tables, identical to the Bronze list). Columns and types VERIFIED by Source 18 (83 columns, typed). Silver `suppliers` has 7 columns against Bronze 9. Row-count total now user-reported (Source 25): 10 tables, 99,584 rows, so cleaning dropped 0 rows from Bronze (99,584 in, 99,584 out); no screenshot or query output supplied, per-table counts still PENDING EVIDENCE. NULL values checked in 8 important columns (Source 25, column list not named, PENDING EVIDENCE); the one missing temperature value (QCT-000250) originates in Bronze and remains NULL in Silver. No cleaning rules supplied. |
| Gold layer, 6 tables | PARTIALLY VERIFIED | Table existence VERIFIED by Source 17 (all 6 in the psql inventory). Column names and types VERIFIED by Source 18 (73 columns, names matching the documented lists exactly). Row counts VERIFIED by Source 19 (18,000, 20, 200, 4,000, 12, 364, total 22,596, live database COUNT(*) output). No Gold SQL supplied. |
| Procurement and quality analysis | VERIFIED | README gives the totals. Notebook adds the rejection-reason breakdown (Low SNF 1,303, Low Fat 513, High Acidity 491, High Temperature 4) and supplier and centre summaries. Model-data totals VERIFIED by Source 23 (rejection reasons match the notebook; date range 2025-11-01 to 2026-10-31). |
| Production analysis | VERIFIED | README gives the output totals. Raw milk input total now VERIFIED from model data (Source 23): 2,600,000.0 L. Yield as a single figure is still not calculable (units do not reconcile for kg batches). |
| Sales analysis | VERIFIED | README gives the revenue and fulfilment totals. Product rows now VERIFIED from model data (Source 23): 12 products with revenue, orders, quantity ordered and fulfilled. Daily rows still PENDING EVIDENCE. |
| Power BI, 4 pages | PARTIALLY VERIFIED | .pbix received and inspected (Source 22): 4 pages named only Page 1 to Page 4 in the file, 63 visuals, 11 model tables VERIFIED from DiagramLayout, 13 measure names referenced by visuals. Model read with pbixray (Source 23): 23 DAX measures (21 with formulas, 2 empty), 1 relationship in the uploaded file (none of the 10 intended dimension relationships exists), Power Query loads only the 6 Gold tables from localhost:5432, KPI values VERIFIED from model data. Dashboard screenshots for all 4 pages supplied (Source 24): rendered pages VERIFIED, card values match the model totals except Page 4, where a date filter (01-04-2026 to 06-10-2026) is active. DISCREPANCY (Source 24b): a Model view screenshot shows many relationship lines that do not exist in the uploaded file - user asked to re-upload the .pbix if he saved the model with those relationships. |
| Profitability analysis | PENDING EVIDENCE | Profit inputs were not supplied. |
| Wastage, returns, inventory, expenses, energy | NOT IMPLEMENTED | Not in the README scope. |
| Tests passed | PENDING EVIDENCE | No formal test files or outputs supplied. Notebook validation checks are Verified execution results (see test_results.md), but they are not a formal test suite. The dataset's own validation report (Source 28, 29 checks, Status PASS) is supplied evidence from the generator, not a test of this pipeline, and was not re-run here. |
| Pipeline run succeeded | PENDING EVIDENCE | No run log supplied. Notebook proves only the CSV read and validation stage. |

## Python implementation - Source 15
The Python implementation was developed in Google Colab, not as separate local Python scripts. One notebook, `dairychain.ipynb`, has been received and inspected (Source 15, 2026-11-11): 148 code cells, 0 markdown cells, imports pandas, os, zipfile, google.colab.files and matplotlib.pyplot only. It reads the 10 CSV files, profiles them, validates them and builds summaries and charts. It has no database library, no PostgreSQL connection, no SQL and no Bronze load. Whether more notebooks exist is unknown; only this one was supplied. Status: PARTIALLY VERIFIED for the Python reading and validation part; the database load part is still Items still requiring evidence. Do not mark Python implementation as missing simply because there is no scripts/ folder. Dependencies: only the package names above are verifiable from the notebook; no version is printed, so no version is claimed and no assumed requirements.txt is created.

## Pipeline limitations - Source 9
The Data Ingestion and Transformation Pipeline document (Source 9) describes the logical processing stages and recorded table inventory. The following information needs to be linked to the actual implementation before making stronger claims. Status: PENDING EVIDENCE.

- Exact source-to-Bronze table mapping.
- Actual Python ingestion code cells in the Colab notebooks: now inspected (Source 15). The database library question is answered: there is none in the notebook, and no Bronze load exists in it.
- Exact Silver transformation rules.
- Exact SQL scripts used to create Gold tables.
- Transaction and rollback behaviour.
- Whether re-running ingestion is idempotent.
- Whether data validation is automated.
- Exact execution order and commands.
- Pipeline execution and failure logs.

These details should be extracted from the real code rather than invented.

## Database scope limits - Source 10
The Database Architecture document (Source 10, section 16) states that the following must not be claimed without additional database evidence. Status: PENDING EVIDENCE / NOT IMPLEMENTED unless proven otherwise.

- Foreign-key constraints on all identifier columns. VERIFIED ABSENT by Source 20: a `pg_constraint` query over bronze, silver, and gold returned 0 rows, so no foreign-key constraint exists on any table.
- Indexes on every join or filter column. VERIFIED ABSENT by Source 21 (`pg_index` returned 0 rows for bronze, silver, and gold). Adding indexes is a future improvement, not current state.
- Partitioning.
- Materialized views.
- Stored procedures.
- Automated incremental loading.
- Automated database backups.
- Replication or high availability.
- Cloud-hosted PostgreSQL deployment.

These may be valuable future improvements, but they are separate from the recorded architecture. The Gold column names are documented (Source 10, sections 5-10) and their types are now VERIFIED by Source 18, and indexes are VERIFIED ABSENT by Source 21 (`pg_index` returned 0 rows for bronze, silver, and gold). Primary keys, foreign keys, unique constraints, and check constraints are VERIFIED ABSENT by Source 20 (`pg_constraint` returned 0 rows for bronze, silver, and gold).

## How to read it
VERIFIED in this table means the README states it and it is copied exactly, at the level of Documented reference values, not Verified execution results, except for the CSV ingestion row, where the notebook's stored outputs also verify the counts. PARTIALLY VERIFIED means part is stated and part still needs source evidence. PENDING EVIDENCE means the source file or output is still needed, that is, Items still requiring evidence. NOT IMPLEMENTED means the README does not describe it as part of DairyChain. No formal test is Verified execution, because no formal test output was supplied. The notebook's own validation checks are Verified execution results from stored outputs, and are listed in test_results.md.

## What would change a status
A status changes only when the named evidence arrives: a file, a query output, a test output, a log or a screenshot. A statement that the work was done, without that evidence, does not change a status.

## Next step / Related files
- [Verification record](verification_record.md)
- [Query references](query_references.md)
- [Screenshots and reports](screenshots_and_reports.md)
