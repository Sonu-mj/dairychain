# Procurement Analysis


## Purpose
This file answers how much milk was procured, how much was accepted and rejected, and what the rejection rate means. It is for a manager who needs to judge supplier and centre performance from the supplied totals.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- What to do next

## Question
How much milk was procured, how much was rejected, and how does rejection differ by supplier, district and collection centre?

## Why it matters
Procurement is a major cost in dairy operations. A high rejection rate means milk was collected, transported and inspected, then could not be used. That is a direct loss of volume and a cost that earns no revenue.

## Data used
Gold table procurement_quality_summary, 18,000 rows, one per batch. Supplier and centre summaries in supplier_performance, 200 rows, and collection_centre_performance, 20 rows.

## Method
Count batches by acceptance status, sum milk volume by status, and divide rejected by total for the batch rate and the volume rate. Compare the two rates: if they differ, rejection is not evenly spread across batch sizes.

## Result
- Procurement batches: 18,000. Accepted: 15,689. Rejected: 2,311.
- Batch rejection rate: 12.84 percent.
- Total milk volume: 8,758,507.64 L. Rejected milk volume: 1,117,247.35 L.
- Volume rejection rate: 12.76 percent.
- Accepted milk volume, calculated from the supplied totals: 7,641,260.29 L.

## What it means
About 1 in 8 batches was rejected, and about 1 in 8 litres was rejected. The batch rate and the volume rate are close, so rejection was not driven mainly by a few very large batches. That is an association in the totals only. It does not prove a cause, and it does not name a supplier or a centre.

## What to do next
Supply the supplier, district and centre breakdowns, the rejection reasons, and the fat and SNF values. Then rank suppliers and centres by rejection rate and volume, and check whether a reason, a district or a centre explains the pattern.

## Key business reference values
The following recorded values can be used as reference points during pipeline validation. They are recorded project references from Source 9. Recalculate them from the database before using them as formal test results.

| Metric | Recorded result |
|---|---:|
| Total procurement batches | 18,000 |
| Accepted batches | 15,689 |
| Rejected batches | 2,311 |
| Batch rejection rate | 12.84% |
| Total milk volume | 8,758,507.64 L |
| Rejected milk volume | 1,117,247.35 L |
| Milk volume rejection rate | 12.76% |
## Numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently shown against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts from Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Intended period: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Quality questions (Source 13)
The milk quality questions QL-01 to QL-05 are placed in full in [../05_Business_Questions_and_Answers/05_procurement_and_supplier_analysis.md](../05_Business_Questions_and_Answers/05_procurement_and_supplier_analysis.md), not duplicated here. QL-01 is shown: 18,000 batches, 15,689 accepted, 2,311 rejected, 12.84 percent batch rejection. QL-04 is now from the model data (Source 23): Low SNF 1,303, Low Fat 513, High Acidity 491, High Temperature 4.

## Next step / Related files
- Production analysis](production_analysis.md)
- Q and A procurement](../05_Business_Questions_and_Answers/05_procurement_and_supplier_analysis.md)
- KPI definitions](kpi_definitions.md)
