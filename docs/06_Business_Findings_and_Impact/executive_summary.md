# Executive Summary

> Status: VERIFIED

## Purpose
This file answers, in one page, what DairyChain found, what it did not find, and what management should do next. It is for an executive who needs the whole result without reading every analysis file.

## In this file
- The project in one line
- Three findings the numbers support
- What is not known yet
- The next three actions

## The project in one line
DairyChain joins procurement, quality, production and sales data in PostgreSQL and Power BI, so a dairy manager can see where milk is lost, how production performs, and how much of what was ordered was delivered.

## Three findings the numbers support
1. Procurement rejection is about 1 in 8. Rejected batches are 2,311 of 18,000, 12.84 percent. Rejected milk is 1,117,247.35 L of 8,758,507.64 L, 12.76 percent.
2. Fulfilment is incomplete on about 1 in 5 orders. Delivered orders are 11,166 of 14,000. Partially delivered orders are 2,227 and cancelled orders are 607, together 2,834 orders not delivered in full. Quantity fulfilled is 161,036.41 of 181,804 ordered, 88.58 percent.
3. Production output is reported in two units that must stay separate. Finished litre-based output is 1,484,135.25 L and finished kg-based output is 266,416.65 kg. No combined output total is valid.

## What is not known yet
Profit, product profit, outlet profit, cost drivers, yield, wastage, returns, inventory risk, expenses and energy use cannot be stated from the supplied numbers, because their inputs were not supplied. Those topics are marked PENDING EVIDENCE or NOT IMPLEMENTED in the Q and A folder.

## The next three actions
1. Get the rejection reasons and the supplier, district and centre breakdowns.
2. Get the cancellation and partial-delivery reasons by product and day.
3. Get the cost inputs, COGS, discounts, returns and operating expenses, before any profit decision.
## Verified numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently verified against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts VERIFIED by Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Sales: revenue Rs 26,734,294.03, 14,000 orders, quantity ordered 181,804, quantity fulfilled 161,036.41, delivered 11,166, partially delivered 2,227, cancelled 607.
- Intended period, to verify: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Key findings](key_findings.md)
- Recommendations](recommendations.md)
- Limitations](limitations_and_future_analysis.md)
