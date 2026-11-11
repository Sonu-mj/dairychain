# Testing Strategy


## Purpose
This file answers how DairyChain should be tested, at each level, and what a passed test means. It is for a developer who needs to prove the pipeline, not only run it once. Its source is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, sections 7, 9 and 12.

## In this file
- Levels
- What each level proves
- What counts as passed
- Key learning

## Levels
- Unit testing: one function or one query on its own. See [unit_testing.md](unit_testing.md).
- Integration testing: the pipeline from CSV to Gold, with counts at each layer. See [integration_testing.md](integration_testing.md).
- SQL validation: each query checked for grain, JOIN duplication and aggregation accuracy. See [sql_validation.md](sql_validation.md).
- Data quality checks: the data itself checked for duplicates, missing values and invalid values. See [data_quality_checks.md](data_quality_checks.md).

Testing should cover different stages of the data pipeline: Python ingestion, Bronze, Silver, Gold, business metrics, and Power BI. The stage tables are in the files above.

## What each level proves
- Unit tests prove the logic is right on known inputs.
- Integration tests prove the layers join up and the counts reconcile.
- SQL validation proves a sum is not doubled by a JOIN and not lost by a filter.
- Data quality checks prove the data is fit for the report, not only that the code ran.

## What counts as passed
A test counts as passed only when it was executed and its output is kept. A test that passed on clean data but was never run on dirty data is only partly proven. See [test_results.md](test_results.md).

A major documentation rule is not to confuse proposed tests with executed tests.


For example, an AI-generated SQL query is not a passed test. A query that executes is not automatically a passed business-logic test.

## Key learning
Debugging is not simply finding code that removes an error. AI can make this process more efficient by helping explain errors, identify possible causes, and suggest targeted changes. However, the developer remains responsible for reproducing the issue, judging the suggested correction, executing it, and validating the result.

> The most useful outcome of debugging is not just code that runs. It is an implementation whose behaviour I can explain and check.


## Next step / Related files
- [Unit testing](unit_testing.md)
- [Integration testing](integration_testing.md)
- [SQL validation](sql_validation.md)
- [Test results](test_results.md)
