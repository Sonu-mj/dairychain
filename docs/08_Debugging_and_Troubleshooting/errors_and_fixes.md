# Errors and Fixes


## Purpose
This file answers which errors were found in DairyChain and how each one was fixed. It is for a reader who needs real errors, not invented ones. Its source for the categories and representative examples is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, sections 4, 5 and 6.

## In this file
- What was supplied
- Debugging categories
- Representative example: Python ingestion failure
- Representative example: incorrect SQL aggregation
- How to add an error

## What was supplied
No error in this file is invented. BUG-001 to BUG-003 are marked fixed because a later notebook cell shows the correction running with output. BUG-004 is now fixed by Source 17: the psql command was run in PowerShell as intended and connected successfully.

## Real errors from the notebook - Source 15
- BUG-001, cell 34: KeyError `'quantity_liters'`. Cause: the code used the American spelling `quantity_liters`, but the CSV column is `quantity_litres`. Fix in cell 36: use `quantity_litres`. shown by cells 38 and 40, which run and show the cost check results.
- BUG-002, cell 63: FileNotFoundError for `/content/dairychain/DairyChain_dataset/data/raw/master/collection_centers.csv`. Cause: the file name used the American spelling `collection_centers.csv`, but the file is `collection_centres.csv`. Fix in cell 65: use `collection_centres.csv`. shown by its output, shape (20, 9).
- BUG-003, cell 87: KeyError `'By-product/residual'`. Cause: the pivot column is named `By-product / residual`, with spaces around the slash. Fix in cells 88-89: use `By-product / residual`. shown by cell 89, which runs the production check for 4,000 batches.
- BUG-004, cell 146: SyntaxError, invalid syntax, from `& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d dairychain`. Cause: a PowerShell command was pasted into a Python code cell. Fix: none in the notebook. The same command, run in Windows PowerShell as intended, connected to database `dairychain` on localhost port 5432 as user `postgres` and returned server version `PostgreSQL 18.6 on x86_64-windows, compiled by msvc-19.44.35229, 64-bit`. Source: [postgresql-connection-and-schemas.png](../13_Project_Evidence/postgresql-connection-and-schemas.png).

Two of these errors are the same kind of mistake twice: a name spelled differently from the actual file or column (BUG-001 and BUG-002). That is a finding about the work, not a new claim: both are visible in the stored outputs.

## The one previously reported error
- Error: a database creation attempt encountered an authentication error. The brief states that PostgreSQL 18.6 was installed, psql was made available through the Windows PATH, and the database creation attempt met an authentication error.
- A current connection test now exists and succeeds: localhost, port 5432, user `postgres`, database `dairychain`, server PostgreSQL 18.6. The earlier authentication error is no longer the current state.

## Debugging categories
The project's Python, PostgreSQL, SQL, and Power BI components can experience different types of problems. These are debugging categories, not a list of confirmed DairyChain incidents. Actual errors should be recorded in the project debugging log.

| Component | Possible issue | What to investigate |
|---|---|---|
| Python ingestion | Source file not found | File path and working directory |
| Python ingestion | Unexpected columns | Source schema and column names |
| Python ingestion | Data type conversion failure | Input values and target data types |
| PostgreSQL | Connection failure | Host, port, database, user, permissions |
| PostgreSQL | Table not found | Schema and table name |
| SQL transformations | Incorrect row counts | Filters, joins, duplicate records |
| SQL transformations | Unexpected aggregates | Grouping level, NULL handling, formulas |
| Power BI | Incorrect KPI | DAX expression and source data |
| Power BI | Slicer not working | Relationship and filter propagation |
| Power BI | Unexpected totals | Aggregation and unit of measurement |

## Representative example: Investigating a Python ingestion failure
The following is a representative debugging example, not a claim about a specific historical DairyChain error.

### Problem
A Python script attempts to read a CSV file, but the file cannot be found.

### Possible causes
- Incorrect file path.
- Different current working directory.
- Incorrect filename.
- File not present in the expected folder.

### Investigation

```python
from pathlib import Path

print("Current working directory:")
print(Path.cwd())

file_path = Path("data/raw/procurement.csv")

print("Resolved file path:")
print(file_path.resolve())

print("File exists:")
print(file_path.exists())
```

### Targeted correction
Use a path that resolves correctly from the script's actual location or configure the project data directory explicitly. Do not change the entire ingestion process just because one input path is incorrect.

### Check
Run the script again and confirm:

- The intended file is found.
- The expected DataFrame is created.
- The expected columns are present.
- The row count is reasonable.

The problem should only be recorded as resolved after these checks have been executed.

## Representative example: Investigating incorrect SQL aggregation
This is another representative technical example, not a claim about a specific historical DairyChain error.

### Problem
An analytical query returns a total that is higher than expected.

### Possible cause
A join may have created duplicate combinations of records before aggregation.

### Investigation
First, examine the row count of the original table:

```sql
SELECT
    COUNT(*) AS original_rows
FROM gold.procurement_quality_summary;
```

Then examine the row count after the join:

```sql
SELECT
    COUNT(*) AS joined_rows
FROM gold.procurement_quality_summary p
JOIN gold.supplier_performance s
    ON p.supplier_id = s.supplier_id;
```

If the joined row count is unexpectedly higher, investigate the relationship and intended level of detail. The second query is a diagnostic example. It does not establish that the join is incorrect; the expected row count depends on the keys and business requirement.

### What needs to be checked
- Is the supplier identifier unique in the supplier summary?
- Does each procurement record match the expected supplier?
- Did the join multiply rows?
- Does the final aggregation represent procurement records or supplier summaries?

### Check
Compare the aggregate before and after the corrected query. Confirm that the resulting metric matches the intended business definition.

## How to add an error
For each new error, add: the error message, the file and line, the input, the cause, the smallest fix, the test that proves the fix, and the date. Do not add an error from memory without its message and its test. Do not mark a bug fixed without the check in [troubleshooting_log.md](troubleshooting_log.md).

## Next step / Related files
- [Debugging methodology](debugging_methodology.md)
- [Troubleshooting log](troubleshooting_log.md)
- [check file](../../VERIFICATION_AND_MISSING_INFO.md)
