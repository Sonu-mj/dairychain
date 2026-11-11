# Unit Testing


## Purpose
This file answers how to unit test DairyChain logic on its own, with known inputs and expected outputs. It is for a developer who needs to catch a fault in one function before it reaches Gold. Its source for the ingestion tests is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 7.1.

## In this file
- What to unit test
- Cases to include
- Python ingestion testing
- Notes

## What to unit test
- Validation functions, such as the illustrative validate_procurement example in [../07_AI_Assisted_Development/python_development.md](../07_AI_Assisted_Development/python_development.md).
- KPI calculations, such as rejection rate, fulfilment rate and average revenue per order.
- Date handling, type conversion and unit handling.
- Any function that cleans, transforms or aggregates a value.

## Cases to include
- Missing values and null identifiers.
- Duplicate identifiers.
- Invalid quantities, including negative and zero values where the rule forbids them.
- Non-numeric values in a numeric field.
- Incorrect date ranges.
- A valid input, so a passing case is also recorded.

## Python ingestion testing
The ingestion process should be tested for:

| Test | Expected behaviour |
|---|---|
| Valid input file | File can be read |
| Missing input file | Clear error is reported |
| Empty input file | Empty input is detected |
| Missing required column | Validation identifies the missing column |
| Unexpected data type | Invalid or incompatible data is identified |
| Database connection failure | Loading does not silently appear successful |
| Successful load | Database row count is checked against the input |

A test in this table is Suggested until its output is recorded in [test_results.md](test_results.md).

## Notes
Add the test files and their outputs to [test_results.md](test_results.md) when they exist.

## Next step / Related files
- [Integration testing](integration_testing.md)
- [Testing with AI](../07_AI_Assisted_Development/testing_with_ai.md)
- [Data quality checks](data_quality_checks.md)
