# Production Efficiency and Yield

> Status: VERIFIED

## Purpose
This file answers what production made and why yield cannot be calculated from the supplied numbers. It is for a manager who needs efficiency, not output alone.

## In this file
- How much was produced?
- What is the production yield, and where does material loss occur?
- PRD-01 to PRD-04: production questions from Source 13

## Business question
How much finished product and byproduct was produced?

## Business context
Production output is the saleable result of accepted milk. Byproduct output matters too, because it is a second output from the same input.

## Data required
Gold table production_performance, 4,000 rows, one per batch. Output is split by unit in the README.

## Analytical approach
Sum finished output and byproduct output separately for litre-based batches and for kg-based batches. Never add litres to kg.

## KPI definitions
No yield formula is used here, because input was not supplied. Output totals are sums by unit.

## Actual result
Production batches 4,000. Finished litre-based 1,484,135.25 L. Byproduct litre-based 466,514.75 L. Finished kg-based 266,416.65 kg. Byproduct kg-based 402,413.85 kg. No combined total is given.

## Direct answer
Production made finished product and byproduct in both units. The split by unit is the correct way to read the result.

## Business interpretation
Output without input is a volume result, not an efficiency result. A large output can come from a large input, so do not call a batch efficient from output alone.

## Recommendation
Supply raw milk input per batch, in the same unit as its output, plus product and shift.

## Business impact
Measured impact: none. Expected benefit: input data would allow yield and loss to be measured.

## Evidence
Evidence: user-supplied README, 2026-11-11, production section.

## Verification status
VERIFIED


## Business question
What is the production yield, and where does material loss occur?

## Business context
Yield shows how much finished product comes from the raw milk that entered a batch. Loss shows where material went that did not become finished product.

## Data required
Raw milk input per batch was not supplied. Finished output was supplied, split by unit. Byproduct output was supplied, split by unit.

## Analytical approach
Calculate yield as finished output divided by relevant raw milk input, times 100, in the same unit, per batch, then by product and shift. Loss is input minus finished output minus byproduct, where the business definition supports that split.

## KPI definitions
Production yield equals (Finished output / Relevant raw material input) x 100.

## Actual result
No yield or loss result was supplied. Result: PENDING EVIDENCE.

## Direct answer
Yield and material loss cannot be calculated from the supplied numbers.

## Business interpretation
Do not estimate yield from the output totals alone. The input total is missing, and any estimate would be invented.

## Recommendation
Supply raw milk input per batch, product, shift and duration. Then calculate yield, list low-yield batches, and check whether a product or shift explains them.

## Business impact
Measured impact: none. Expected benefit: yield by batch would show where material is lost and where to investigate first.

## Evidence
Evidence: README gives output only. No input rows were supplied.

## Verification status
PENDING EVIDENCE

## Business question
PRD-01 - How many production batches were processed?

## Business context
Determine the total number of production batches recorded. This provides an overall indication of production activity. It can also be analysed by product and shift to understand how production is distributed.

## Data required
Gold table gold.production_performance. Required: production_id.

## Analytical approach
Use the distinct count of production_id when measuring the number of unique batches.

## KPI definitions
Total production batches equals COUNT(DISTINCT production_id).

## Actual result
4,000 production batches: 3,001 litre-based and 999 kg-based, all with production_status Completed. Source 23 verified the split and the status from the model data.

## Direct answer
4,000 production batches were processed.

## Business interpretation
This is an activity total, not an efficiency result. It does not say how much was made per batch.

## Recommendation
Break the 4,000 batches down by product and shift once those rows are supplied.

## Business impact
Measured impact: none. Expected benefit: a breakdown would show where production activity is concentrated.

## Evidence
Evidence: Source 13, PRD-01, user-supplied 2026-11-11, recorded project reference 4,000. Also in the user-supplied README, 2026-11-11. Source 23: batch count, unit split, and Completed status VERIFIED against the model data read with pbixray get_table.

## Verification status
VERIFIED


## Business question
PRD-02 - How much raw milk was processed during production?

## Business context
Measure the total milk input used across production batches. This indicates the total raw milk input associated with production and provides a basis for investigating production volumes and the relationship between raw material input and finished output.

## Data required
Gold table gold.production_performance. Required: total_raw_milk_litres.

## Analytical approach
Use SUM(total_raw_milk_litres) over the intended production records. This metric should not be confused with total milk procured. Procurement and production represent different stages of the supply chain.

## KPI definitions
Total raw milk processed equals SUM(total_raw_milk_litres), in litres.

## Actual result
Total raw milk processed 2,600,000.0 L (SUM(total_raw_milk_litres) over 4,000 batches, Source 23 model data). Split: litre batches 1,950,650.0 L, kg batches 649,350.0 L. This is NOT the same as total milk procured (8,758,507.64 L) - procurement and production are different stages.

## Direct answer
2,600,000.0 L of raw milk was processed.

## Business interpretation
The input total is now known, so the litre side can be checked: finished 1,484,135.25 L plus byproduct 466,514.75 L equals the litre-batch input exactly (1,950,650.0 L), so no litre loss is shown. The kg side cannot be compared the same way, because its outputs are in kg while its input is recorded in litres, so a single yield figure still cannot be calculated.

