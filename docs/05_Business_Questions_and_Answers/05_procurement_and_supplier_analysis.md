# Procurement and Supplier Analysis

> Status: VERIFIED

## Purpose
This file answers how much milk was procured, how much was rejected, and what can and cannot be said about suppliers. It is for a manager who needs the rejection problem sized before any supplier is blamed.

## In this file
- How much was procured and rejected?
- Which suppliers contribute most, and are higher prices inefficient?
- PR-01 to PR-05: procurement questions from Source 13
- QL-01 to QL-05: milk quality questions from Source 13

## Business question
How much milk was procured, and how much was accepted or rejected?

## Business context
Procurement is a major dairy cost. Rejected milk was collected and inspected, then could not be used, so it is a direct volume loss.

## Data required
Gold table procurement_quality_summary, 18,000 rows, one per batch. Supplier and centre summaries in supplier_performance, 200 rows, and collection_centre_performance, 20 rows.

## Analytical approach
Count batches by acceptance status, sum volume by status, and calculate the batch rejection rate and the volume rejection rate.

## KPI definitions
Batch rejection rate equals rejected batches divided by total batches, times 100. Volume rejection rate equals rejected volume divided by total volume, times 100.

## Actual result
Procurement batches 18,000. Accepted 15,689. Rejected 2,311. Batch rejection rate 12.84 percent. Total milk 8,758,507.64 L. Rejected milk 1,117,247.35 L. Volume rejection rate 12.76 percent. Accepted milk, calculated: 7,641,260.29 L.

## Direct answer
About 1 in 8 batches and about 1 in 8 litres were rejected. The two rates are close, so rejection was not driven mainly by a few very large batches.

## Business interpretation
Rejection at this level needs investigation, but the totals alone do not name a cause. A supplier, a centre, a district, a reason or a quality measure could explain it, and only the breakdown can tell which.

## Recommendation
Supply the supplier, district and centre breakdowns, the rejection reasons, and the fat and SNF values. Then rank by rejection rate and volume.

## Business impact
Measured impact: none was supplied, so no rupee saving is claimed. Expected benefit: finding the main rejection reason would cut the 1,117,247.35 L rejected volume.

## Evidence
Evidence: user-supplied README, 2026-11-11, procurement section. Gold counts as listed in the README.

## Verification status
VERIFIED


## Business question
Which suppliers contribute the largest procurement volumes, and does a higher price mean a supplier is inefficient?

## Business context
Volume shows who supplies most. Price alone does not show efficiency, because quality, quantity and product specification also matter.

## Data required
Supplier performance table, 200 rows, is named in the README. Supplier names, volumes, prices and quality values were not supplied.

## Analytical approach
Sum quantity and value by supplier, show average price by supplier, and read price together with acceptance rate, fat and SNF. Do not rank a supplier on price alone.

## KPI definitions
Procurement value equals sum of procured quantity x procurement price. Acceptance rate equals accepted batches divided by total batches, times 100.

## Actual result
No supplier breakdown was supplied. Result: PENDING EVIDENCE.

## Direct answer
No supplier ranking or supplier judgement can be given from the supplied numbers.

## Business interpretation
A higher price with higher quality and lower rejection can be better value than a lower price with high rejection. That judgement needs the quality data, so it is not made here.

## Recommendation
Supply supplier rows with quantity, price, acceptance rate, fat, SNF and rejection reason.

## Business impact
Measured impact: none. Expected benefit: a supplier view would show where to renegotiate, support or replace supply.

## Evidence
Evidence: README names supplier_performance with 200 rows. No rows were supplied.

## Verification status
PENDING EVIDENCE

## Business question
PR-01 - What is the total quantity of milk procured?

## Business context
Determine the total milk volume collected through the procurement process. This metric provides an overall view of milk collection volume. Management can use it to understand the scale of procurement activity and compare procurement volumes across reporting periods.

## Data required
Gold table gold.procurement_quality_summary. Required: quantity_litres and procurement records.

## Analytical approach
Aggregate quantity_litres with SUM over all relevant procurement records, unless a specific filter is part of the business question.

## KPI definitions
Total milk procured equals SUM(quantity_litres), in litres.

