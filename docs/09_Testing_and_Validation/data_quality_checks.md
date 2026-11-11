# Data Quality Checks


## Purpose
This file answers which data quality checks DairyChain must run and what each check proves. It is for a reader who needs to trust the data behind a Gold number. Its source for Power BI testing is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 7.6, and for reconciliation the same document, section 8.

## In this file
- Checks
- Power BI testing
- Relationship validation checklist (Source 11)
- Troubleshooting common data model problems (Source 11)
- Reconciliation considerations
- What a failed check means
- Notes

## Checks
- Record counts across processing layers.
- Missing values and duplicate records.
- Data type consistency.
- Referential integrity.
- Invalid or unexpected values.
- Procurement cost reconciliation.
- Aggregation accuracy.
- Unit-of-measure consistency.
- SQL output check.
- Power BI measure and filter validation.

## Power BI testing
Power BI should be validated independently of the visual design. Check the following:

- KPI values against PostgreSQL.
- Correct aggregation of revenue and quantities.
- Relationship cardinality and filter direction.
- Date slicer behaviour.
- Product and category slicer behaviour.
- Whether only the intended visuals respond to a slicer.
- Whether production outputs in litres and kilograms remain separate.
- Whether percentage measures use the correct numerator and denominator.

A visually correct dashboard is not necessarily analytically correct.

## Relationship validation checklist (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 10). Before considering the Power BI model complete, check the following. UPDATED by Source 23 (pbixray): the model has now been read, so the items marked [x] below are shown from the model, the item marked FAILED is shown as not satisfied, and the remaining items still need checking in Power BI.

### Dimension uniqueness
- [x] `dim_date[Date]` contains unique dates. (Source 23: dim_date is a CALENDAR table, so dates are unique by construction.)
- [x] `dim_product[product_id]` is unique. (Source 23: dim_product is DISTINCT(SELECTCOLUMNS(...)), so product_id is unique by construction.)
- [x] `dim_supplier[supplier_id]` is unique. (Source 23: dim_supplier is DISTINCT(SELECTCOLUMNS(...)), so supplier_id is unique by construction.)
- [x] `dim_collection_centre[collection_centre_id]` is unique. (Source 23: dim_collection_centre is DISTINCT(SELECTCOLUMNS(...)), so collection_centre_id is unique by construction.)
- [x] `dim_unit[Unit]` is unique. (Source 23: dim_unit is DISTINCT(SELECTCOLUMNS(...)), so Unit is unique by construction; the model data holds two values, "Litre" and "Kilogram".)

### Relationships
- [ ] Relationship keys use compatible data types.
- [ ] Cardinality matches actual uniqueness.
- [x] Relationships are active where required. (Source 23: the single relationship in the model is active, IsActive 1.)
- [x] Filter direction is intentional. (Source 23: the single relationship has CrossFilteringBehavior Single.)
- [ ] No unnecessary fact-to-fact relationships exist. FAILED (Source 23): the only relationship in the model IS a fact-to-fact relationship, `gold procurement_quality_summary[supplier_id]` to `gold supplier_performance[supplier_id]`.
- [ ] No unintended ambiguous filter paths exist.

### Slicers
- [ ] Date slicers filter the intended pages and visuals.
- [ ] Product slicers affect relevant product visuals.
- [ ] Supplier filters affect procurement and supplier analysis.
- [ ] Collection-centre filters affect the intended procurement analysis.
- [ ] Unit slicers separate production measurements.
- [ ] Unrelated visuals do not change unexpectedly.

### Measures
- [x] Batch counts use batch-level identifiers. (Source 23: Total Production Batches = DISTINCTCOUNT('gold production_performance'[production_id]).)
- [x] Overall order counts do not double-count product-level orders. (Source 23: Total Orders = SUM('gold sales_daily_summary'[total_orders]) = 14,000; product `total_orders` sums to 28,000, so the measure correctly uses the daily grain, not the product grain.)
- [x] Revenue is not counted twice across summary tables. (Source 23: Total Revenue = SUM('gold sales_product_performance'[total_revenue]) and Daily Revenue = SUM('gold sales_daily_summary'[total_revenue]); each measure sums one grain only, and both grains total Rs 26,734,294.03.)
- [x] Rejection percentages use the correct metric definition. (Source 23: Overall Rejection Rate = DIVIDE([Total Rejected Milk], [Total Milk Procured], 0), a volume rate, 12.76 percent, not the batch rate, 12.84 percent.)
- [x] Production units are kept separate. (Source 23: Finished Output (L) and Finished Output (kg) filter by unit_of_measure; see the L/kg flag in kpi_definitions.md - the filters use "L" and "kg" while the data holds "Litre" and "Kilogram".)
- [ ] Average selling price is correctly defined.

## Troubleshooting common data model problems (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 11).

| Problem | Possible cause | What to inspect |
|---|---|---|
| Slicer does not filter a visual | No active relationship or missing filter path | Model relationships and visual interactions |
| KPI total is too high | Duplicate rows or incorrect aggregation | Table grain, joins, and measure |
| Product selection does not affect daily revenue | Daily summary has no product key | Reporting grain and model relationships |
| Date slicer does not filter a table | Missing or incorrect date relationship | Date columns and relationship settings |
| Unit slicer displays only one unit | Incorrect dimension values or relationship | Distinct unit values and data types |
| Revenue differs between pages | Different source tables, filters, or definitions | Reconcile both calculations in PostgreSQL |
| Batch count is incorrect | Counting summary rows or using non-unique fields | Correct batch identifier and aggregation |

## Reconciliation considerations
Reconciliation should consider row counts, unique identifiers, total milk volume, accepted and rejected quantities, production output by unit, total revenue, and order counts. The comparison must use the same filters, date ranges, and business definitions on both sides. See [integration_testing.md](integration_testing.md) for the stage-by-stage reconciliation checks.

## What a failed check means
A failed check means the data or the query is wrong, not that the check is wrong. Find the cause at the right layer, fix it, and run the check again. Record the count of rows affected by every fix.

## Results from the notebook - Source 15
Full table with cell numbers is in [test_results.md](test_results.md). Headline results, all from stored outputs:

- Duplicate rows: 0 in all 10 datasets, and 0 duplicate keys.
- Missing values: 0 in suppliers, procurement and order lines; 1 missing temperature in quality tests (QCT-000250); 607 missing delivery dates in sales orders, all Cancelled.
- NULL checks in the database (Source 25, given by the user, 2026-11-11): NULL values were checked in 8 important columns. The one missing temperature value (QCT-000250) was confirmed to originate in Bronze and remain NULL in Silver, so it is a source-data gap carried through the layers, not a cleaning error.
- Referential integrity: 0 invalid references across the 8 relationships checked in cell 83.
- Procurement cost: 1 mismatch (PRC-001000, difference 6,657.17), 17,999 valid.
- Procurement-quality status match: 0 mismatches in 18,000 records.
- Rejection-rule consistency: 0 inconsistent records for all four rules.
- Total milk: 8,758,507.64 L, rejected 1,117,247.35 L, 12.76 percent, matching the README.

## Notes
. The data-quality checks the notebook runs are from stored outputs. The checks above are the list from the README, stated as method, plus the notebook results in this section.

## Next step / Related files
- [Testing strategy](testing_strategy.md)
- [Data validation](../03_Data_Engineering/data_validation.md)
- [Test results](test_results.md)
