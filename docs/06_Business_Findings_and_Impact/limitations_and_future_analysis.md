# Limitations and Future Analysis


## Purpose
This file answers what limits DairyChain today. It is for a reader who needs the boundary of the current work.

## In this file
- Limitations
- Power BI model limitations (Source 11)

## Limitations
- Yield is reported in litres and kilograms separately. Raw milk input total is from the model data (Source 23): 2,600,000.0 L.
- Product ranking is from the model data (Source 23): Pure Cow and Buffalo Ghee is the top revenue product at Rs 5,986,642.50.
- The intended period, 1 Nov 2025 to 31 Oct 2026, is shown for the data range from the model data (Source 23): procurement timestamps run 2025-11-01 to 2026-10-31; sales daily order_date runs 2025-11-02 to 2026-10-31.
- Column names, types, and nullability are from Source 18 (238 columns). Keys and constraints are absent by Sources 20 and 21 (0 rows).
- Power BI relationships are from Source 23 (pbixray): only 1 relationship exists in the model, `gold procurement_quality_summary[supplier_id]` to `gold supplier_performance[supplier_id]`, M:1, Single, active. The exact source expressions for procurement_date and production_date are also shown as DAX calculated columns. Source 11 explains that procurement_date and production_date are date-level fields derived from the relevant timestamps.

## Power BI model limitations (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 12). The documented model contains summary tables at different aggregation levels. This is suitable for the current reporting requirements but creates analytical limitations.

- A date filter cannot narrow product-level sales summaries without a date-product-level source table.
- Product filters cannot narrow daily sales revenue without product-level daily sales data or an appropriate bridge.
- Supplier summaries do not provide the same detail as individual procurement batches.
- Collection-centre summaries cannot replace procurement-level detail.
- Some cross-analysis questions require more detailed source data than the current Gold tables expose.

These limitations should be explained rather than hidden by creating relationships that do not represent genuine business relationships.

## Next step / Related files
- [Executive summary](executive_summary.md)
- [Implementation status](../13_Project_Evidence/implementation_status.md)