## Actual result
Total milk procured 8,758,507.64 L. VERIFIED against the model data read with pbixray get_table (Source 23): SUM(quantity_litres) over 18,000 rows equals 8,758,507.64 L, matching the recorded project total exactly.

## Direct answer
The total milk volume is 8,758,507.64 L, verified against the model data (Source 23).

## Business interpretation
This is the scale of procurement. It does not by itself show whether collection was efficient or profitable.

## Recommendation
The total is now verified against the model data (Source 23). Keep the model-data totals file as the evidence record.

## Business impact
Measured impact: none. Expected benefit: a verified total anchors every procurement comparison that follows.

## Evidence
Evidence: Source 13, PR-01, user-supplied 2026-11-11. Recorded total from the user-supplied README, 2026-11-11. Source 23: total VERIFIED against the model data read with pbixray get_table.

## Verification status
VERIFIED


## Business question
PR-02 - Which suppliers contribute the highest milk procurement volume?

## Business context
Identify the suppliers contributing the largest quantity of milk. This supports supplier relationship management, collection planning, and procurement concentration analysis.

## Data required
Gold table gold.supplier_performance. Required: supplier_id, supplier_name, total_milk_litres.

## Analytical approach
Read the supplier-level summary, order by total_milk_litres descending. Do not join the summary to procurement detail unnecessarily before calculating totals.

## KPI definitions
Supplier milk volume equals total_milk_litres for that supplier.

## Actual result
No supplier breakdown was supplied. Result: PENDING EVIDENCE.

## Direct answer
No supplier ranking can be given from the supplied numbers.

## Business interpretation
Without the rows, no supplier can be named as the largest contributor, and no concentration claim can be made.

## Recommendation
Supply the 200 supplier rows with total_milk_litres, then rank them.

## Business impact
Measured impact: none. Expected benefit: a ranking would show where supply is concentrated.

## Evidence
Evidence: Source 13, PR-02, user-supplied 2026-11-11. No rows were supplied.

## Verification status
PENDING EVIDENCE


## Business question
PR-03 - Which supplier districts contribute the most milk?

## Business context
Understand the geographical distribution of milk procurement. This identifies the districts contributing the largest quantities of milk and helps management understand procurement concentration and geographical dependence.

## Data required
Gold table gold.procurement_quality_summary. Required: supplier_district, quantity_litres.

## Analytical approach
Group by supplier_district, sum quantity_litres, calculate each district share of the total, using the same reporting filters for the district total and the overall total.

## KPI definitions
District contribution percentage equals (District Milk Volume / Total Milk Volume) x 100.

## Actual result
Ranking verified from the Page 2 dashboard screenshot (Source 24, 2026-11-11, "Milk Procurement by Supplier District", Sum of quantity_litres by supplier_district), highest to lowest: Sabarkantha, Banaskantha, Kheda, Mehsana, Anand, Satara, Kolhapur, Kolar, Pune, Hisar, Karnal, Mysuru, Rajkot, Mandya, Ludhiana. All 15 district bars fall between about 0.52M and 0.64M litres, read approximately from the chart axis, so the exact per-district litres and shares are NOT readable from the chart and are not claimed here. Result: PARTIALLY VERIFIED (ranking only).

## Direct answer
Sabarkantha contributes the most milk, followed by Banaskantha and Kheda, with Ludhiana lowest of the 15 districts shown. Exact district litres are not supplied.

## Business interpretation
No district can be named as the largest contributor, and no geographical dependence can be claimed.

## Recommendation
Supply procurement rows grouped by supplier_district, then rank by total_milk_litres and share.

## Business impact
Measured impact: none. Expected benefit: a district view would show where collection depends on a small area.

## Evidence
Evidence: Source 13, PR-03, user-supplied 2026-11-11. No rows were supplied. Source 24: the district ranking is verified from the Page 2 screenshot (image-11.png), read from the bar chart; exact per-district litres are not readable from the chart.

## Verification status
PARTIALLY VERIFIED (ranking only)


## Business question
PR-04 - What is the average milk quantity collected per procurement batch?

## Business context
Understand the average volume of milk collected in an individual procurement batch. This describes the typical size of a procurement batch and can be used to compare batch collection patterns across suppliers, districts, or collection centres.

