# KPI Definitions

> Status: PARTIALLY VERIFIED

## Purpose
This file answers what every KPI in DairyChain means, with the same name and formula in every file. It is for any reader who needs to check a number before quoting it.

## In this file
- KPI table
- Formulas from the brief
- Representative DAX measures: procurement rejection rate
- Power BI calculation review
- Aggregation considerations (Source 11)
- Example DAX measures (Source 11)
- Verified DAX measures, calculated columns, and calculated tables - Source 23 (pbixray)
- What cannot be calculated yet
- Unit and zero rules

## KPI table
| KPI | Formula | Unit |
|---|---|---|
| Batch rejection rate | Rejected batches / Total batches x 100 | Percent |
| Volume rejection rate | Rejected milk volume / Total milk volume x 100 | Percent |
| Fulfilment rate by quantity | Quantity fulfilled / Quantity ordered x 100 | Percent |
| Delivered order share | Delivered orders / Total orders x 100 | Percent |
| Cancelled order share | Cancelled orders / Total orders x 100 | Percent |
| Average revenue per order | Total sales revenue / Total orders | INR per order |

## Formulas from the brief
- Gross sales: sum of sale value before discounts and returns.
- Net revenue: Gross sales - Discounts - Sales returns.
- Gross profit: Net revenue - Cost of Goods Sold.
- Gross profit margin: (Gross Profit / Net Revenue) x 100.
- Operating profit: Gross Profit - Operating Expenses.
- Operating profit margin: (Operating Profit / Net Revenue) x 100.
- Procurement value: sum of procured quantity x procurement price.
- Production yield: (Finished output / Relevant raw material input) x 100.
- Wastage rate: (Wastage quantity / Appropriate total quantity basis) x 100.
- Return rate: Returned quantity / Relevant sold quantity x 100.
- Expense-to-revenue ratio: (Operating Expenses / Net Revenue) x 100.
- Inventory balance: Opening stock + Signed stock movements.

## Representative DAX measures: procurement rejection rate
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 8. These are representative DAX measures for the Procurement and Quality Analysis page, not verified Power BI measures. The source table and columns below are user-supplied in that document. A .pbix file has now been supplied (Source 22), and its model has now been read with pbixray (Source 23), so the VERIFIED formulas are in the Source 23 section below. The measure names Total Milk Procured, Total Accepted Milk, Total Rejected Milk and Overall Rejection Rate ARE referenced in the .pbix. Source 23 correction: the representative Total Milk Procured and Overall Rejection Rate formulas below match the verified formulas, but the representative Total Rejected Milk formula below does NOT match the verified one - see the correction note after the Milk Rejection Rate block.

**Total Milk Procured**

```dax
Total Milk Procured =
SUM(
    'gold procurement_quality_summary'[quantity_litres]
)
```

**Total Rejected Milk**

```dax
Total Rejected Milk =
CALCULATE(
    SUM(
        'gold procurement_quality_summary'[quantity_litres]
    ),
    'gold procurement_quality_summary'[quality_status]
        = "Rejected"
)
```

**Milk Rejection Rate**

```dax
Overall Rejection Rate =
DIVIDE(
    [Total Rejected Milk],
    [Total Milk Procured],
    0
)
```

### Source 23 correction - Total Rejected Milk
The representative Total Rejected Milk formula above is a CALCULATE on `gold procurement_quality_summary[quantity_litres]` filtered to `quality_status = "Rejected"`. The VERIFIED dashboard formula (Source 23, pbixray) is different: a plain SUM of `gold collection_centre_performance[rejected_milk_litres]`, defined on `gold collection_centre_performance`. Do not quote the representative formula as the dashboard formula. The verified formula is in the Source 23 section below. Whether the two formulas return the same total was not checked here, so no equality is claimed.

### Verification considerations
The measure must be checked for:

- Correct source columns.
- Correct quality-status values.
- Correct filter behaviour.
- Consistency with the underlying PostgreSQL calculation.
- Appropriate percentage formatting in Power BI.

