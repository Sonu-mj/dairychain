# Rejected Approaches


## Purpose
This file answers which design approaches were rejected, and why. It is for a reader who needs to know which shortcuts were avoided.

## In this file
- Why each was left out

## Rejected
- A single-layer design, with reports built straight from raw CSV files. Rejected because a cleaning error would be hidden in every report, and a Gold number could not be traced back.
- Adding litre and kg quantities together. Rejected because the units are different, and the sum would have no meaning.

## Why each was left out
Each approach above was left out because it would make a number look stronger than its evidence. A documentation set that overclaims is harder to trust than one that states its limits.

## Next step / Related files
- Architecture decisions](architecture_decisions.md)
- Limitations](../06_Business_Findings_and_Impact/limitations_and_future_analysis.md)
- Check file](../../VERIFICATION_AND_MISSING_INFO.md)
