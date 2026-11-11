# Non-Functional Requirements

> Status: PENDING EVIDENCE

## Purpose
This file answers what quality limits DairyChain must meet, such as correctness, clarity and reproducibility, and what was not promised. It is for a reviewer who wants to know how the work should be judged.

## In this file
- Correctness
- Reproducibility
- Clarity and honesty
- What was not promised

## Correctness
- Record counts must reconcile across Bronze, Silver and Gold. The supplied counts are 99,584 source records, 18,000 procurement batches and 4,000 production batches in Gold, with 14,000 sales orders.
- Litre and kg quantities must never be added together. They are different units and must be analysed separately.
- A KPI must use the same name and formula in every file. See [../04_Business_Analytics/kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md).

## Reproducibility
- A reader with the repo, the CSV files and the SQL should be able to reach the same Gold counts. Status: PENDING EVIDENCE. No repo, SQL, CSV list or run log was supplied, so reproducibility cannot be checked yet.

## Clarity and honesty
- Every finding carries a status label: VERIFIED, PARTIALLY VERIFIED, PENDING EVIDENCE or NOT IMPLEMENTED.
- Measured impact and expected benefit are kept separate. No measured profit or cost saving was supplied, so none is claimed.

## What was not promised
Performance targets, uptime, concurrent users, security controls and production deployment are not stated in the supplied sources. Do not read them into this project.

## Next step / Related files
- Assumptions and constraints](assumptions_and_constraints.md)
- Testing strategy](../09_Testing_and_Validation/testing_strategy.md)
- Verification file](../../VERIFICATION_AND_MISSING_INFO.md)