The rejection rate calculated from milk volume is not the same as the rejection rate calculated from the number of batches. These are two different business metrics. The volume rejection rate supplied in the README is 12.76 percent (1,117,247.35 L of 8,758,507.64 L). The batch rejection rate is 12.84 percent (2,311 of 18,000 batches). Do not use one in place of the other.

## Rejection metrics and average selling price
Source: the user-supplied "DairyChain - Database Architecture" document (Source 10, 2026-11-11, sections 5 and 9).

### Batch rejection rate vs volume rejection rate
Two different rejection metrics can be calculated from `gold.procurement_quality_summary`. They must not be treated as interchangeable.

- Batch rejection rate: Rejected Batches / Total Batches x 100. Recorded result: 2,311 / 18,000 x 100 = 12.84 percent.
- Milk-volume rejection rate: Rejected Milk Volume / Total Milk Volume x 100. Recorded result: 1,117,247.35 L / 8,758,507.64 L x 100 = 12.76 percent.

Use the batch rate when the question is about batches, and the volume rate when the question is about milk volume. The DAX measures above use milk volume, not batch count, so they answer the volume question only.

### Average selling price warning
`average_selling_price` in `gold.sales_product_performance` is a product-level field. An unweighted average of this field across products is not necessarily the same as the weighted average selling price across all transactions. The exact calculation and aggregation method should be documented when defining Power BI measures. Do not average the product-level field across products and present the result as the overall average selling price.

## Power BI calculation review
Source: "Code Review and Security Practices", section 6 (Source 5). A Power BI visual may display a plausible number even when its underlying measure or relationship is incorrect. The following checks should be performed.

| Review area | What to inspect |
|---|---|
| DAX measures | Correct formula and source columns |
| Relationships | Correct keys and cardinality |
| Filter direction | Whether filters propagate as intended |
| Date table | Correct date relationships and reporting coverage |
| Slicers | Whether each slicer affects the intended visuals |
| Aggregation | Whether values are counted, averaged, or summed appropriately |
| Units | Whether litres and kilograms remain separate |

### Rejection-rate measures
The DAX measures in the "Representative DAX measures" section above use milk volume rather than batch count: Total Milk Procured, Total Rejected Milk, and Overall Rejection Rate using DIVIDE. They are representative only, except where the verified formulas in the Source 23 section below replace them. The verified Total Rejected Milk formula is a plain SUM of `gold collection_centre_performance[rejected_milk_litres]`, not the CALCULATE on procurement quantity shown above, so the representative version must not be quoted as the dashboard formula. A reviewer should confirm that the measure returns the correct value for the current filter context. A milk-volume rejection rate should not be labelled as a batch rejection rate. The volume rate is 12.76 percent and the batch rate is 12.84 percent. Do not use one in place of the other.

## Aggregation considerations (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 8). Incorrect aggregations are a common source of misleading dashboard numbers. All measures below are representative / illustrative from that source. A .pbix file has now been supplied (Source 22), and its model has now been read with pbixray (Source 23), so the VERIFIED DAX formulas are in the Source 23 section below; the measures in this section stay representative / illustrative.

### Order counts
`sales_daily_summary` contains one record per date and includes total orders. For overall daily order totals, summing its `total_orders` values is appropriate when the dates are unique and the table's business definition is consistent. However, `sales_product_performance` contains one record per product, and a product-level order count may represent orders associated with each product. One order can potentially contain multiple products. Do not assume that summing the product-level `total_orders` gives the overall distinct order count. The overall project reference is 14,000 orders. Use a verified order-level or date-level calculation for the overall total.

### Revenue
Revenue exists in both `sales_product_performance` and `sales_daily_summary`. These tables represent revenue at different grains. The product-level table supports product comparisons. The date-level table supports daily revenue analysis. Each can be used for the relevant reporting purpose, but the values must not be added together because they represent the same business activity at different aggregation levels. The recorded total revenue is Rs 26,734,294.03.

