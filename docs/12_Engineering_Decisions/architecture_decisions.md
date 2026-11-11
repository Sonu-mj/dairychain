# Architecture Decisions


## Purpose
This file answers why DairyChain uses Bronze, Silver and Gold layers and a Power BI report on top. It is for a reader who needs the layering reason, not only the layer names.

## In this file
- The choice
- Why three layers
- Why Power BI on top
- Technical decision example: keeping production measurement units separate
- Trade-offs

## The choice
DairyChain uses a layered design: CSV to Python to PostgreSQL, then Bronze, Silver, Gold, then Power BI. Each layer has one job and one grain, so a fault can be found at the layer where it happened.

## Why three layers
- Bronze keeps the source as it arrived, so a cleaning error can be checked against the original.
- Silver keeps cleaned data, so Gold does not have to re-clean raw data for every report.
- Gold keeps report-ready summaries, so Power BI does not have to re-aggregate raw batches for every visual.

## Why Power BI on top
Power BI presents Gold tables as four report pages, with DAX measures for the calculations the report needs. It is a presentation layer, not a replacement for the Gold tables. A number that is wrong in Gold will be wrong in Power BI, so Gold is checked first.

## Technical decision example: keeping production measurement units separate
Source: Decision Log, section 5, user-supplied 2026-11-11. Do not enter this as an AI suggestion decision unless the original AI interaction confirms that AI proposed the approach. Table and column names below are user-supplied. A.pbix file has now been supplied (Source 22) and confirms the dim_unit table exists in the model, and Source 23 (pbixray) has now shown the DAX example as the model formula.

### Problem
The DairyChain production data contains finished-product quantities measured in litres and kilograms. Combining these quantities into one total would create a misleading metric because they represent different measurement units.

### Technical decision
Production quantities should be analysed separately by unit of measure.

### Implementation reference
A Power BI dimension was created to represent the distinct units:

```dax
dim_unit =
DISTINCT(
    SELECTCOLUMNS(
        'gold production_performance',
        "Unit",
        TRIM(
            'gold production_performance'[unit_of_measure]
        )
    )
)
```

The intended relationship is:

`dim_unit[Unit]` to `gold production_performance[unit_of_measure]`

With one-to-many cardinality and single-direction filtering.

### Reason
A total of 100 litres plus 100 kilograms is not a meaningful production quantity. The unit dimension allows production analysis to be filtered by the appropriate unit.

### Checks
- [x] Confirm that the distinct unit values are correct. from Source 23: the model data holds "Litre" and "Kilogram".
- [ ] Confirm the relationship is active and has the intended cardinality. The only relationship in the model is `gold procurement_quality_summary[supplier_id]` to `gold supplier_performance[supplier_id]`.
- [ ] Check that the unit slicer filters the intended production visuals.
- [x] Confirm that litre and kilogram totals are not combined. from Source 23: Finished Output (L) and Finished Output (kg) filter by unit, and the docs keep litre and kg totals separate.

Decision classification: technical design example. UPDATED by Source 23: the DAX is shown as the model formula, the unit values are shown, and litre/kg separation is shown.

## Trade-offs
Three layers cost more work than one layer, because each layer needs its own validation. The benefit is that a wrong number can be traced to its layer, and a fix in one layer does not force a rebuild of the whole pipeline from the source files.

## Next step / Related files
- [Database decisions](database_decisions.md)
- [Bronze Silver Gold](../03_Data_Engineering/bronze_silver_gold_layers.md)
- [Rejected approaches](rejected_approaches.md)
- [AI decision log](../07_AI_Assisted_Development/ai_task_log/actual_development_tasks.md)
