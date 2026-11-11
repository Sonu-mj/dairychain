# Data Validation


## Purpose
This file answers which checks must run on DairyChain data and what each check proves. It is for a reader who needs to trust a Gold number before acting on it.

## In this file
- Checks by layer
- Ingestion validation
- Pipeline validation and reconciliation
- Checks by business rule
- Documented SQL examples (Source 16)
- Prepared check sequence (Source 16)
- What a failed check means

## Checks by layer
- Bronze: row counts per file match the source, no file is missing, types are as expected.
- Silver: no duplicate keys, no missing required values, dates are in range, quantities are not negative unless the business rule allows it.
- Gold: row counts match the README (18,000, 20, 200, 4,000, 12, 364), sums at Gold match sums at Silver, and daily totals add to the period total.

## Ingestion validation
Useful checks from the pipeline document include:

| Check | Purpose |
|---|---|
| File existence | Confirm the intended input is available |
| Row count | Identify the number of records read |
| Column count | Confirm the file structure |
| Column names | Identify schema mismatches |
| Data types | Identify incompatible values |
| Missing values | Identify incomplete records |
| Duplicate records | Identify potential duplication |

## Intentional data-quality scenarios - Source 28

The dataset contains 5 deliberate data-quality faults, so the cleaning and validation work can be shown against known faults. They are documented in the zip data dictionary, and each one was confirmed present in the supplied CSVs on 2026-11-11:

- DQ-01: suppliers SUP-0015, status value `active` in lowercase. The other suppliers use `Active` or `Inactive`.
- DQ-02: suppliers SUP-0042, village with leading and trailing whitespace (` Boriavi `).
- DQ-03: milk_procurement PRC-000500, procurement timestamp in non-ISO format (`10/11/2025 19:19`). This is the same row the notebook (Source 15) cleaned in cells 30-32, converting it to 2025-11-10 19:19:00.
- DQ-04: milk_procurement PRC-001000, total purchase cost inflated by 25 percent (510.03 L at 52.21 gives 26,628.67, but the file holds 33,285.84). This is the same row the notebook (Source 15) flagged as the 1 cost mismatch, 6,657.17, 0.0056 percent of rows.
- DQ-05: quality_tests QCT-000250, temperature_c is NULL. This is the same row the notebook (Source 15) reported as the 1 missing temperature, and Source 25 confirmed it originates in Bronze and stays NULL in Silver.

The validation report supplied with the dataset ([dataset_validation_report.txt](../13_Project_Evidence/dataset_validation_report.txt)) lists 29 checks, including `five_intentional_dq_patterns_present`. That report is supplied evidence from the dataset, recorded as supplied, not re-run as a test by this documentation. See [test_results.md](../09_Testing_and_Validation/test_results.md).

## Pipeline validation and reconciliation
A successful pipeline requires more than checking whether the scripts execute. The output at each stage should be examined.

### Source-to-Bronze validation
Compare: source file row counts, Bronze table row counts, expected columns, and important identifiers.

### Bronze-to-Silver validation
Compare: source and cleaned row counts, missing-value counts, duplicate records, data types, and transformation outcomes.

### Silver-to-Gold validation
Compare the Gold table results against independently calculated SQL aggregates from the underlying Silver data. Examples include: procurement batch counts, accepted and rejected milk quantities, supplier-level procurement totals, collection-centre totals, production output by unit, product revenue, and daily order counts.

### Gold-to-Power BI validation
Compare: total revenue, total orders, procurement volume, rejection percentages, production quantities, and product-level performance. The calculations must use consistent filters and metric definitions.

## Database inspection queries
Source: the user-supplied "DairyChain - Database Architecture" document (Source 10, 2026-11-11, section 14). These queries provide a starting point for inspecting the actual database structure and validating its recorded table inventory. Run them against the real database; the recorded counts below are reference values, not proof the checks passed.