### Production quantities
The production table contains quantities in litres and kilograms. A total quantity calculation must respect the selected unit. Do not create an overall production output metric that adds both units without an appropriate conversion.

### Average selling price
The product-level table contains an `average_selling_price` value for each product. An unweighted average across products is not necessarily equivalent to a weighted average across all transactions. The intended KPI must define whether it represents the average of product-level average prices, total revenue divided by total fulfilled or sold quantity subject to the correct sales definition, or the average transaction-level selling price. The measure should be named and interpreted according to its actual calculation.

## Verified DAX measures, calculated columns, and calculated tables - Source 23
Source: `dairy_chain_project.pbix`, read with the open-source pbixray Python library (Source 23, 2026-11-11). pbixray reads the model without Power BI Desktop. This replaces the Source 22 limitation: unzipping the file alone could not parse the XPress9-compressed DataModel, but pbixray extracted the DAX, relationships, and Power Query. Evidence file: [pbixray_dax_measures.txt](../13_Project_Evidence/pbixray_dax_measures.txt) (full DAX dump, 291 lines). Model metadata: Culture en-US, ModifiedTime 2026-11-09 21:23:18, StructureModifiedTime 2026-11-10 19:52:10.

### Verified DAX measures - 23 rows, 21 with formulas, 2 empty
pbixray `dax_measures` returns 23 rows. The formulas below are copied exactly from the extraction. Short single-line formulas are shown in the table; multi-line formulas follow in full.

| Measure | Host table | Verified DAX formula |
|---|---|---|
| Total Revenue | `gold collection_centre_performance` | `SUM('gold sales_product_performance'[total_revenue])` |
| Total Orders | `gold collection_centre_performance` | `SUM('gold sales_daily_summary'[total_orders])` |
| Delivered Orders | `gold collection_centre_performance` | `SUM('gold sales_daily_summary'[delivered_orders])` |
| Total Products | `gold collection_centre_performance` | `DISTINCTCOUNT('gold sales_product_performance'[product_id])` |
| Total Suppliers | `gold collection_centre_performance` | `DISTINCTCOUNT('gold supplier_performance'[supplier_id])` |
| Total Rejected Milk | `gold collection_centre_performance` | `SUM('gold collection_centre_performance'[rejected_milk_litres])` |
| Overall Rejection Rate | `gold collection_centre_performance` | `DIVIDE([Total Rejected Milk], [Total Milk Procured], 0)` |
| Daily Revenue | `dim_collection_centre` | `SUM('gold sales_daily_summary'[total_revenue])` |
| Cancelled Orders | `dim_collection_centre` | `SUM('gold sales_daily_summary'[cancelled_orders])` |
| Partially Delivered Orders | `dim_collection_centre` | `SUM('gold sales_daily_summary'[partially_delivered_orders])` |
| Total Milk Procured | `gold procurement_quality_summary` | `SUM('gold procurement_quality_summary'[quantity_litres])` |
| Average Revenue per Order | `dim_collection_centre` | `DIVIDE([Total Revenue], [Total Orders], 0)` |
| Total Accepted Milk | `dim_collection_centre` | `CALCULATE(SUM('gold procurement_quality_summary'[quantity_litres]), 'gold procurement_quality_summary'[quality_status] = "Accepted")` |
| Total Production Batches | `dim_collection_centre` | `DISTINCTCOUNT('gold production_performance'[production_id])` |
| Total Raw Milk Processed (L) | `dim_collection_centre` | `SUM('gold production_performance'[total_raw_milk_litres])` |
| Total Finished Product Output | `dim_collection_centre` | `SUM('gold production_performance'[finished_product_quantity])` |
| Finished Output (L) | `dim_collection_centre` | `CALCULATE(SUM('gold production_performance'[finished_product_quantity]), 'gold production_performance'[unit_of_measure] = "L")` |
| Finished Output (kg) | `dim_collection_centre` | `CALCULATE(SUM('gold production_performance'[finished_product_quantity]), 'gold production_performance'[unit_of_measure] = "kg")` |
| Average Production Duration | `dim_collection_centre` | `AVERAGE('gold production_performance'[production_duration_minutes])` |
| Total Finished Output | `dim_collection_centre` | `SUM('gold production_performance'[finished_product_quantity])` |
| Short Product Name | `dim_collection_centre` | See the broken-expression flag below - it is a measure, not a column |
| Measure | `gold sales_product_performance` | None - empty, unused placeholder |
| Measure 2 | `dim_collection_centre` | None - empty, unused placeholder |

