# Sales Analysis

> Status: VERIFIED

## Purpose
This file answers how much DairyChain sold, how much was delivered in full, and how much was not. It is for a manager who needs revenue together with fulfilment, not revenue alone.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- Slicer behaviour (Source 11)
- Aggregation warnings (Source 11)
- Product revenue ranking - VERIFIED by Source 23 (model data)
- What to do next

## Question
How much revenue did sales make, how many orders were delivered in full, and how much quantity was fulfilled?

## Why it matters
Revenue shows what was sold. Fulfilment shows what reached the customer. An order that is partially delivered or cancelled still appears in the order count, but it does not deliver the same value as a delivered order.

## Data used
Gold tables sales_product_performance, 12 rows, one per product, and sales_daily_summary, 364 rows, one per day. The 12 product rows are now VERIFIED from the model data read with pbixray get_table (Source 23) - see the product table below. The 364 daily rows themselves were not supplied, so no daily trend is given here.

## Method
Sum revenue and orders, count orders by status, and divide quantity fulfilled by quantity ordered. Check that delivered plus partially delivered plus cancelled equals total orders.

## Result
- Total sales revenue: Rs 26,734,294.03. Total orders: 14,000.
- Quantity ordered: 181,804. Quantity fulfilled: 161,036.41. Unfulfilled quantity, calculated: 20,767.59. Fulfilled share, calculated: 88.58 percent.
- Delivered: 11,166, 79.76 percent. Partially delivered: 2,227, 15.91 percent. Cancelled: 607, 4.34 percent.
- Orders not delivered in full, calculated: 2,834.
- Average revenue per order, calculated: Rs 1,909.59.

## Product revenue ranking - VERIFIED by Source 23 (model data)
Source: `gold sales_product_performance` read with pbixray get_table, 2026-11-11. Ranked by total revenue, highest first. "Product-associated orders" means the order count recorded against that product; it is not a distinct order count.

| Product | Category | Product-associated orders | Quantity ordered | Quantity fulfilled | Total revenue (Rs) | Share of revenue |
|---|---|---:|---:|---:|---:|---:|
| Pure Cow and Buffalo Ghee | Fat Rich | 2296 | 14,987.00 | 9,740.25 | 5,986,642.50 | 22.39 percent |
| Fresh Malai Paneer | Coagulated | 2341 | 15,367.00 | 14,693.00 | 5,531,071.00 | 20.69 percent |
| Pasteurised Table Butter | Fat Rich | 2370 | 15,378.00 | 10,009.16 | 5,156,439.08 | 19.29 percent |
| Fresh Dairy Cream | Fat Rich | 2365 | 15,312.00 | 10,817.00 | 2,354,907.50 | 8.81 percent |
| Elaichi Flavoured Milk | Beverage | 2328 | 15,110.00 | 14,532.00 | 1,799,512.50 | 6.73 percent |
| Probiotic Lassi | Fermented | 2288 | 14,861.00 | 14,163.00 | 1,123,028.00 | 4.20 percent |
| Classic Set Curd | Fermented | 2339 | 15,233.00 | 14,687.00 | 1,091,328.75 | 4.08 percent |
| Full Cream Milk | Liquid Milk | 2248 | 14,615.00 | 14,028.00 | 916,687.20 | 3.43 percent |
| Standardised Milk | Liquid Milk | 2280 | 14,905.00 | 14,324.00 | 851,256.00 | 3.18 percent |
| Toned Milk | Liquid Milk | 2394 | 15,496.00 | 14,890.00 | 796,826.70 | 2.98 percent |
| Double Toned Milk | Liquid Milk | 2385 | 15,307.00 | 14,600.00 | 694,144.80 | 2.60 percent |
| Spiced Masala Buttermilk | Beverage | 2366 | 15,233.00 | 14,553.00 | 432,450.00 | 1.62 percent |
| **Total** | | **28,000** | **181,804.00** | **161,036.41** | **26,734,294.03** | **100.00 percent** |

Reading the table: the top 3 products carry 62.37 percent of revenue (Pure Cow and Buffalo Ghee 22.39 percent, Fresh Malai Paneer 20.69 percent, Pasteurised Table Butter 19.29 percent), so a problem with one of them matters more than a problem with a small one. Spiced Masala Buttermilk is the smallest revenue product at Rs 432,450.00, 1.62 percent. Product revenue sums to Rs 26,734,294.03, matching the daily total exactly. Product-associated orders sum to 28,000, not 14,000 - see the verified proof in the Aggregation warnings section below.

