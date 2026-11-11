# Pipeline Performance


## Purpose
This file answers how to judge whether the DairyChain pipeline is fast enough and where its time goes. It is for a developer who needs a measured view, not a guess about the slowest step.

## In this file
- What to measure
- What to record
- Notes

## What to measure
- Time to ingest the 10 CSV files.
- Time to clean and build Silver.
- Time to build each of the 6 Gold tables.
- Time to refresh the Power BI report.
- Row counts at each step, so a slow step can be separated from a large step.

## What to record
For each run, record the start and end time per step, the row count per step, and any step that failed or was retried. A single total time does not show which step needs work.

## Notes
No pipeline timing, run log or performance measurement was supplied. Do not claim a run time, a fastest step or a measured improvement.

## Next step / Related files
- Query optimization](query_optimization.md)
- Python optimization](python_optimization.md)
- Pipeline execution](../03_Data_Engineering/pipeline_execution.md)
