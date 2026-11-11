# Query Optimization


## Purpose
This file answers how to make DairyChain SQL fast without changing what it returns. It is for an analyst who needs a query that is both correct and quick enough to run in a report.

## In this file
- Rules
- Indexes
- What not to claim

## Rules
- Select only the columns the report needs.
- Aggregate at the correct grain before joining, so a JOIN does not duplicate values.
- Filter early, so the query works on fewer rows.
- Avoid repeated database queries for the same result. Cache a Gold result instead of re-running the same aggregation for every visual.

## Indexes
Indexes may improve access patterns, such as looking up a batch, a supplier, a product or a day. Source 21 shown that no index exists on any table in bronze, silver, or gold (a `pg_index` query returned 0 rows, user-supplied screenshot 2026-11-11), so indexes are a future improvement, not current state. The right index depends on the actual queries and the actual schema. Do not list an index as implemented until its DDL can be shown.

## What not to claim
No performance benchmark, timing or measured improvement was supplied, so none is claimed. A faster query is a claim that needs a before-and-after timing, not a feeling.

## Next step / Related files
- Python optimization](python_optimization.md)
- Pipeline performance](pipeline_performance.md)
- SQL validation](../09_Testing_and_Validation/sql_validation.md)
