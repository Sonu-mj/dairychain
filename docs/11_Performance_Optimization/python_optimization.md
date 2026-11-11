# Python Optimization

> Status: PENDING EVIDENCE

## Purpose
This file answers how to keep DairyChain Python fast enough for 99,584 records without adding complexity that is not needed. It is for a developer who needs practical speed, not a new framework.

## In this file
- Rules
- When Pandas is right
- When Parquet helps
- What not to claim

## Rules
- Read only the columns needed, and only the rows needed for the task.
- Use vectorised Pandas operations instead of a row-by-row loop where the operation allows it.
- Validate in one pass where possible, and log the rows that fail instead of stopping on the first failure.
- Keep the unit with every quantity, so a fast result is not a wrong result.

## When Pandas is right
Pandas is appropriate for ingestion, cleaning and transformation at the scale in this project, 99,584 source records. It is not a database, and it is not a substitute for SQL aggregation at Gold grain.

## When Parquet helps
Parquet is a columnar format that can help analytical processing and file size, because a query can read only the columns it needs. The brief names Parquet as part of the project context. Its actual use must be checked against the code and the outputs, which were not supplied.

## What not to claim
No Python timing or measured improvement was supplied, so none is claimed.

## Next step / Related files
- Query optimization](query_optimization.md)
- Pipeline performance](pipeline_performance.md)
- Data ingestion](../03_Data_Engineering/data_ingestion.md)
