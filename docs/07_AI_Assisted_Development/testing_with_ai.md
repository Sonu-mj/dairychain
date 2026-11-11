# Testing with AI


## Purpose
This file answers how AI helped with testing in DairyChain and what testing still has to prove on its own. It is for a developer who needs test cases that catch real faults, not tests that only pass on clean data. Its sources are the Master Project Brief testing workflow and section 9 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, in full.

## In this file
- Decision framework for AI-generated suggestions
- Accuracy rules for the decision log
- Check areas: Python ingestion
- Check areas: SQL transformations
- Check areas: Power BI
- Test areas from the brief
- Levels of testing
- What AI can do
- Notes

## Tests
AI can suggest test cases, but a suggested test is not an executed test. The methodology distinguishes between:

- **Suggested test:** A test case proposed during development.
- **Executed test:** A test that was actually run.
- **Passed test:** An executed test whose actual result matched the expected result.

Actual test evidence and pass/fail results belong in a test report, not in this methodology document.

## Decision framework for AI-generated suggestions
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 9. Use this framework to assess a proposed solution.

| Decision | Meaning |
|---|---|
| Accept | The approach matches the requirement and has been reviewed |
| Modify | The proposed approach is useful but needs changes |
| Reject | The solution is incorrect, unnecessary, insecure, or unsuitable |
| Investigate | There is not enough evidence to decide whether the solution is correct |

For example, a query that calculates rejected batch percentage cannot automatically be used to calculate rejected milk volume percentage. The calculation must match the business definition. This distinction is important when AI suggests an implementation that looks technically valid but answers a different question.

Do not back-fill this section with invented cases.

## Accuracy rules for the decision log
Source: Decision Log, section 9, user-supplied 2026-11-11, as a short cross-reference. The full log is in [ai_task_log/actual_development_tasks.md](ai_task_log/actual_development_tasks.md). Maintain these rules throughout the project:

1. Do not invent AI prompts or responses.
2. Do not claim that a suggestion was rejected unless it actually happened.
3. Do not mark a suggestion as accepted without reviewing the implementation.
4. Do not claim that a change passed testing without an execution result.
5. Separate technical examples from historical development decisions.
6. Record the actual date and implementation reference where available.
7. Update the entry when an investigating decision is resolved.


## Check areas: Python ingestion
- Confirm expected input files are available.
- Check that records are loaded into the intended Bronze tables.
- Compare loaded row counts with the source files.
- Check for missing or incorrectly typed values.

## Check areas: SQL transformations
- Confirm that the Silver and Gold tables contain the expected columns.
- Check duplicate and missing records where relevant.
- Validate joins and aggregation logic.
- Reconcile important aggregate values with their underlying records.

## Check areas: Power BI
- Check that KPI calculations match the underlying database values.
- Check relationship behaviour and filter interactions.
- Confirm that date and category slicers affect the intended visuals.
- Avoid combining measurements that use incompatible units, such as litres and kilograms.

## Test areas from the brief
- Missing values.
- Duplicate identifiers.
- Invalid quantities.
- Negative values.
- Incorrect date ranges.
- Invalid foreign keys.
- Incorrect aggregations.
- JOIN duplication.
- Inventory reconciliation.
- Revenue and profit calculations.
- Transaction rollback.
- Parameterised queries.

## Levels of testing
- Unit testing: test one function or one query on its own, with known inputs and expected outputs.
- Integration testing: test the pipeline from CSV to Gold, and check counts at each layer.
- Data validation: test the data itself, not only the code, for duplicates, missing values and invalid values.
- End-to-end testing: test the full flow to Power BI, and check that a Gold number appears correctly in the report.

## What AI can do
AI can suggest test cases and edge cases, and can help explain a failure. Only an executed test with its output is a passed test.

## Notes
See [../09_Testing_and_Validation/test_results.md](../09_Testing_and_Validation/test_results.md).

## Next step / Related files
- [Testing strategy](../09_Testing_and_Validation/testing_strategy.md)
- [Unit testing](../09_Testing_and_Validation/unit_testing.md)
- [Code review](code_review.md)
