# Rejected Approaches

> Status: PARTIALLY VERIFIED

## Purpose
This file answers what DairyChain did not do, and why. It is for a reader who needs to know which shortcuts were avoided and which future options were left for later.

## In this file
- Rejected or not claimed
- Why each was left out
- Future options

## Rejected or not claimed
- A single-layer design, with reports built straight from raw CSV files. Rejected because a cleaning error would be hidden in every report, and a Gold number could not be traced back.
- Adding litre and kg quantities together. Rejected because the units are different, and the sum would have no meaning.
- Quoting revenue as profit. Rejected because profit needs COGS and operating expenses, which were not supplied.
- Claiming forecasting or predictive demand modelling. Not claimed, because it is not described as implemented in the README.
- Claiming cloud deployment, automated orchestration, real-time streaming, production monitoring or enterprise security. Not claimed, because none is demonstrated in the supplied sources.

## Why each was left out
Each approach above was left out because it would make a number look stronger than its evidence. A documentation set that overclaims is harder to trust than one that states its limits.

## Future options
The README lists future improvements, including Airflow orchestration, automated quality checks, cloud processing and more detailed forecasting. Those are future possibilities, not rejected ideas. Their status is NOT IMPLEMENTED. See [../06_Business_Findings_and_Impact/limitations_and_future_analysis.md](../06_Business_Findings_and_Impact/limitations_and_future_analysis.md).

## Next step / Related files
- Architecture decisions](architecture_decisions.md)
- Limitations](../06_Business_Findings_and_Impact/limitations_and_future_analysis.md)
- Verification file](../../VERIFICATION_AND_MISSING_INFO.md)