Two measures have no expression and are recorded as unused placeholders: `Measure` on `gold sales_product_performance` and `Measure 2` on `dim_collection_centre`. No formula is invented for either.

Two different measure names share the same formula: `Total Finished Product Output` and `Total Finished Output` are both `SUM('gold production_performance'[finished_product_quantity])` on `dim_collection_centre`. Both rows are recorded as they appear in the model. Neither formula applies a unit filter, so use either only with an appropriate unit filter or grouping by `unit_of_measure`.

Multi-line formulas in full, copied exactly:

**Overall Rejection Rate**

```dax
DIVIDE(
    [Total Rejected Milk],
    [Total Milk Procured],
    0
)
```

**Average Revenue per Order**

```dax
DIVIDE(
    [Total Revenue],
    [Total Orders],
    0
)
```

**Total Accepted Milk**

```dax
CALCULATE(
    SUM('gold procurement_quality_summary'[quantity_litres]),
    'gold procurement_quality_summary'[quality_status] = "Accepted"
)
```

**Finished Output (L)**

```dax
CALCULATE(
    SUM('gold production_performance'[finished_product_quantity]),
    'gold production_performance'[unit_of_measure] = "L"
)
```

**Finished Output (kg)**

```dax
CALCULATE(
    SUM('gold production_performance'[finished_product_quantity]),
    'gold production_performance'[unit_of_measure] = "kg"
)
```

### FLAG - Finished Output (L) and Finished Output (kg) filter values
The model data holds `unit_of_measure` values "Litre" and "Kilogram" (full words), verified with pbixray get_table on `gold production_performance` (3,001 Litre batches, 999 Kilogram batches). The two DAX measures above filter `unit_of_measure` = "L" and "kg". Those filters do not match the values in the data, so the two measures would return blank unless the filter matches. This is flagged to check in Power BI, not called wrong. The plain SUM measures (`Total Finished Product Output` and `Total Finished Output`) have no unit filter and are not affected.

### What the verified formulas change against the representative DAX
- Total Milk Procured, Overall Rejection Rate, Total Accepted Milk, Total Production Batches, Total Raw Milk Processed (L), and Average Production Duration match the representative formulas given in the sections above. The representative name "Total Raw Milk Processed" differs from the verified name "Total Raw Milk Processed (L)".
- Total Rejected Milk does NOT match: the representative formula is a CALCULATE on procurement quantity filtered to Rejected, the verified formula is a plain SUM of `gold collection_centre_performance[rejected_milk_litres]`. The representative version must not be quoted as the dashboard formula.
- Overall Rejection Rate is the volume rejection rate, 12.76 percent, not the batch rejection rate, 12.84 percent. The verified Total Rejected Milk and Total Milk Procured are both volume sums, so the rate divides rejected volume by procured volume.

### Short Product Name - calculated column and a flagged measure
`Short Product Name` on `gold sales_product_performance` is a DAX calculated column, not a measure:

```dax
VAR ProductName = 'gold sales_product_performance'[product_name]
RETURN
    IF(
        LEN(ProductName) > 15,
        LEFT(ProductName, 15) & "...",
        ProductName
    )
```

There is also a `Short Product Name` entry in `dax_measures` on `dim_collection_centre`:

```dax
SWITCH(
    TRUE(),
    LEN([product_name]) > 15,
    LEFT([product_name], 15) & "...",
    [product_name]
)
```