## What it means
About 1 in 5 orders was not delivered in full. That is a fulfilment gap, not a revenue gap alone, because partially delivered orders still earn some revenue and cancelled orders earn none. The cause is not stated in the README, so no cause is claimed here.

## Slicer behaviour (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 7). A slicer should only affect visuals that are connected to its underlying data through the reporting model or an intentionally configured interaction. Slicer behaviour is documented intent. The slicers themselves are now verified as present in the supplied .pbix (Source 22): Page 1 has `dim_product[product_name]`, `dim_product[category]`, and `dim_date[Date]` plus an auto date table (Year, Quarter); Page 4 has `gold sales_daily_summary[order_date]`, `gold sales_product_performance[Short Product Name]`, and `gold sales_product_performance[category]`. Whether each slicer actually filters the intended visuals is still not verified as rendered, and Source 23 found only one relationship in the model, so most slicers have no relationship path to follow.

### Date slicer
Field: `dim_date[Date]`. Expected relevant tables: `sales_daily_summary`, `procurement_quality_summary`, and `production_performance`. This supports time-based analysis across the three reporting areas. However, the product-level sales summary has no date key, so a date slicer cannot filter `sales_product_performance` through the documented relationships.

### Product Category slicer
Field: `gold sales_product_performance[category]`, or the corresponding product category attribute in `dim_product`. Expected relevant reporting area: product-level sales visuals. A product category slicer should not be assumed to filter daily sales summary because that table does not contain product-level information.

### Product Name slicer
Field: `gold sales_product_performance[product_name]`, or the corresponding product attribute in `dim_product`. Expected relevant reporting areas: product sales analysis, and production analysis through the product dimension. It should not be assumed to filter daily revenue because `sales_daily_summary` contains date-level rather than product-level records.

### Supplier or district slicer
Supplier-based filtering should operate through `dim_supplier` where the district attribute is available in that dimension. It should affect the related supplier and procurement information, not unrelated production or sales aggregates.

### Shift slicer
The procurement and production tables have their own shift fields. A procurement shift slicer should not automatically be expected to filter production data. These are separate operational events and should have separate filtering behaviour unless a deliberate shared shift dimension and business requirement are implemented.

## Aggregation warnings (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 8). See also [kpi_definitions.md](kpi_definitions.md).

### Order counts
Do not sum the product-level `total_orders` in `sales_product_performance` to get the overall distinct order count. VERIFIED PROOF from the model data (Source 23): product `total_orders` sums to 28,000, while the distinct order total in `sales_daily_summary` is 14,000. An order appears once per product, so summing product-level orders counts the same order more than once. Use the date-level calculation for the overall total. The overall project reference is 14,000 orders.

### Revenue
Revenue exists in both `sales_product_performance` and `sales_daily_summary`, at different grains. Each can be used for its relevant reporting purpose, but the values must not be added together because they represent the same business activity at different aggregation levels. The recorded total revenue is Rs 26,734,294.03. Source 23: both grains now VERIFIED from the model data to the same total, Rs 26,734,294.03.

## What to do next
The product breakdown is now supplied (Source 23) and ranked above. Still to supply: the daily breakdown, the cancellation reasons and the average selling price. Then check whether a product, a day or a reason explains the gap.

## Key business reference values
The following recorded values can be used as reference points during pipeline validation. They are recorded project references from Source 9. Recalculate them from the database before using them as formal test results.

| Metric | Recorded result |
|---|---:|
| Total sales revenue | Rs 26,734,294.03 |
| Total orders | 14,000 |
| Delivered orders | 11,166 |
| Partially delivered orders | 2,227 |
| Cancelled orders | 607 |
| Quantity ordered | 181,804 |
| Quantity fulfilled | 161,036.41 |
## Verified numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently verified against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts VERIFIED by Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Sales: revenue Rs 26,734,294.03, 14,000 orders, quantity ordered 181,804, quantity fulfilled 161,036.41, delivered 11,166, partially delivered 2,227, cancelled 607.
- Source 23: all sales totals above are now VERIFIED against the model data read with pbixray get_table; the product rows are in the table above; discounts total Rs 250,307.17 verified from the model data.
- Intended period, to verify: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- [Profitability analysis](profitability_analysis.md)
- Q and A sales](../05_Business_Questions_and_Answers/09_sales_and_demand.md)
- KPI definitions](kpi_definitions.md)
