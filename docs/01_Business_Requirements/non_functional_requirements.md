# Non-Functional Requirements


## Purpose
This file answers what quality limits DairyChain must meet, such as correctness, clarity and reproducibility. It is for a reviewer who wants to know how the work should be judged.

## In this file
- Correctness
- Reproducibility
- Clarity and honesty

## Correctness
- Record counts must reconcile across Bronze, Silver and Gold. The supplied counts are 99,584 source records, 18,000 procurement batches and 4,000 production batches in Gold, with 14,000 sales orders.
- Litre and kg quantities must never be added together. They are different units and must be analysed separately.
- A KPI must use the same name and formula in every file. See [../04_Business_Analytics/kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md).

## Reproducibility
- A reader with the repo, the CSV files and the SQL should be able to reach the same Gold counts.

## Clarity and honesty
- Measured impact and expected benefit are kept separate.

## Next step / Related files
- Assumptions and constraints](assumptions_and_constraints.md)
- Testing strategy](../09_Testing_and_Validation/testing_strategy.md)
- Check file](../../VERIFICATION_AND_MISSING_INFO.md)