## Data required
Gold table gold.procurement_quality_summary. Required: procurement_id or batch_id, quantity_litres.

## Analytical approach
Use the batch-level grain. If there is exactly one row per batch, the average of quantity_litres is appropriate. If multiple records can represent one batch, aggregate to batch level first.

## KPI definitions
Average quantity per batch equals total milk volume divided by total batches, in litres per batch.

## Actual result
Average quantity per batch about 486.58 L (8,758,507.64 / 18,000). VERIFIED against the model data (Source 23): the same totals come from the model data, so the average is confirmed.

## Direct answer
About 486.58 L per batch, verified against the model data (Source 23).

## Business interpretation
A single average hides variation between suppliers, districts, and centres. Do not use it as the typical batch for any one supplier.

## Recommendation
The average is now verified against the model data (Source 23). A per-supplier, per-district, or per-centre breakdown would still need the rows.

## Business impact
Measured impact: none. Expected benefit: a verified average supports batch-size comparison.

## Evidence
Evidence: Source 13, PR-04, user-supplied 2026-11-11. Totals from the user-supplied README, 2026-11-11. Source 23: totals VERIFIED against the model data.

## Verification status
VERIFIED


## Business question
PR-05 - How does milk procurement vary across shifts?

## Business context
Compare procurement volume and batch activity across collection shifts. This identifies differences in milk collection activity between shifts and can help management understand collection patterns and allocate operational resources.

## Data required
Gold table gold.procurement_quality_summary. Required: shift, procurement_id, quantity_litres.

## Analytical approach
Group by shift. For each shift, count batches, sum quantity_litres, and calculate average quantity per batch. Compare both batch counts and milk volumes: a shift with more batches does not necessarily collect more milk.

## KPI definitions
Total batches per shift equals COUNT of procurement records in that shift. Total milk per shift equals SUM(quantity_litres) in that shift. Average quantity per batch equals total milk divided by total batches in that shift.

## Actual result
Shift breakdown VERIFIED from the model data read with pbixray get_table (Source 23). Procurement shift values are "Morning" and "Evening".

| Shift | Batches | Total milk (L) | Average per batch (L) | Rejected batches | Rejection rate |
|---|---:|---:|---:|---:|---:|
| Morning | 9,835 | 4,801,175.33 | 488.17 | 1,267 | 12.88 percent |
| Evening | 8,165 | 3,957,332.31 | 484.67 | 1,044 | 12.79 percent |
| **Total** | **18,000** | **8,758,507.64** | **486.58** | **2,311** | **12.84 percent** |

## Direct answer
Morning collects more milk than Evening: 4,801,175.33 L from 9,835 batches, against 3,957,332.31 L from 8,165 batches. Rejection rates are close: 12.88 percent in the Morning, 12.79 percent in the Evening.

## Business interpretation
Morning is the busier shift by both batches and milk, but the rejection rate barely differs between shifts, so shift is not the main rejection driver. The average batch size is also close: 488.17 L in the Morning against 484.67 L in the Evening.

## Recommendation
Staff and transport can be planned around the Morning peak, but the rejection fix is not a shift fix - use QL-04 (rejection reasons) instead.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: the shift view shows where collection effort is concentrated.

## Evidence
Evidence: Source 13, PR-05, user-supplied 2026-11-11. Shift rows now VERIFIED from the model data read with pbixray get_table (Source 23).

## Verification status
VERIFIED


## Business question
QL-01 - What percentage of procurement batches are rejected?

## Business context
Measure the proportion of procurement batches that fail the quality acceptance criteria. This provides an overview of procurement batch acceptance performance. A higher rejection percentage indicates that a larger proportion of collected batches are failing the applicable quality criteria.

## Data required
Gold table gold.procurement_quality_summary. Required: procurement_id, quality_status.

## Analytical approach
Count total batches, count rejected batches and accepted batches by quality_status, then divide rejected by total.

## KPI definitions
Batch rejection rate equals (Rejected Batches / Total Batches) x 100.

## Actual result
Total batches 18,000. Accepted batches 15,689. Rejected batches 2,311. Batch rejection rate 12.84 percent.

## Direct answer
12.84 percent of procurement batches were rejected.