### List the project's tables
```sql
SELECT
    table_schema,
    table_name
FROM information_schema.tables
WHERE table_schema IN (
    'bronze',
    'silver',
    'gold'
)
AND table_type = 'BASE TABLE'
ORDER BY
    table_schema,
    table_name;
```

### Inspect the columns of a Gold table
```sql
SELECT
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns
WHERE table_schema = 'gold'
  AND table_name = 'procurement_quality_summary'
ORDER BY ordinal_position;
```

Repeat the column inspection for each Gold table, and compare the result with the documented columns in [../02_System_Architecture/data_dictionary.md](../02_System_Architecture/data_dictionary.md). A column in the database that is not in the dictionary, or a dictionary column that is not in the database, is a mismatch to record, not to ignore.

### Check the number of records in all six Gold tables
```sql
SELECT
    'procurement_quality_summary' AS table_name,
    COUNT(*) AS total_rows
FROM gold.procurement_quality_summary

UNION ALL

SELECT
    'supplier_performance',
    COUNT(*)
FROM gold.supplier_performance

UNION ALL

SELECT
    'collection_centre_performance',
    COUNT(*)
FROM gold.collection_centre_performance

UNION ALL

SELECT
    'production_performance',
    COUNT(*)
FROM gold.production_performance

UNION ALL

SELECT
    'sales_product_performance',
    COUNT(*)
FROM gold.sales_product_performance

UNION ALL

SELECT
    'sales_daily_summary',
    COUNT(*)
FROM gold.sales_daily_summary;
```

Recorded reference counts to compare against: procurement_quality_summary 18,000; supplier_performance 200; collection_centre_performance 20; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364.


## Documented SQL examples - Source 16
Source: the PDF "DairyChain PostgreSQL Codes and Outputs" (Source 16, 2026-11-11, sections 3-6). Do not present any of them as executed Gold SQL or shown DDL. The catalogue queries, the Gold row-count check, and the join-cardinality diagnostic are already in this file (from Source 10) or in [../08_Debugging_and_Troubleshooting/errors_and_fixes.md](../08_Debugging_and_Troubleshooting/errors_and_fixes.md), so they are not repeated here; the PDF repeats them, and the one copy is the reference.

### Create the three processing schemas
```sql
CREATE SCHEMA IF NOT EXISTS bronze;
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
```

### Example supplier table definition - illustrative only
```sql
CREATE TABLE silver.suppliers (
    supplier_id TEXT PRIMARY KEY,
    supplier_name TEXT NOT NULL,
    district TEXT,
    state TEXT,
    registration_date DATE,
    status TEXT
);
```
### Inspect sample rows
```sql
SELECT *
FROM bronze.milk_procurement
LIMIT 10;
```
The Bronze table name is now from Source 17, and its columns are from Source 18 (10 columns, all text).

### Count rows in a table
```sql
SELECT COUNT(*)
FROM bronze.milk_procurement;
```
Do not insert the Colab source count of 18,000 as the database result unless this query is actually run against the corresponding table.

### Aggregate procurement by supplier
```sql
SELECT
    supplier_id,
    SUM(quantity_litres) AS litres_received
FROM silver.milk_procurement
GROUP BY supplier_id;
```

### Join procurement to supplier master
```sql
SELECT
    p.procurement_id,
    s.supplier_name,
    p.quantity_litres
FROM silver.milk_procurement AS p
JOIN silver.suppliers AS s
    ON p.supplier_id = s.supplier_id;
```

### Convert a text value to a numeric type
```sql
SELECT
    quantity_litres::NUMERIC(12,2) AS quantity_litres
FROM bronze.milk_procurement;
```
This SELECT casts values for its result; it does not alter the stored table definition.

### Trim text values
```sql
SELECT
    TRIM(acceptance_status) AS acceptance_status
FROM bronze.milk_procurement;
```
The source column name in the inspected CSV is `acceptance_status` for procurement; quality-test records use `quality_status`.