Flag, not verified working: `dim_collection_centre` has only three columns (`collection_centre_id`, `centre_name`, `centre_district`) and no `product_name` column, so this expression references a column that does not exist in its host table. It is recorded as a broken or unused expression unless proven otherwise in Power BI. Do not call it a verified working measure.

### Verified DAX calculated columns - date fields
`procurement_date` on `gold procurement_quality_summary`:

```dax
DATE(
    YEAR('gold procurement_quality_summary'[procurement_timestamp]),
    MONTH('gold procurement_quality_summary'[procurement_timestamp]),
    DAY('gold procurement_quality_summary'[procurement_timestamp])
)
```

`production_date` on `gold production_performance`:

```dax
DATE(
    YEAR('gold production_performance'[production_start]),
    MONTH('gold production_performance'[production_start]),
    DAY('gold production_performance'[production_start])
)
```

This RESOLVES the Source 11 dim_date mismatch definitively: `procurement_date` and `production_date` are DAX calculated columns in the Power BI model, derived from the timestamps. They are NOT columns in PostgreSQL - the Source 18 column dump (238 rows) has no `procurement_date` or `production_date` in any Gold table.

### Verified DAX calculated tables - the dimensions
The five dimensions are NOT loaded from PostgreSQL. They are DAX calculated tables derived from the Gold tables. Power Query loads only the 6 Gold tables (see below).

`dim_date`:

```dax
CALENDAR(
    MIN('gold sales_daily_summary'[order_date]),
    MAX('gold sales_daily_summary'[order_date])
)
```

Note: this is NOT the Source 11 reference implementation, which built the date table from a UNION of all three date columns. The model uses only `gold sales_daily_summary[order_date]`.

`dim_product`:

```dax
DISTINCT(
    SELECTCOLUMNS(
        'gold sales_product_performance',
        "product_id", 'gold sales_product_performance'[product_id],
        "product_name", 'gold sales_product_performance'[product_name],
        "category", 'gold sales_product_performance'[category]
    )
)
```

`dim_supplier`:

```dax
DISTINCT(
    SELECTCOLUMNS(
        'gold supplier_performance',
        "supplier_id", 'gold supplier_performance'[supplier_id],
        "supplier_name", 'gold supplier_performance'[supplier_name],
        "supplier_district", 'gold supplier_performance'[supplier_district]
    )
)
```

`dim_collection_centre`:

```dax
DISTINCT(
    SELECTCOLUMNS(
        'gold collection_centre_performance',
        "collection_centre_id", 'gold collection_centre_performance'[collection_centre_id],
        "centre_name", 'gold collection_centre_performance'[centre_name],
        "centre_district", 'gold collection_centre_performance'[centre_district]
    )
)
```

`dim_unit`:

```dax
DISTINCT(
    SELECTCOLUMNS(
        'gold production_performance',
        "Unit", TRIM('gold production_performance'[unit_of_measure])
    )
)
```

### Power Query source - VERIFIED
Only the 6 Gold tables are loaded, each with the same source: `PostgreSQL.Database("localhost:5432", "dairychain")`, Navigation to Schema `gold`, Item = the table name. No dimension table is loaded in Power Query. The source is localhost port 5432, database `dairychain`.

### Relationships - VERIFIED, only one exists
pbixray `relationships` returns exactly one row:

| From table | From column | To table | To column | Active | Cardinality | Filter direction | From key count |
|---|---|---|---|---|---|---|---|
| `gold procurement_quality_summary` | `supplier_id` | `gold supplier_performance` | `supplier_id` | 1 | M:1 | Single | 203 |