## Business interpretation
About 1 in 8 batches failed quality acceptance. The totals alone do not name a cause.

## Recommendation
Use the breakdowns in QL-02 to QL-05 to find which suppliers, centres, reasons, or quality measures explain the rejections.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: finding the main rejection cause would cut the rejected volume.

## Evidence
Evidence: Source 13, QL-01, user-supplied 2026-11-11, with recorded project reference 18,000 / 15,689 / 2,311 / 12.84 percent. Also in the user-supplied README, 2026-11-11. Source 23: totals VERIFIED against the model data read with pbixray get_table (18,000 batches, 15,689 accepted, 2,311 rejected, 12.84 percent; volume 8,758,507.64 L procured, 1,117,247.35 L rejected, 12.76 percent).

## Verification status
VERIFIED


## Business question
QL-02 - Which suppliers have the highest rejection rates?

## Business context
Identify suppliers with higher milk rejection levels. This can support supplier-level quality investigations and targeted improvements.

## Data required
Gold tables gold.supplier_performance and gold.procurement_quality_summary. Required: supplier_id, supplier_name, total_batches, rejected batch count, accepted batch count, total milk quantity, rejected milk quantity.

## Analytical approach
Rank suppliers by rejection rate. Be explicit about which rejection metric is being compared: batch rejection rate or milk-volume rejection rate. Do not assume that the existing rejection_rate_percentage column uses the batch-based definition. Verify its underlying SQL calculation before comparing it with the independently calculated batch rejection rate.

## KPI definitions
Supplier batch rejection rate equals (Rejected Batches / Total Batches) x 100. Supplier milk-volume rejection rate equals (Rejected Milk Volume / Total Milk Volume) x 100.

## Actual result
No supplier rejection breakdown was supplied. Result: PENDING EVIDENCE.

## Direct answer
No supplier rejection ranking can be given from the supplied numbers.

## Business interpretation
No supplier can be blamed for rejection yet. A supplier with a high volume rate and a low batch rate is a different problem from one with a high batch rate.

## Recommendation
Supply supplier rows with batch counts and milk volumes by status, verify what rejection_rate_percentage measures, then rank by both rates.

## Business impact
Measured impact: none. Expected benefit: a supplier ranking would show where quality investigation should start.

## Evidence
Evidence: Source 13, QL-02, user-supplied 2026-11-11. No rows were supplied.

## Verification status
PENDING EVIDENCE


## Business question
QL-03 - Which collection centres have the highest rejected milk volume?

## Business context
Identify collection centres contributing the largest rejected milk quantities. Management can investigate whether the volumes are related to collection processes, handling, storage, or supplier quality patterns.

## Data required
Gold tables gold.collection_centre_performance and gold.procurement_quality_summary. Required: collection_centre_id, centre_name, rejected_milk_litres, total milk volume.

## Analytical approach
Rank centres by rejected_milk_litres, and read rejected volume together with rejection percentage. A large centre may have a high rejected volume but a lower rejection percentage than a smaller centre. Both metrics should be considered when comparing centres.

## KPI definitions
Centre rejection percentage equals (Rejected Milk Volume / Total Milk Volume) x 100. Rejected volume equals rejected_milk_litres.

## Actual result
No centre breakdown was supplied. Result: PENDING EVIDENCE.

## Direct answer
No collection-centre ranking can be given from the supplied numbers.

## Business interpretation
Volume alone does not prove a centre is worse. A large centre naturally rejects more litres even at a low rate.

## Recommendation
Supply the 20 centre rows with total and rejected milk, then rank by both volume and percentage.

## Business impact
Measured impact: none. Expected benefit: a centre view would show whether rejection is concentrated in a few centres.

## Evidence
Evidence: Source 13, QL-03, user-supplied 2026-11-11. No rows were supplied.

## Verification status
PENDING EVIDENCE


## Business question
QL-04 - What are the most common reasons for milk rejection?

## Business context
Understand the reasons associated with rejected procurement batches. This identifies recurring rejection reasons and can help management prioritise quality-control improvements and investigate recurring problems.

## Data required
Gold table gold.procurement_quality_summary. Required: rejection_reason, procurement_id, quality_status.

