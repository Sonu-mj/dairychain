# Production Analysis

> Status: VERIFIED

## Purpose
This file answers how many production batches ran and how much finished product and byproduct came out, split by unit. It is for a manager who needs output without mixing litres and kilograms.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- What to do next

## Question
How much finished product and byproduct did production make, and how should the result be read when batches use different units?

## Why it matters
Production turns accepted milk into saleable product. Output alone does not prove efficiency. Efficiency needs output against input, by batch, product and shift, in the same unit.

## Data used
Gold table production_performance, 4,000 rows, one per production batch. Raw milk input total is now VERIFIED from the model data (Source 23): 2,600,000.0 L in total, 1,950,650.0 L for litre batches and 649,350.0 L for kg batches. Yield still cannot be calculated as a single figure: for litre batches finished plus byproduct equals the input exactly, and for kg batches the outputs are in kg while the input is recorded in litres.

## Method
Sum finished output and byproduct output separately for litre-based batches and for kg-based batches. Never add a litre total to a kg total. Report duration and shift performance only when the breakdown is supplied.

## Result
- Production batches: 4,000.

| Unit | Production batches | Finished output | Byproduct output |
|---|---:|---:|---:|
| Litres | 3,001 | 1,484,135.25 L | 466,514.75 L |
| Kilograms | 999 | 266,416.65 kg | 402,413.85 kg |

The batch split is new from Source 9, the Data Ingestion and Transformation Pipeline document, 2026-11-11: 3,001 litre-based batches plus 999 kg-based batches equals 4,000 batches. Do not combine production output measured in litres and kilograms. No combined total is given, because litres and kg cannot be added. Raw milk input (Source 23, model data): litre batches 1,950,650.0 L, kg batches 649,350.0 L, total 2,600,000.0 L. The kg-batch input is recorded in litres, so it is not added to a kg output total.

## What it means
The README gives output, not efficiency. With the input total now known, the litre side reconciles exactly: finished 1,484,135.25 L plus byproduct 466,514.75 L equals the litre-batch input of 1,950,650.0 L, so no litre loss is shown. The kg side cannot be compared the same way, because its outputs are in kg and its input is recorded in litres. No yield, no loss and no batch ranking can be stated as a single figure. A batch with high output may simply have had high input.

## What to do next
Raw milk input per batch is now supplied in total (Source 23). Still to supply: input per batch in the same unit as its output, plus product and shift. Then calculate yield as finished output divided by raw milk input, times 100, and list the lowest-yield batches for investigation.
## Verified numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently verified against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts VERIFIED by Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches (3,001 litre-based, 999 kg-based, from Source 9). Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Source 23: raw milk input total 2,600,000.0 L now VERIFIED from the model data.
- Sales: revenue Rs 26,734,294.03, 14,000 orders, quantity ordered 181,804, quantity fulfilled 161,036.41, delivered 11,166, partially delivered 2,227, cancelled 607.
- Intended period, to verify: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Procurement analysis](procurement_analysis.md)
- Sales analysis](sales_analysis.md)
- Q and A production](../05_Business_Questions_and_Answers/06_production_efficiency.md)