### Flag purchase-cost mismatches
```sql
SELECT
    *,
    CASE
        WHEN total_purchase_cost IS NULL THEN 'MISSING_COST'
        WHEN ABS(
            total_purchase_cost -
            quantity_litres * purchase_rate_per_litre
        ) > 0.01 THEN 'COST_MISMATCH'
        ELSE 'OK'
    END AS cost_validation_status
FROM bronze.milk_procurement;
```
The later Colab inspection reported one cost mismatch, but that is a Pandas result, not output from this SQL query.

### Procurement batch rejection rate
```sql
SELECT
    COUNT(*) AS total_batches,
    COUNT(*) FILTER (
        WHERE quality_status = 'Rejected'
    ) AS rejected_batches,
    COUNT(*) FILTER (
        WHERE quality_status = 'Accepted'
    ) AS accepted_batches,
    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE quality_status = 'Rejected'
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS rejection_rate_percentage
FROM gold.procurement_quality_summary;
```
A Colab/Pandas reference calculation recorded 18,000 batches, 2,311 rejected, 15,689 accepted, and 12.84 percent rejection. The `quality_status` column is consistent with the documented Gold column list in [../02_System_Architecture/data_dictionary.md](../02_System_Architecture/data_dictionary.md).

### Assumptions in these examples
- The examples use `bronze.milk_procurement` and `silver.milk_procurement` as table names. Source 17: the psql table inventory confirms both `bronze.milk_procurement` and `silver.milk_procurement` exist, so `milk_procurement` is the real name, not the illustrative `bronze.procurement` from Source 9.
- The cost-validation CASE uses `total_purchase_cost`, `quantity_litres`, and `purchase_rate_per_litre`. Those match documented Gold columns. Source 18: all three columns exist in `bronze.milk_procurement`, but there they are all data_type `text`, so the numeric comparison in the CASE needs a cast to work as written; the type-casting example in this file (`quantity_litres::NUMERIC(12,2)`) is the relevant pattern.
- The rejection-rate query uses `quality_status` on `gold.procurement_quality_summary`, which is consistent with the documented Gold column list.

## Prepared check sequence - Source 16, run - Sources 17, 18, 19, 20, 21 and 25
Source: the PDF "DairyChain PostgreSQL Codes and Outputs" (Source 16, 2026-11-11, section 9). No run date is visible in the screenshots or in the pasted output, so no run date is claimed; all are recorded as user-supplied 2026-11-11.

### Step 1 - Connection (Source 17)
Command run in Windows PowerShell: `& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -h localhost -p 5432 -U postgres -d dairychain`. Password prompt answered, psql banner `psql (18.6)` shown, prompt `dairychain=#` reached. Connection SUCCEEDS. Source: [postgresql-connection-and-schemas.png](../13_Project_Evidence/postgresql-connection-and-schemas.png).

### Step 2 - Database, user, and server version (Source 17)
Query run: `SELECT current_database AS database_name, current_user AS connected_user, inet_server_addr AS server_address, inet_server_port AS server_port, version AS server_version;` Result, 1 row: `dairychain | postgres | ::1 | 5432 | PostgreSQL 18.6 on x86_64-windows, compiled by msvc-19.44.35229, 64-bit`. Server version is now shown as 18.6, not just the client version. Note the code-page warning in the screenshot: console code page 437 differs from Windows code page 1252, 8-bit characters might not work correctly. That warning is recorded as shown; it did not stop the connection or the queries.

### Step 3 - Schemas and table inventory (Source 17)
Schema query run (information_schema.schemata, excluding information_schema and pg_catalog): 5 rows, `bronze, gold, pg_toast, public, silver`. Table inventory query run (information_schema.tables, same exclusions, table_type = 'BASE TABLE'): 26 rows, bronze 10, gold 6, silver 10, listed in [data_dictionary.md](../02_System_Architecture/data_dictionary.md). Bronze and silver lists are identical. Source: [postgresql-table-inventory.png](../13_Project_Evidence/postgresql-table-inventory.png).

