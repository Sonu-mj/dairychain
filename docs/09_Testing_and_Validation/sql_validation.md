# SQL Validation

> Status: PENDING EVIDENCE

## Purpose
This file answers how to check a DairyChain SQL query before its output is trusted. It is for an analyst who needs to catch JOIN duplication, wrong grain and bad aggregation before the report is built. Its source for business-metric testing is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 7.5.

## In this file
- Checks for every query
- JOIN and grain
- Aggregation
- Business-metric testing
- Status

## Checks for every query
- The tables and columns named in the query exist in the schema.
- The grain of the result is stated, and the GROUP BY matches that grain.
- Filters do not silently remove rows that should be counted.
- NULLs are handled by a stated rule, not by accident.

## JOIN and grain
A JOIN can duplicate a financial value if the grain of the joined table is finer than the grain of the query. Check the row count before and after each JOIN, and aggregate at the correct grain before joining a summary to a detail table.

## Aggregation
- Check a sum against a second method, such as a Gold total against a Silver total.
- Check a rate against its count and its volume, as in procurement: batch rate 12.84 percent and volume rate 12.76 percent.
- Never add litre and kg quantities in the same sum.

## Business-metric testing
Important metrics should be checked independently. These are reference values from the user-supplied README. A test should be marked as passed only after the relevant SQL calculation has actually been executed and reconciled.

**Procurement batch rejection rate**

2311 / 18000 x 100 = 12.84%

**Milk volume rejection rate**

1,117,247.35 / 8,758,507.64 x 100 = about 12.76%

**Sales revenue**

The recorded project reference is Rs 26,734,294.03.

## Status
No project SQL files were supplied, so no query can be validated here from source. Status: PENDING EVIDENCE. The illustrative queries are in [../07_AI_Assisted_Development/sql_development.md](../07_AI_Assisted_Development/sql_development.md).

## Next step / Related files
- [Data quality checks](data_quality_checks.md)
- [Unit testing](unit_testing.md)
- [Query references](../13_Project_Evidence/query_references.md)
