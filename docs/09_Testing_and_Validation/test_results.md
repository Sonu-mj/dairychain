# Test Results


## Purpose
This file answers which tests were actually executed in DairyChain and what they showed. It is for a reviewer who needs executed results, not a list of tests that were planned. Its source for the status meanings is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 9.

## In this file
- What was supplied
- How to add a result
- Rule

## What was supplied
One Colab notebook, `dairychain.ipynb` (Source 15, 2026-11-11), holds the validation checks. Its cells run the checks and its stored outputs show the results. Those checks are listed below as from stored outputs. They are notebook validation checks. Do not describe them as a passed test suite.

## Dataset validation report - Source 28

The dataset ZIP (Source 28, 2026-11-11) supplies its own validation report, `validation_report.txt`, copied to [dataset_validation_report.txt](../13_Project_Evidence/dataset_validation_report.txt). It lists 29 checks, all PASS: 10 primary-key uniqueness checks (one per dataset), 10 foreign-key checks, and 9 business-rule checks (all production batches completed, inputs from accepted procurement only, input after source timestamp, source consumption not over procurement, fulfilled not above ordered, fulfilled non-negative, sales not above total primary output, procurement cost matches except the injected row, and the five intentional DQ patterns present). Total datasets 10, total rows 99,584, total CSV size 7.47 MB, generation time 2.27 seconds.

This report shows the generated files are internally consistent, including the 5 deliberate faults.

## Validation evidence from the notebook - Source 15
All values below are from the notebook's stored outputs, with cell numbers. "PASS" in the last rows is the notebook's own label in its `quality_report` dataframe (cells 111, 114, 116), not a test-framework verdict.

| Check | Cells | Result in stored output |
|---|---|---|
| Duplicate rows, all 10 datasets | 19, 27, 50, 66, 68, 70, 72, 74, 76, 78, 80 | 0 duplicate rows in every dataset; 0 duplicate keys (supplier_id, procurement_id, test_id, centre_id, product_id, production_id, output_id, input_id, order_id, order_line_id) |
| Missing values, suppliers and procurement | 18, 26 | 0 in every column |
| Missing values, quality tests | 47, 49, 62 | temperature_c missing 1 (QCT-000250, Accepted); rejection_reason missing 15,689, all Accepted rows, so expected |
| Missing values, sales orders | 76, 81 | actual_delivery_date missing 607, all Cancelled orders; delivery_delay_days missing 607 |
| Missing values, sales order lines | 78 | 0 in every column |
| Procurement cost reconciliation | 38, 40, 97, 112, 117, 122 | 1 mismatch: PRC-001000, SUP-0155, recorded 33,285.84, calculated 26,628.67, difference 6,657.17; 17,999 valid; exception rate 0.0056 percent |
| Procurement-quality status match | 99, 100, 115 | 0 mismatches across 18,000 records; crosstab Accepted 15,689, Rejected 2,311, no cross-matches |
| Rejection-rule consistency | 61 | 0 inconsistent records for each rule: Low SNF, Low Fat, High Acidity, High Temperature |
| Quality summary | 62 | 18,000 records, 1 missing temperature, 0 duplicate rows, 0 duplicate test ids, 0 missing rejection reasons among Rejected rows |
| Negative numeric values | 108 | 0 for quantity_litres, purchase_rate_per_litre, fat, SNF, temperature, acidity |
| Accepted quality rule violations | 110 | 0 for fat below 3.2, SNF below 8.2, temperature above 8.5C, acidity above 0.17 |
| Quality timestamps | 107 | 0 invalid timestamps |
| Referential integrity, 8 relationships | 83 | 0 invalid references: procurement to suppliers, procurement to centres, quality tests to procurement, production batches to products, production outputs to batches, production inputs to batches, order lines to orders, order lines to products |
| Sales line totals and quantities | 78 | Line total mismatches 0; invalid quantities 0; fulfilled more than ordered 0; invalid prices 0; invalid discounts 0; total sales value 26,734,294.03, matching the README |
| Order fulfilment, order level | 86 | 0 errors for Delivered, Partially Delivered and Cancelled orders after aggregating lines per order |
| Order fulfilment, line level | 84, 85 | 3,795 flagged lines under Partially Delivered orders. This is a grain artefact, not a defect: a partially delivered order has some lines fully fulfilled and some at 0, so a per-line check flags them. The order-level check in cell 86 gives 0 errors. Do not report 3,795 as failed orders. |
| Production input/output, litre batches | 94 | 3,001 litre-based batches, 0 mismatches, difference 0.00 |
| Production input/output, naive combined check | 89, 91 | 999 mismatches, all with quantity difference -19.5, all kg-based batches. This is a unit-mixing artefact: input is in litres and output is in kilograms, so the two must not be compared as one number. Cells 95-96 confirm the 999 kg batches each have a primary and a residual output. Do not report 999 as failed batches. |
| Notebook quality report, 7 checks | 111, 114, 116 | Procurement cost validation: 1 mismatch flagged. The other 6 checks read PASS - 0 mismatches, 0 invalid timestamps, 0 negative values, 0 violations, 0 invalid references, 0 duplicates. These are the notebook's own labels. |
| Rejection reasons, counts | 43, 44 | Low SNF 1,303 (56.38 percent), Low Fat 513 (22.20 percent), High Acidity 491 (21.25 percent), High Temperature 4 (0.17 percent), total 2,311. The rejection-reason breakdown comes from the notebook's stored outputs. |
| Supplier rejection, highest | 101, 103 | SUP-0087: 84 records, 40,492.31 L, rejection rate 26.05 percent. Supplier risk list uses total_records of 80 or more and rejection rate above 15 percent. |
| Centre rejection, highest | 124, 126 | CC-002: 930 records, 442,288.44 L, rejected 60,816.91 L, rate 13.75 percent, above the overall 12.76 percent. |
| Total milk, notebook calculation | 98, 125 | Total 8,758,507.64 L, accepted 7,641,260.29 L, rejected 1,117,247.35 L, volume rejection 12.76 percent. Matches the README exactly. |

For example, an AI-generated SQL query is not a passed test. A query that executes is not automatically a passed business-logic test.

## How to add a result
For each test, add: the test name, the level (unit, integration, SQL validation or data quality), the input, the expected output, the actual output, the date run, and the result (passed or failed). Keep the output file or log with the entry.

## Rule
Only tests that have actually been executed should be reported as passed. A planned test is not a passed test. A test without its output is not a result.

## Next step / Related files
- [Testing strategy](testing_strategy.md)
- [Unit testing](unit_testing.md)
- [Integration testing](integration_testing.md)