### Step 4 - Gold row counts (Source 19)
The Gold row-count UNION ALL query from the "Database inspection queries" section above was run and the output supplied as a user-supplied screenshot (image-7.png, 2026-11-11), copied into the docs as [postgresql-gold-row-counts.png](../13_Project_Evidence/postgresql-gold-row-counts.png). Result, 6 rows: procurement_quality_summary 18000, collection_centre_performance 20, supplier_performance 200, production_performance 4000, sales_product_performance 12, sales_daily_summary 364. Total 22596. All 6 counts match the exactly. No run date is visible in the screenshot, so no run date is claimed. Bronze and Silver row counts in the database are now DONE by Source 25 (given by the user totals: Bronze 99,584, Silver 99,584; ).

### Step 5 - Column names and types per table (Source 18)
The `information_schema.columns` output was supplied as pasted text (238 rows: Bronze 82, Gold 73, Silver 83), recomputed and saved verbatim as [information_schema_columns_238_rows.txt](../13_Project_Evidence/information_schema_columns_238_rows.txt). Column names, data types, precision, scale, and nullability are now shown for all 26 tables: see [data_dictionary.md](../02_System_Architecture/data_dictionary.md). Key findings: Bronze is all `text`; Silver is typed; Silver `suppliers` has 7 columns against Bronze 9 (`status` and `contact_reference` are not in Silver); all 238 rows are nullable YES with no default. This output does NOT show primary keys, foreign keys, unique constraints, or indexes, so those needed pg_constraint / pg_index queries. Constraints are now resolved by Source 20 (Step 6 below: 0 rows, absent). Indexes are now resolved by Source 21 (Step 7 below: 0 rows, absent).

### Step 6 - Constraints (pg_constraint) (Source 20)
Query run in psql (user-supplied screenshot image-8.png, 2026-11-11), copied into the docs as [postgresql-constraints-zero-rows.png](../13_Project_Evidence/postgresql-constraints-zero-rows.png):

```sql
SELECT
    n.nspname AS schema_name,
    c.relname AS table_name,
    con.conname AS constraint_name,
    CASE con.contype
        WHEN 'p' THEN 'PRIMARY KEY'
        WHEN 'f' THEN 'FOREIGN KEY'
        WHEN 'u' THEN 'UNIQUE'
        WHEN 'c' THEN 'CHECK'
        ELSE con.contype::text
    END AS constraint_type,
    pg_get_constraintdef(con.oid) AS definition
FROM pg_constraint con
JOIN pg_class c
  ON con.conrelid = c.oid
JOIN pg_namespace n
  ON c.relnamespace = n.oid
WHERE n.nspname IN ('bronze', 'silver', 'gold')
ORDER BY n.nspname, c.relname, constraint_type;
```

Result: `(0 rows)`. No primary key, foreign key, unique, or check constraint exists on any table in bronze, silver, or gold. This is consistent with Source 18, where all 238 columns are nullable YES with no column default. What it does NOT prove: indexes. `pg_constraint` does not cover indexes, so indexes are checked separately in Step 7 below (Source 21: 0 rows, absent). No run date is visible in the screenshot, so no run date is claimed; recorded as user-supplied 2026-11-11.

### Step 7 - Indexes (pg_index) (Source 21)

Query run in psql (user-supplied screenshot image-9.png, 2026-11-11), copied into the docs as [postgresql-indexes-zero-rows.png](../13_Project_Evidence/postgresql-indexes-zero-rows.png):

```sql
SELECT
    n.nspname AS schema_name,
    t.relname AS table_name,
    i.relname AS index_name,
    ix.indisprimary AS is_primary,
    ix.indisunique AS is_unique,
    ix.indisvalid AS is_valid,
    pg_get_indexdef(ix.indexrelid) AS index_definition
FROM pg_index ix
JOIN pg_class t
  ON ix.indrelid = t.oid
JOIN pg_namespace n
  ON t.relnamespace = n.oid
JOIN pg_class i
  ON ix.indexrelid = i.oid
WHERE n.nspname IN ('bronze', 'silver', 'gold')
ORDER BY n.nspname, t.relname, i.relname;
```

