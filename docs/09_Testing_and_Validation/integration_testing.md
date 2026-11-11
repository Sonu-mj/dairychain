# Integration Testing

> Status: PENDING EVIDENCE

## Purpose
This file answers how to test DairyChain end to end, from CSV to Gold to Power BI. It is for a developer who needs to prove the layers join up, not only that each layer runs alone. Its sources are the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, sections 7.2, 7.3, 7.4 and 8.

## In this file
- What to test
- Bronze layer testing
- Silver layer testing
- Gold layer testing
- Reconciliation testing
- Counts to reconcile
- Status

## What to test
- CSV to Bronze: every file is loaded, and no file is missed or loaded twice.
- Bronze to Silver: cleaning changes are logged, and the cleaned row count is explained.
- Silver to Gold: each Gold table is built from Silver at the stated grain, and its count matches the README.
- Gold to Power BI: each Gold number appears correctly in the report, with the right filter and the right measure.

## Bronze layer testing
The Bronze layer should preserve the ingested source records at the intended ingestion level.

Checks should include:

- Whether the required source tables exist.
- Whether the expected columns are present.
- Whether source records were loaded.
- Whether the loaded record counts match the source.
- Whether data types and parsing have been handled consistently.

Recorded project reference: The Bronze layer contains 10 source tables representing 99,584 rows in total. This is a documented project reference count, not proof that every ingestion test has passed.

## Silver layer testing
The Silver layer contains 10 cleaned tables.

Checks should include:

- Expected columns and data types.
- Missing-value handling.
- Duplicate-record handling.
- Identifier consistency.
- Valid dates and numeric values.
- Business-rule compliance.
- Row-count differences from Bronze, where records are legitimately filtered or transformed.

A difference in row count is not automatically a failure. It must be explained by the transformation rules.

## Gold layer testing
The Gold layer contains six analytical tables. The documented table inventory is:

| Gold table | Recorded rows | Expected level of detail |
|---|---:|---|
| procurement_quality_summary | 18,000 | One row per procurement batch |
| collection_centre_performance | 20 | One row per collection centre |
| supplier_performance | 200 | One row per supplier |
| production_performance | 4,000 | One row per production batch |
| sales_product_performance | 12 | One row per product |
| sales_daily_summary | 364 | One row per date |

These counts can be used as reference checks when executing the project against the corresponding database. Example:

```sql
SELECT COUNT(*) AS total_rows
FROM gold.procurement_quality_summary;
```

Repeat the count check for each Gold table and compare the results with the documented inventory.

## Reconciliation testing
Reconciliation checks whether related data processing stages produce consistent results.

### Bronze to source
Compare source-file record counts with the corresponding Bronze table counts.

### Bronze to Silver
Investigate records removed, modified, or retained during cleaning. Document the transformation rules responsible for expected differences.

### Silver to Gold
Recalculate important aggregates from Silver and compare them with the corresponding Gold tables.

### Gold to Power BI
Compare Power BI KPIs and chart values with SQL queries on the underlying Gold tables.

Reconciliation should consider:

- Row counts.
- Unique identifiers.
- Total milk volume.
- Accepted and rejected quantities.
- Production output by unit.
- Total revenue.
- Order counts.

The comparison must use the same filters, date ranges, and business definitions on both sides.

## Counts to reconcile
- Source: 99,584 records.
- Gold: procurement_quality_summary 18,000, collection_centre_performance 20, supplier_performance 200, production_performance 4,000, sales_product_performance 12, sales_daily_summary 364.
- Sales: delivered plus partially delivered plus cancelled equals 14,000.
- Procurement: accepted plus rejected equals 18,000.

## Status
No integration test output was supplied, so no integration test is reported as passed. Status: PENDING EVIDENCE.

## Next step / Related files
- [SQL validation](sql_validation.md)
- [Data quality checks](data_quality_checks.md)
- [Pipeline execution](../03_Data_Engineering/pipeline_execution.md)
