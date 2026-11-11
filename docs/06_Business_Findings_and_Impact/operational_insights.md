# Operational Insights


## Purpose
This file answers what the operations data shows about procurement, production and sales together. It is for a manager who needs the operational picture, not a single total.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- What to do next

## Question
What do procurement, production and sales together show about operations?

## Why it matters
Operations are connected. Milk rejected in procurement cannot enter production. Product not produced cannot be sold. Orders not fulfilled in sales can point back to procurement or production, but only the breakdown can prove the link.

## Data used
Procurement totals, production output totals and sales totals from the README. No breakdown by supplier, centre, product, shift or day was supplied.

## Method
Read the three areas side by side, at the same period, and check whether the volumes are consistent. Do not claim a cause from a period total alone.

## Result
- Procurement: 8,758,507.64 L in, 1,117,247.35 L rejected, 7,641,260.29 L accepted, calculated.
- Production: 4,000 batches, with finished and byproduct output in litres and in kg, as listed in the key findings file.
- Sales: Rs 26,734,294.03 from 14,000 orders, with 2,834 orders not delivered in full.

## What it means
The three areas each show a gap: rejection in procurement, unknown yield in production, and incomplete fulfilment in sales.

## What to do next
Supply the breakdowns by supplier, centre, product, shift and day, with reasons for rejection, cancellation and partial delivery. Then test whether the same supplier, product or day explains more than one gap.
## Numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently shown against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts from Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Intended period: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Key findings](key_findings.md)
- Recommendations](recommendations.md)
- Q and A anomaly](../05_Business_Questions_and_Answers/12_anomaly_and_irregularity_findings.md)