Result: `(0 rows)`. No index of any kind exists on any table in bronze, silver, or gold: no primary-key index, no unique index, and no other index. Together with Source 20 (0 constraints), this closes the keys and indexes question completely: no primary key, no foreign key, no unique constraint, no check constraint, and no index exists on any of the 26 tables. This is consistent with Source 18, where all 238 columns are nullable YES with no column default. The prepared check sequence for schema, columns, counts, constraints, and indexes is now fully DONE, including the Bronze and Silver row-count totals by Source 25 (given by the user, see Step 8 below). No run date is visible in the screenshot, so no run date is claimed; recorded as user-supplied 2026-11-11.

### Connection command template
Adapt username, host, and port to the real local configuration. The actual command run is recorded in Step 1 above (full psql.exe path, localhost, port 5432, user postgres, database dairychain).
```powershell
psql -h localhost -p 5432 -U postgres -d dairychain
```
Output captured (Source 17): the psql banner `psql (18.6)` and prompt `dairychain=#` are visible in the screenshot.

### Confirm database, user, and server version
```sql
SELECT
    current_database() AS database_name,
    current_user AS connected_user,
    version() AS server_version;
```
Output captured (Source 17): one row, `dairychain | postgres | ::1 | 5432 | PostgreSQL 18.6 on x86_64-windows, compiled by msvc-19.44.35229, 64-bit`. Server version shown as 18.6.

### Confirm required schemas
```sql
SELECT schema_name
FROM information_schema.schemata
WHERE schema_name IN ('bronze', 'silver', 'gold')
ORDER BY schema_name;
```
Output captured (Source 17): 5 rows, `bronze, gold, pg_toast, public, silver`.

### Confirm actual Gold tables
```sql
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_schema = 'gold'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```
Output captured (Source 17): the full inventory returned 26 rows, including all 6 Gold tables. The information_schema.columns query is DONE by Source 18 (238 rows, see Step 5 above). The Gold row-count query is DONE by Source 19 (6 rows: 18,000, 20, 200, 4,000, 12, 364, total 22,596, see Step 4 above). Bronze and Silver row counts in the database are now DONE by Source 25 (given by the user totals, see Step 8 below).

### Step 8 - Bronze and Silver row counts (Source 25, user-reported)

The user reported the database check as complete for row counts, 2026-11-11, in his own words: "Database check is now complete for row counts: Bronze: 10 tables, 99,584 rows. Silver: 10 tables, 99,584 rows. Bronze 99,584 and Silver 99,584 are recorded as given by the user database totals. Silver kept all 99,584 rows, so cleaning dropped 0 rows at the Bronze-to-Silver step (99,584 in, 99,584 out). Gold 22,596 was already shown by screenshot in Source 19 and is now also confirmed by this user report. Silver's 83 columns were already shown by the Source 18 column dump and this report is a second confirmation, not new evidence. The one missing temperature value (QCT-000250, already known from the notebook in Source 15) was confirmed to originate in Bronze and remain NULL in Silver.

## Checks by business rule
- Procurement: accepted plus rejected batches equals 18,000. Check: 15,689 plus 2,311 equals 18,000.
- Check: 11,166 plus 2,227 plus 607 equals 14,000.
- Production: litre and kg outputs are kept separate. Production batches split as 3,001 litre-based batches and 999 kg-based batches, total 4,000. A check that adds them is a failed check.
- Units: every quantity carries its unit, and no calculation mixes units.

## What a failed check means
A failed check stops the pipeline from being reported as correct. It does not mean the data is deleted. It means the cause is found, fixed at the right layer, and the check is run again. The test record is in [../09_Testing_and_Validation/data_quality_checks.md](../09_Testing_and_Validation/data_quality_checks.md).

## Next step / Related files
- [Data cleaning](data_cleaning.md)
- [Data quality checks](../09_Testing_and_Validation/data_quality_checks.md)
- [SQL validation](../09_Testing_and_Validation/sql_validation.md)