This is a MAJOR correction to the documented 10-row intended relationship mapping (Source 11): none of the 10 intended dimension relationships exists in the model. The single relationship that does exist is a fact-to-fact link between the two Gold tables on `supplier_id`; it is not one of the documented dimension relationships, and it is not via `dim_supplier`. The 10 intended relationships that are missing are: `dim_date` to `sales_daily_summary`, `dim_date` to `procurement_quality_summary`, `dim_date` to `production_performance`, `dim_product` to `sales_product_performance`, `dim_product` to `production_performance`, `dim_supplier` to `supplier_performance`, `dim_supplier` to `procurement_quality_summary`, `dim_collection_centre` to `collection_centre_performance`, `dim_collection_centre` to `procurement_quality_summary`, and `dim_unit` to `production_performance`. Consequence: most slicers do not propagate through the model as documented, because there is no relationship for them to follow. Do not invent the missing relationships.

### Anomaly from Source 22 - now EXPLAINED
The Source 22 anomaly (measures defined on `gold collection_centre_performance` and `dim_collection_centre` for sales, milk, and production subjects) is explained by the verified formulas: those tables were used as the measure-host tables in the model, and the formulas reference other tables directly - for example Total Revenue on `gold collection_centre_performance` is a plain SUM of `gold sales_product_performance[total_revenue]`, which works without a relationship because it is a plain SUM. Consequence: without relationships, those measures do not filter by the slicers on other tables. A date, product, or centre slicer has no relationship path to the table the measure sums, so the measure value does not change when that slicer changes.

### Model tables - 16 in total
pbixray `tables` returns 16: the 6 Gold tables, the 5 dimensions, and 5 auto-generated date tables: `DateTableTemplate_e309f29c-2a23-42af-ae89-4348ee0e667e` and four `LocalDateTable_` tables (for `dim_date[Date]`, `gold procurement_quality_summary[procurement_timestamp]`, `gold production_performance[production_start]`, and `gold production_performance[production_end]`). The auto date tables are generated by Power BI, not business tables.

### Verified model-data totals - Source 23 (pbixray get_table)
Totals were computed from the model tables with pbixray get_table and match the README exactly. Full totals are in [pbixray_model_data_totals.txt](../13_Project_Evidence/pbixray_model_data_totals.txt).

- `gold procurement_quality_summary`, 18,000 rows: total milk 8,758,507.64 L, accepted 7,641,260.29 L (15,689 batches), rejected 1,117,247.35 L (2,311 batches), batch rejection 12.84 percent, volume rejection 12.76 percent. Rejection reasons: Low SNF 1,303, Low Fat 513, High Acidity 491, High Temperature 4. Cost mismatches: 1 row (cost_status != MATCH). Date range 2025-11-01 to 2026-10-31, matching the intended period 1 Nov 2025 to 31 Oct 2026.
- `gold sales_daily_summary`, 364 rows: revenue Rs 26,734,294.03, orders 14,000, delivered 11,166, partial 2,227, cancelled 607, quantity ordered 181,804, fulfilled 161,036.41, fulfilment 88.58 percent. Date range 2025-11-02 to 2026-10-31.
- `gold sales_product_performance`, 12 rows: product revenue sums to Rs 26,734,294.03, matching daily. BUT product `total_orders` sums to 28,000, NOT 14,000 - this PROVES the docs warning: do not sum product-level `total_orders`, an order appears once per product. Product revenue by product is in [sales_analysis.md](sales_analysis.md).
- `gold production_performance`, 4,000 rows: total raw milk 2,600,000.0 L, finished Litre 1,484,135.25 L, finished Kilogram 266,416.65 kg, byproduct Litre 466,514.75 L, byproduct kg 402,413.85 kg, Litre batches 3,001, Kilogram batches 999, all 4,000 Completed.
- `gold collection_centre_performance`, 20 rows: total milk 8,758,507.64 L, accepted 7,641,260.29 L, rejected 1,117,247.35 L, batches 18,000. `gold supplier_performance`, 200 rows: total milk 8,758,507.64 L, batches 18,000. All Gold tables reconcile to the same totals.
- Discounts total Rs 250,307.17 in both the daily and product tables.
- Note: procurement has no `unit_of_measure` column; production shift values are "Shift-B (14:00-22:00)" style (Shift-A 1,095, Shift-B 2,175, Shift-C 730), while procurement shift values are "Morning" (9,835) and "Evening" (8,165).