## Analytical approach
Include only rejected records. Group by rejection_reason, count rejected batches, and calculate each reason share of all rejections. Missing rejection reasons should not automatically be treated as a real rejection category. Their treatment should be documented separately.

## KPI definitions
Percentage of rejections equals (Rejected batches for that reason / All rejected batches) x 100.

## Actual result
Rejection-reason breakdown VERIFIED from the model data read with pbixray get_table (Source 23). It matches the notebook breakdown (Source 15, cells 43-44).

| Rejection reason | Batches | Share of rejections |
|---|---:|---:|
| Low SNF (<8.2%) | 1,303 | 56.38 percent |
| Low Fat (<3.2%) | 513 | 22.20 percent |
| High Acidity (>0.17%) | 491 | 21.25 percent |
| High Temperature (>8.5C) | 4 | 0.17 percent |
| **Total rejected** | **2,311** | **100.00 percent** |

## Direct answer
Low SNF is the most common rejection reason, 1,303 batches, 56.38 percent of all rejections.

## Business interpretation
More than half of all rejections are Low SNF. Low Fat and High Acidity together account for another 43.45 percent. High Temperature is negligible at 4 batches. The first quality fix to try is the SNF problem, not temperature control.

## Recommendation
Investigate why SNF runs low - feed, breed, collection delay, or testing - starting with the centres and suppliers with the most Low SNF rejections. That breakdown by centre and supplier is still PENDING EVIDENCE.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: fixing the SNF cause would cut the largest share of the 2,311 rejected batches.

## Evidence
Evidence: Source 13, QL-04, user-supplied 2026-11-11. Breakdown now VERIFIED from the model data read with pbixray get_table (Source 23); it matches the notebook (Source 15).

## Verification status
VERIFIED


## Business question
QL-05 - How do average fat and SNF levels differ between accepted and rejected milk?

## Business context
Compare milk quality measurements between accepted and rejected procurement batches. This provides a comparison of fat and SNF measurements across quality outcomes and can help investigate whether certain quality measurements are associated with higher rejection levels.

## Data required
Gold table gold.procurement_quality_summary. Required: quality_status, fat_percentage, snf_percentage.

## Analytical approach
Calculate average fat_percentage and average snf_percentage separately for accepted batches and for rejected batches. Missing measurement values should be considered when interpreting the results. An average calculated from available measurements may not represent every procurement batch.

## KPI definitions
Average fat percentage equals AVG(fat_percentage) within each quality_status group. Average SNF percentage equals AVG(snf_percentage) within each quality_status group.

## Actual result
No average fat or SNF breakdown was supplied. Result: PENDING EVIDENCE. The Page 2 dashboard screenshot (Source 24, 2026-11-11, "Average Fat & SNF by Quality Status") does NOT answer this question: it plots SUMS of snf_percentage and fat_percentage by quality_status (Accepted SNF about 138K and fat about 77K; Rejected SNF about 20K and fat about 11K), not averages, even though the title says "Average". Summing a percentage across batches has no business meaning, and the accepted sums are larger mainly because there are 15,689 accepted batches against 2,311 rejected ones. Do not use those numbers as average fat or SNF.

## Direct answer
No fat or SNF difference between accepted and rejected milk can be given from the supplied numbers. The chart that looks like an answer is a sum, not an average.

## Business interpretation
No quality measurement can be linked to rejection yet. An association, once measured, would still not prove a cause.

## Recommendation
Supply average fat and SNF by quality_status, with the count of missing measurements in each group.

## Business impact
Measured impact: none. Expected benefit: a clear fat or SNF gap would point the quality investigation at a measurement, not a guess.

## Evidence
Evidence: Source 13, QL-05, user-supplied 2026-11-11. No rows were supplied. Source 24: the Page 2 screenshot shows a chart titled "Average Fat & SNF by Quality Status", but its subtitle says "Sum of snf_percentage and Sum of fat_percentage", so it plots sums, not the averages this question asks for.

## Verification status
PENDING EVIDENCE (averages still not supplied; the chart sums are recorded as a flag, not as an answer)

## Next step / Related files
- Procurement analysis](../04_Business_Analytics/procurement_analysis.md)
- KPI definitions](../04_Business_Analytics/kpi_definitions.md)
- Production efficiency](06_production_efficiency.md)