## Recommendation
Supply a density conversion, or record kg-batch input in kg, if a kg yield is needed. Until then, do not quote a single yield percentage.

## Business impact
Measured impact: none. Expected benefit: the input total unlocks the litre-side check and shows where a yield figure is still blocked.

## Evidence
Evidence: Source 13, PRD-02, user-supplied 2026-11-11. Total VERIFIED from the model data read with pbixray get_table (Source 23).

## Verification status
VERIFIED


## Business question
PRD-03 - What is the average production duration per batch?

## Business context
Understand the average time taken to complete production batches. This provides an overview of production processing time, can help identify operational differences, and supports comparisons across products or shifts.

## Data required
Gold table gold.production_performance. Required: production_id, production_duration_minutes.

## Analytical approach
Use the production-batch grain and investigate missing or invalid duration values. An average across all batches may not represent the typical duration of every product, because different products may require different processing times.

## KPI definitions
Average production duration equals AVG(production_duration_minutes), in minutes per batch.

## Actual result
Average production duration 135.03 minutes per batch (mean of production_duration_minutes over 4,000 batches, Source 23 model data). Range: 29.98 to 180.00 minutes. Duration means by product range from 133.48 minutes (Full Cream Milk) to 136.87 minutes (Fresh Malai Paneer), so no product stands out as much slower or faster.

## Direct answer
135.03 minutes per batch on average.

## Business interpretation
Durations are tightly grouped by product, so duration alone does not explain any production difference. The overall mean hides little variation.

## Recommendation
Supply duration by batch with shift if a shift comparison is needed.

## Business impact
Measured impact: none. Expected benefit: a duration view would show where processing time is longest.

## Evidence
Evidence: Source 13, PRD-03, user-supplied 2026-11-11. Mean and range computed from the model data read with pbixray get_table (Source 23).

## Verification status
VERIFIED


## Business question
PRD-04 - How much finished product is produced by each product and unit?

## Business context
Compare finished product output across products while maintaining correct measurement units. This helps management understand the production output associated with different products and can identify products with higher output volumes within the same measurement unit.

## Data required
Gold table gold.production_performance. Required: product_id, product_name, finished_product_quantity, unit_of_measure.

## Analytical approach
Group results by product_name and unit_of_measure. Compare quantities only within compatible units. DairyChain production output includes litres and kilograms, and these units must be analysed separately. A total of 1,000 litres and 500 kilograms must not be presented as a combined total of 1,500 units.

## KPI definitions
Finished output by product and unit equals SUM(finished_product_quantity) grouped by product_name and unit_of_measure.

## Actual result
Finished output by product and unit is now VERIFIED from the model data read with pbixray get_table (Source 23).

| Product | Unit | Finished output | Byproduct output |
|---|---|---:|---:|
| Classic Set Curd | Kilogram | 216,253.53 kg | 6,689.97 kg |
| Double Toned Milk | Litre | 211,672.50 L | 5,427.50 L |
| Elaichi Flavoured Milk | Litre | 209,956.50 L | 6,493.50 L |
| Fresh Dairy Cream | Litre | 10,822.50 L | 205,627.50 L |
| Fresh Malai Paneer | Kilogram | 40,129.83 kg | 182,813.67 kg |
| Full Cream Milk | Litre | 211,672.50 L | 5,427.50 L |
| Pasteurised Table Butter | Kilogram | 10,033.29 kg | 212,910.21 kg |
| Probiotic Lassi | Litre | 203,463.00 L | 12,987.00 L |
| Pure Cow and Buffalo Ghee | Litre | 9,740.25 L | 206,709.75 L |
| Spiced Masala Buttermilk | Litre | 203,463.00 L | 12,987.00 L |
| Standardised Milk | Litre | 211,672.50 L | 5,427.50 L |
| Toned Milk | Litre | 211,672.50 L | 5,427.50 L |
| **Total** | | **1,484,135.25 L and 266,416.65 kg** | **466,514.75 L and 402,413.85 kg** |

## Direct answer
Finished output by product and unit is in the table above. The highest litre output is shared by four milk products at 211,672.50 L each (Double Toned Milk, Full Cream Milk, Standardised Milk, Toned Milk); the highest kg output is Classic Set Curd at 216,253.53 kg.

## Business interpretation
Output is spread evenly across the milk products, so no single milk product drives litre output. Note the byproduct pattern: products with low finished output carry high byproduct (Fresh Dairy Cream, Pure Cow and Buffalo Ghee, Pasteurised Table Butter), which is the data as recorded, not an interpretation of efficiency.

## Recommendation
Use this table with units kept separate. Do not add a litre total to a kg total.

## Business impact
Measured impact: none. Expected benefit: a per-product view shows which products drive output.

## Evidence
Evidence: Source 13, PRD-04, user-supplied 2026-11-11. Totals from the user-supplied README, 2026-11-11. Per-product rows now VERIFIED from the model data read with pbixray get_table (Source 23).

## Verification status
VERIFIED

## Next step / Related files
- Production analysis](../04_Business_Analytics/production_analysis.md)
- KPI definitions](../04_Business_Analytics/kpi_definitions.md)
- Procurement analysis](05_procurement_and_supplier_analysis.md)