### What Source 23 does NOT prove
No dashboard screenshots and no visual values - none were rendered. KPI values ARE now verified from the model data - see the Verified model-data totals section above. No Gold SQL, no DDL, no Bronze or Silver row counts. The missing relationships are not claimed to exist.

## Example DAX measures (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 9). These measures illustrate calculations supported by the documented Gold tables. They are representative / illustrative, and their source tables and columns are user-supplied. The verified dashboard formulas are now in the Source 23 section above. Most of the representative formulas below match the verified ones; the exceptions are noted below: the representative Total Rejected Milk formula differs from the verified one, and the representative name "Total Raw Milk Processed" differs from the verified name "Total Raw Milk Processed (L)".

### Procurement measures
These measures calculate milk volume, not batch counts.

**Total Accepted Milk**

```dax
Total Accepted Milk =
CALCULATE(
    SUM(
        'gold procurement_quality_summary'[quantity_litres]
    ),
    'gold procurement_quality_summary'[quality_status]
        = "Accepted"
)
```

**Total Rejected Milk**

```dax
Total Rejected Milk =
CALCULATE(
    SUM(
        'gold procurement_quality_summary'[quantity_litres]
    ),
    'gold procurement_quality_summary'[quality_status]
        = "Rejected"
)
```

Source 23: this representative formula differs from the verified dashboard formula, which is `SUM('gold collection_centre_performance'[rejected_milk_litres])` on `gold collection_centre_performance`. Do not quote this representative version as the dashboard formula.

**Overall Rejection Rate**

```dax
Overall Rejection Rate =
DIVIDE(
    [Total Rejected Milk],
    [Total Milk Procured],
    0
)
```

`Total Milk Procured` is used by Overall Rejection Rate but its DAX is not repeated here. It is given in the "Representative DAX measures: procurement rejection rate" section above, from Source 4, section 8. Do not invent a different definition for it here. Overall Rejection Rate is the volume rejection rate, 12.76 percent, not the batch rejection rate, 12.84 percent.

### Production measures
**Total Production Batches**

```dax
Total Production Batches =
DISTINCTCOUNT(
    'gold production_performance'[production_id]
)
```

**Total Raw Milk Processed**

```dax
Total Raw Milk Processed =
SUM(
    'gold production_performance'[total_raw_milk_litres]
)
```

**Average Production Duration**

```dax
Average Production Duration =
AVERAGE(
    'gold production_performance'[production_duration_minutes]
)
```

### Unit-specific output measure
A generic sum of `finished_product_quantity` should not be presented as a combined physical output across litres and kilograms.

```dax
Finished Product Output =
SUM(
    'gold production_performance'[finished_product_quantity]
)
```

Source 23: the model has two measures with this exact formula, `Total Finished Product Output` and `Total Finished Output`, both on `dim_collection_centre`. Use this measure only with an appropriate unit filter or visual grouping by `unit_of_measure`. For more explicit reporting, separate measures can be created for litres and kilograms using CALCULATE with the corresponding unit value. Verify the exact unit strings in the database before writing those measures.

## What cannot be calculated yet
Discounts, sales returns, COGS and operating expenses were not supplied in the README. Gross profit, net revenue and operating profit therefore cannot be calculated from the supplied numbers, and this set does not calculate them. A formula without its inputs is a definition, not a result.

## Unit and zero rules
- Handle zero denominators, missing values, negative quantities, cancelled transactions and inconsistent units before reporting a KPI. A division by zero is a missing result, not zero.
- Never add litre and kg quantities. Report them side by side, with the unit on every number.
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
- [Analytics methodology](analytics_methodology.md)
- [Profitability analysis](profitability_analysis.md)
- [Procurement analysis](procurement_analysis.md)
- [Prompt engineering](../07_AI_Assisted_Development/prompt_engineering.md)
