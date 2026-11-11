# Business Questions and SQL Solutions - 15 Questions Answered

## Purpose
This file answers 15 business questions from the project's own data. Each question has a plain-words answer, the method used, a PostgreSQL query that reproduces the answer from the Silver tables, the exact figures from the dataset, and what the figures mean for the business. The source is the user-supplied PDF "DairyChain Business Questions and SQL Solutions" (Source 29, 2026-11-11).

## In this file
- Conclusion: the problem, what we solved, and how we solved it
- How the answers were calculated, and how the SQL is to be read
- Questions 1 to 15, each with a plain-words answer, method, SQL query, dataset answer, and business meaning
- Consolidated findings

## How the answers were calculated
The answers were calculated from the 10 CSV files with Python and Pandas. The SQL queries in this file are the PostgreSQL equivalent of each calculation, written against the Silver-layer table names (for example, silver.milk_procurement). The SQL examples are reproducible PostgreSQL queries and are not represented as executed database output. To reproduce an answer in PostgreSQL, connect to the dairychain database, confirm the Silver table names and column types, run the query, and compare the output with the figures given here. The figures describe this project dataset only. They are not external market prices, factory benchmarks, or proof of real-world dairy performance.

## Conclusion

### The problem
A dairy business buys milk from 200 suppliers through 20 collection centres, processes it into 12 products, and sells it to customers. But it could not see where its money was going. It did not know which suppliers it was paying the most, whether the price it paid matched the quality it received, why milk was being rejected, which collection centres were losing the most milk, how much finished product each batch of raw milk produced, or which products and orders were actually performing. The data existed in 10 separate files, but nobody had turned it into answers a manager could act on.

### What we solved
The project turns 99,584 records into answers. Fifteen business questions are answered, covering supplier spend and quality, purchase rates, cost accuracy, rejection reasons, collection centre performance, production yield, sales revenue, and order fulfilment. The headline finding is that rejected milk cost Rs 5.99 crore out of Rs 48.19 crore of milk purchased, and Low SNF alone cost Rs 3.44 crore, more than half of all rejected milk cost. Other answers point the same way: one supplier takes the largest spend because it supplies the most milk, the best-quality supplier costs only about Rs 0.86 more per litre, one cost record is wrong by Rs 6,657.17, and 2,834 of 14,000 orders were not fully fulfilled.

### How we solved it
The 10 CSV files were read with Python and Pandas, the answers were calculated from them, and a PostgreSQL query is given for each question so the same answer can be reproduced from the Silver tables. The data was organised into Bronze, Silver, and Gold layers in PostgreSQL, and 4 Power BI pages with 21 DAX measures were built on the Gold tables so the answers can also be seen as dashboards. Each question states its tables, its join keys, and its calculation rule, so a reader can follow the answer from the raw file to the final figure.

## Question 1 - Which suppliers account for the highest milk-purchasing spend?

### Answer in plain words
Ganesh Jadhav Dairy is the supplier the business pays the most. It supplied 112 batches of milk, 57,396.83 litres in total, and the business paid Rs 3,175,190.94 for it, about Rs 31.75 lakh. This supplier is first on spend mainly because it supplies the largest volume of milk, not because it charges the highest price per litre. The next question checks the price per litre separately, because total spend and price per litre are two different questions.

### How we found it
Group the procurement rows by supplier, add the litres, and recalculate each row cost as quantity in litres multiplied by the purchase rate per litre. Join the supplier names so the ranking shows names, then order by the recalculated spend.

```sql
SELECT
    s.supplier_id,
    s.supplier_name,
    COUNT(*) AS procurement_records,
    ROUND(SUM(p.quantity_litres), 2) AS milk_litres,
    ROUND(SUM(ROUND(
        p.quantity_litres * p.purchase_rate_per_litre, 2
    )), 2) AS validated_spend_inr
FROM silver.milk_procurement AS p
JOIN silver.suppliers AS s
  ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.supplier_name
ORDER BY validated_spend_inr DESC
LIMIT 10;
```

### Answer

> **Answer**
>
> - **Ganesh Jadhav Dairy (SUP-0132)** ranks first: 112 procurement records, 57,396.83 litres, Rs 3,175,190.94 (about Rs 31.75 lakh) in recalculated spend.
> - It is also the highest-volume supplier in this dataset.

### What it means
This supplier contributes the largest total procurement spend mainly because it supplies the largest volume. This does not mean it has the highest purchase rate per litre; Question 2 checks that separately. Spend is recalculated from quantity multiplied by rate. Procurement record PRC-001000 contains a recorded-cost error, so summing the uncorrected total_purchase_cost column would overstate spend by Rs 6,657.17.

## Question 2 - Are different suppliers paid different prices per litre?

### Answer in plain words
Yes, the price per litre does vary. A single transaction can be as low as Rs 47.59 or as high as Rs 64.00 per litre. But when you average each supplier over all its transactions, the averages sit in a narrow band, from Rs 54.40 to Rs 55.84 per litre. The overall weighted average, where bigger purchases count more, is about Rs 55.02 per litre. So the price differences between suppliers are small, even though single transactions vary a lot.

### How we found it
For each supplier, calculate the average, minimum, and maximum purchase rate per litre. The weighted average is the total recalculated cost divided by the total litres, so larger purchases have more influence than a simple average.

```sql
SELECT
    s.supplier_id,
    s.supplier_name,
    COUNT(*) AS records,
    ROUND(AVG(p.purchase_rate_per_litre), 2) AS avg_rate,
    ROUND(MIN(p.purchase_rate_per_litre), 2) AS min_rate,
    ROUND(MAX(p.purchase_rate_per_litre), 2) AS max_rate
FROM silver.milk_procurement AS p
JOIN silver.suppliers AS s
  ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.supplier_name
ORDER BY avg_rate DESC;

-- Weighted average price across all procurement
SELECT ROUND(
    SUM(ROUND(quantity_litres * purchase_rate_per_litre, 2)) /
    NULLIF(SUM(quantity_litres), 0), 2
) AS weighted_avg_rate
FROM silver.milk_procurement;
```

### Answer

> **Answer**
>
> - Transaction rates range from Rs 47.59 to Rs 64.00 per litre.
> - Supplier-level average rates range from Rs 54.40 to Rs 55.84.
> - Highest supplier average: Ganesh Reddy Dairy (SUP-0183), Rs 55.84/L.
> - Lowest supplier average: Suresh Verma Dairy (SUP-0010), Rs 54.40/L.
> - Overall quantity-weighted rate: about Rs 55.02/L.

### What it means
The dataset records real variation in the rate field, but the spread between supplier averages is much narrower than the spread between individual transactions. Check contract terms, fat and SNF incentives, timing, and collection conditions before calling a rate difference unfair. Rate comparisons should ideally control for milk quality, season, supplier agreement, and transaction date. This query is descriptive, not a causal explanation.

## Question 3 - Which suppliers provide the strongest quality for the price paid?

### Answer in plain words
Nitin Jadhav Dairy gives the best quality for the price among suppliers with enough tests to judge. Out of 91 quality tests, 88 were accepted, an acceptance rate of 96.70 percent, at an average rate of Rs 55.26 per litre. For comparison, the cheapest supplier by average rate, Suresh Verma Dairy, charges Rs 54.40 per litre but only 89.02 percent of its milk is accepted. So the best-quality supplier costs about Rs 0.86 more per litre, and in return about 7.68 percentage points more of its milk is accepted.

### How we found it
Join each quality test to its procurement batch, then to the supplier. Rank by acceptance percentage, keeping only suppliers with at least 30 tests so a supplier is not ranked on a handful of records. Review the price alongside quality rather than hiding the trade-off inside one score.

```sql
SELECT
    s.supplier_id,
    s.supplier_name,
    COUNT(*) AS tests,
    COUNT(*) FILTER (
        WHERE q.quality_status = 'Accepted'
    ) AS accepted_tests,
    COUNT(*) FILTER (
        WHERE q.quality_status = 'Rejected'
    ) AS rejected_tests,
    ROUND(100.0 * COUNT(*) FILTER (
        WHERE q.quality_status = 'Accepted'
    ) / NULLIF(COUNT(*), 0), 2) AS acceptance_pct,
    ROUND(AVG(p.purchase_rate_per_litre), 2) AS avg_rate
FROM silver.quality_tests AS q
JOIN silver.milk_procurement AS p
  ON p.batch_id = q.batch_id
JOIN silver.suppliers AS s
  ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.supplier_name
HAVING COUNT(*) >= 30
ORDER BY acceptance_pct DESC, avg_rate ASC
LIMIT 10;
```

### Answer

> **Answer**
>
> - **Nitin Jadhav Dairy (SUP-0131)**: 88 accepted out of 91 tests, 96.70% acceptance, at Rs 55.26/L.
> - For comparison, Suresh Verma Dairy averages Rs 54.40/L but has an 89.02% acceptance rate (73 of 82 tests).

### What it means
The top-quality supplier costs about Rs 0.86/L more than the lowest-average-rate supplier, but its observed acceptance rate is about 7.68 percentage points higher. This is a useful supplier-review comparison, not proof that paying more causes better quality. What counts as best value depends on how the business values accepted milk, rejected milk, testing costs, and supplier reliability. This question uses acceptance percentage as the primary quality measure and displays average rate beside it.

## Question 4 - Are recorded milk-purchase costs calculated correctly?

### Answer in plain words
Almost every record is correct. Only one record out of 18,000 is wrong: PRC-001000. Its quantity was 510.03 litres at Rs 52.21 per litre, so the cost should be Rs 26,628.67, but the recorded cost is Rs 33,285.84, an overstatement of Rs 6,657.17. The other 17,999 records match within one paise. The lesson is simple: do not silently overwrite the source cost. Keep the original value, store the calculated value, and flag the exception for review.

### How we found it
Create an expected cost for each row as quantity multiplied by rate, rounded to two decimal places, subtract it from the recorded amount, and flag absolute differences above Rs 0.01.

```sql
SELECT
    procurement_id,
    quantity_litres,
    purchase_rate_per_litre,
    total_purchase_cost AS recorded_cost,
    ROUND(quantity_litres * purchase_rate_per_litre, 2)
        AS calculated_cost,
    ROUND(
        total_purchase_cost -
        ROUND(quantity_litres * purchase_rate_per_litre, 2), 2
    ) AS difference_inr
FROM silver.milk_procurement
WHERE ABS(
    total_purchase_cost -
    ROUND(quantity_litres * purchase_rate_per_litre, 2)
) > 0.01
ORDER BY ABS(
    total_purchase_cost -
    ROUND(quantity_litres * purchase_rate_per_litre, 2)
) DESC;
```

### Answer

> **Answer**
>
> - One mismatch found: **PRC-001000**.
> - Quantity 510.03 L, rate Rs 52.21/L.
> - Calculated cost Rs 26,628.67, recorded cost Rs 33,285.84, overstatement Rs 6,657.17.
> - The other 17,999 records match within the one-paise tolerance.

### What it means
Do not silently overwrite the source cost. Preserve the original value, store the calculated value, and flag the exception for review. The row belongs to supplier Rajesh Rathod Dairy (SUP-0155). A finance or procurement owner should confirm which value is authoritative before correcting the official record.

## Question 5 - How much could a 2% reduction in milk-purchasing costs save?

### Answer in plain words
A 2 percent cut in milk-purchasing costs would save about Rs 96.38 lakh over the dataset period. The validated spend, recalculated from quantity multiplied by rate, is Rs 481,919,772.07, about Rs 48.19 crore, and 2 percent of that is about Rs 9,638,395.44. This is a scenario calculation, not a forecast. It gives management a sense of scale for rate negotiations and quality improvement, not a guaranteed saving.

### How we found it
First recalculate spend from quantity multiplied by rate, then multiply the total by 0.02. This is a scenario calculation, not a forecast or proof that a 2 percent reduction is achievable.

```sql
WITH validated_spend AS (
    SELECT SUM(ROUND(
        quantity_litres * purchase_rate_per_litre, 2
    )) AS spend_inr
    FROM silver.milk_procurement
)
SELECT
    ROUND(spend_inr, 2) AS baseline_spend_inr,
    ROUND(spend_inr * 0.02, 2) AS potential_2pct_saving_inr
FROM validated_spend;
```

### Answer

> **Answer**
>
> - Validated spend across all procurement records: **Rs 481,919,772.07** (about Rs 48.19 crore).
> - A 2% reduction would represent approximately **Rs 9,638,395.44** (about Rs 96.38 lakh) over the dataset period.

### What it means
This gives management a scale for prioritising rate negotiations, quality improvement, and supplier consolidation discussions. It is not a guaranteed saving. The main figure includes rejected procurement records because the dataset records a cost for them. If rejected milk is not paid for under the real commercial policy, the accepted-only baseline is Rs 422,004,105.05 and 2% of that is Rs 8,440,082.10. The reporting rule must be confirmed.

Note on the two spend totals: the validated spend here (Rs 481,919,772.07) is Rs 6,657.17 lower than the recorded total spend used elsewhere in the README (Rs 481,926,429.24), and the difference is exactly the PRC-001000 cost error from Question 4, because the validated figure recalculates every row as quantity multiplied by rate.

## Question 6 - Why is milk being rejected?

### Answer in plain words
Out of 18,000 quality tests, 2,311 were rejected, which is 12.84 percent. The main reason is Low SNF, with 1,303 rejections, or 56.38 percent of all rejections. Low Fat is next with 513, then High Acidity with 491, and High Temperature with only 4. So more than half of the problem is one reason: the milk does not have enough solids-not-fat. Fixing Low SNF first gives the biggest return on any quality work.

### How we found it
Filter the quality tests to Rejected, group by rejection reason, count the tests, and divide each count by the rejected-test total.

```sql
SELECT
    rejection_reason,
    COUNT(*) AS rejected_tests,
    ROUND(100.0 * COUNT(*) /
        SUM(COUNT(*)) OVER (), 2) AS share_of_rejections_pct
FROM silver.quality_tests
WHERE quality_status = 'Rejected'
GROUP BY rejection_reason
ORDER BY rejected_tests DESC;
```

### Answer

> **Answer**
>
> - **2,311 rejected tests** (12.84% of 18,000 tests).
> - Low SNF = 1,303 (56.38%), Low Fat = 513 (22.20%), High Acidity = 491 (21.25%), High Temperature = 4 (0.17%).

### What it means
Low SNF is the largest recorded reason and should be the first investigation priority. Review supplier-level SNF patterns, sampling, storage, and test procedures before deciding on corrective action. These percentages are based on rejection records, not rejected litres. A volume-weighted reason analysis could produce a different ranking.

## Question 7 - Which suppliers repeatedly provide lower-quality milk?

### Answer in plain words
Dinesh Pawar Dairy is the worst repeat offender among suppliers with enough tests to judge. Out of 84 tests, 21 were rejected, a rejection rate of 25.00 percent, one in every four batches. Next are Rajesh Jadhav Dairy at 23.66 percent, Ganesh Reddy Dairy at 21.69 percent, Anil Verma Dairy at 20.99 percent, and Vikram Singh Dairy at 20.62 percent. These are not one-off failures; they are a pattern, and they are the right suppliers for a focused quality review.

### How we found it
Join quality tests to procurement by batch_id, group by supplier, count tests and rejections, calculate the rejection rate, and restrict the ranking to suppliers with at least 30 tests so a supplier is not judged on a handful of records.

```sql
SELECT
    s.supplier_id,
    s.supplier_name,
    COUNT(*) AS tests,
    COUNT(*) FILTER (
        WHERE q.quality_status = 'Rejected'
    ) AS rejected_tests,
    ROUND(100.0 * COUNT(*) FILTER (
        WHERE q.quality_status = 'Rejected'
    ) / NULLIF(COUNT(*), 0), 2) AS rejection_pct
FROM silver.quality_tests AS q
JOIN silver.milk_procurement AS p
  ON p.batch_id = q.batch_id
JOIN silver.suppliers AS s
  ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.supplier_name
HAVING COUNT(*) >= 30
ORDER BY rejection_pct DESC, rejected_tests DESC
LIMIT 10;
```

### Answer

> **Answer**
>
> - **Dinesh Pawar Dairy (SUP-0087)**: 21 rejected out of 84, 25.00%.
> - Rajesh Jadhav Dairy (SUP-0024): 22/93, 23.66%.
> - Ganesh Reddy Dairy (SUP-0038): 18/83, 21.69%.
> - Anil Verma Dairy (SUP-0003): 17/81, 20.99%.
> - Vikram Singh Dairy (SUP-0083): 20/97, 20.62%.

### What it means
These suppliers are sensible candidates for a focused quality review, including SNF and fat trends, collection handling, and repeat testing. Review the cause before changing supplier terms. The ranking is based on test counts rather than volume-weighted rejection. The 30-test threshold is a screening choice to reduce small-sample noise, not a universal standard.

## Question 8 - Do suppliers who deliver more milk also provide better-quality milk?

### Answer in plain words
No. Across all 200 suppliers, the correlation between the volume a supplier delivers and its acceptance percentage is about -0.0608, which is extremely weak and slightly negative. In plain terms, a supplier that delivers more milk is not more likely to deliver better milk. Volume tells you nothing about quality here. A big supplier still needs the same quality checks as a small one.

### How we found it
For each supplier, calculate total litres and accepted tests divided by total tests. Then calculate the Pearson correlation between those two supplier-level measures.

```sql
WITH supplier_metrics AS (
    SELECT
        p.supplier_id,
        SUM(p.quantity_litres) AS total_litres,
        100.0 * COUNT(*) FILTER (
            WHERE q.quality_status = 'Accepted'
        ) / NULLIF(COUNT(*), 0) AS acceptance_pct
    FROM silver.milk_procurement AS p
    JOIN silver.quality_tests AS q
      ON q.batch_id = p.batch_id
    GROUP BY p.supplier_id
)
SELECT
    COUNT(*) AS suppliers,
    ROUND(CORR(total_litres, acceptance_pct)::numeric, 4)
        AS pearson_correlation
FROM supplier_metrics;
```

### Answer

> **Answer**
>
> - Across 200 suppliers, the Pearson correlation is approximately **-0.0608**.

### What it means
This is an extremely weak negative linear relationship. In this dataset, supplying more litres is not meaningfully associated with a higher acceptance percentage. Supplier volume should not be used as a substitute for quality monitoring. Correlation does not establish cause and can hide differences in season, supplier type, centre, or the number of tests per supplier.

## Question 9 - Which collection centre rejects the largest share of the milk it receives?

### Answer in plain words
Boriavi Milk Collection Centre rejects the largest share of the milk it receives, by volume. Out of 442,288.44 litres received, 60,816.91 litres were rejected, a volume rejection rate of 13.75 percent. Umreth is next at 13.60 percent, and Bakrol is lowest at 10.98 percent. This is a volume-based rate, not a count of batches: it measures the share of litres lost, which is what the money follows.

### How we found it
Join procurement to the collection-centre master data, sum all litres, sum rejected litres only, and divide rejected litres by received litres for each centre.

```sql
SELECT
    c.collection_centre_id,
    c.centre_name,
    COUNT(*) AS procurement_records,
    ROUND(SUM(p.quantity_litres), 2) AS received_litres,
    ROUND(SUM(CASE WHEN p.acceptance_status = 'Rejected'
                   THEN p.quantity_litres ELSE 0 END), 2)
        AS rejected_litres,
    ROUND(100.0 * SUM(CASE WHEN p.acceptance_status = 'Rejected'
                            THEN p.quantity_litres ELSE 0 END) /
          NULLIF(SUM(p.quantity_litres), 0), 2)
        AS rejection_by_volume_pct
FROM silver.milk_procurement AS p
JOIN silver.collection_centres AS c
  ON c.collection_centre_id = p.collection_centre_id
GROUP BY c.collection_centre_id, c.centre_name
ORDER BY rejection_by_volume_pct DESC;
```

### Answer

> **Answer**
>
> - **Boriavi Milk Collection Centre (CC-002)**: 60,816.91 rejected litres out of 442,288.44 received, a 13.75% volume rejection rate.
> - Umreth is next at 13.60%. Bakrol is lowest at 10.98%.

### What it means
Boriavi is the first centre to investigate for milk handling, chilling, time-to-testing, and supplier mix. Compare its processes with lower-rejection centres before deciding what to change. This is a volume-weighted rate. The overall volume rejection rate is 12.76%, while the record-count rejection rate is 12.84%; these are different metrics.

## Question 10 - How much more milk could be accepted if rejections fell by 10%?

### Answer in plain words
If rejections fell by 10 percent from where they are now, the business could accept about 111,724.74 more litres of milk. The current rejected volume is 1,117,247.35 litres, and 10 percent of that is the extra amount. This is a practical target for the quality programme: cut rejections by a tenth, and that is how much milk comes back into the system. It is a relative 10 percent cut in rejected litres, not a 10 percentage point cut in the rejection rate.

### How we found it
Sum quantity in litres where acceptance status is Rejected and multiply that amount by 10%. This is a relative 10% reduction in rejected litres, not a 10-percentage-point reduction in the rejection rate.

```sql
WITH rejected_volume AS (
    SELECT SUM(quantity_litres) AS rejected_litres
    FROM silver.milk_procurement
    WHERE acceptance_status = 'Rejected'
)
SELECT
    ROUND(rejected_litres, 2) AS current_rejected_litres,
    ROUND(rejected_litres * 0.10, 2)
        AS potential_additional_accepted_litres
FROM rejected_volume;
```

### Answer

> **Answer**
>
> - Current rejected volume: **1,117,247.35 litres**.
> - A 10% relative reduction would represent **111,724.74 litres** of additional potentially accepted milk.

### What it means
This gives a practical improvement target for the quality programme. Prioritising the dominant low-SNF reason and the highest-rejection suppliers and centres may help focus the investigation. The calculation assumes the recovered volume becomes acceptable and usable. It does not automatically translate into revenue or finished product; capacity, product mix, and commercial acceptance rules also matter.

## Question 11 - Are production batches producing a consistent amount of finished product?

### Answer in plain words
Yes, the output is consistent within each product. Every one of the 4,000 batches uses exactly 650.00 litres of raw milk. Liquid milk products give 633.75 litres per batch, which is 97.50 percent of the input. Flavoured milk gives 630.50 litres, 97.00 percent. Buttermilk and lassi give 611.00 litres, 94.00 percent. Paneer gives 120.51 kg, 18.00 percent of the 669.5 kg input-mass basis. Ghee gives 29.25 litres, 4.50 percent. Cream gives 32.50 litres, 5.00 percent. Butter gives 30.13 kg, about 4.50 percent. Curd gives 649.41 kg, about 97.00 percent.

### How we found it
Sum all raw-milk input rows per production_id, then join to the primary-product output and product unit. For kilogram products, convert 650 litres to 669.5 kg using the dataset conversion factor of 1.03 kg per litre before calculating the yield ratio. Only primary product output is used; the by-product and residual output is kept separate.

```sql
WITH input_totals AS (
    SELECT production_id, SUM(input_quantity) AS input_litres
    FROM silver.production_inputs
    GROUP BY production_id
),
primary_outputs AS (
    SELECT production_id, product_id,
           SUM(output_quantity) AS primary_output
    FROM silver.production_outputs
    WHERE output_classification = 'Primary product'
    GROUP BY production_id, product_id
),
batch_yield AS (
    SELECT
        b.production_id, b.product_id, pr.product_name,
        pr.unit_of_measure, i.input_litres, o.primary_output,
        CASE WHEN pr.unit_of_measure = 'Kilogram'
             THEN i.input_litres * 1.03
             ELSE i.input_litres END AS comparable_input
    FROM silver.production_batches AS b
    JOIN input_totals AS i ON i.production_id = b.production_id
    JOIN primary_outputs AS o
      ON o.production_id = b.production_id
     AND o.product_id = b.product_id
    JOIN silver.products AS pr ON pr.product_id = b.product_id
)
SELECT
    product_name, unit_of_measure,
    COUNT(*) AS batches,
    ROUND(AVG(input_litres), 2) AS avg_input_litres,
    ROUND(AVG(primary_output), 2) AS avg_primary_output,
    ROUND(100.0 * AVG(primary_output / comparable_input), 2)
        AS yield_pct
FROM batch_yield
GROUP BY product_name, unit_of_measure
ORDER BY yield_pct DESC;
```

### Answer

> **Answer**
>
> - All 4,000 production batches are marked Completed. Each batch uses 650.00 litres of raw milk.
> - Liquid milk products: 633.75 L per batch (97.50%). Flavoured milk: 630.50 L (97.00%). Buttermilk/lassi: 611.00 L (94.00%).
> - Paneer: 120.51 kg (18.00% of the 669.5 kg input-mass basis). Ghee: 29.25 L (4.50%). Cream: 32.50 L (5.00%). Butter: 30.13 kg (about 4.50%). Curd: 649.41 kg (about 97.00%).

### What it means
The batch outputs follow a consistent product-specific conversion pattern in the supplied data. Use the yield table for comparisons within the same product and unit, not to compare litres directly with kilograms. Only primary product output is used in the yield metric; the by-product and residual output is kept separate. The 1.03 kg per litre conversion is a dataset modelling assumption, not a universal dairy-process constant.

## Question 12 - Are any production batches unusually low- or high-yield compared with the same product?

### Answer in plain words
No. After comparing each batch only with batches of the same product, and after converting kilograms to litres correctly, no batch stands out. Within each product, the primary yield is the same across its batches to four decimal places. There is simply no batch-level yield variation in this dataset to investigate. That is a limit of the data, not a finding about a real factory: a real plant would show variation, and this dataset cannot support anomaly monitoring conclusions.

### How we found it
Calculate a per-batch yield after converting input to the product output unit. Compare each batch only with batches of the same product; a three-standard-deviation check is a common screening method. Round yield to four decimals to avoid treating floating-point noise as a real process difference.

```sql
WITH input_totals AS (
     SELECT production_id, SUM(input_quantity) AS input_litres
     FROM silver.production_inputs
     GROUP BY production_id
),
primary_outputs AS (
     SELECT production_id, product_id,
            SUM(output_quantity) AS primary_output
     FROM silver.production_outputs
     WHERE output_classification = 'Primary product'
     GROUP BY production_id, product_id
),
batch_yield AS (
     SELECT b.production_id, b.product_id, pr.product_name,
            ROUND(o.primary_output /
                 CASE WHEN pr.unit_of_measure = 'Kilogram'
                      THEN i.input_litres * 1.03
                      ELSE i.input_litres END, 4) AS yield_ratio
     FROM silver.production_batches AS b
     JOIN input_totals AS i ON i.production_id = b.production_id
     JOIN primary_outputs AS o
       ON o.production_id = b.production_id
      AND o.product_id = b.product_id
     JOIN silver.products AS pr ON pr.product_id = b.product_id
),
scored AS (
     SELECT *,
         AVG(yield_ratio) OVER (PARTITION BY product_id) AS avg_yield,
         STDDEV_POP(yield_ratio) OVER (PARTITION BY product_id) AS sd_yield
     FROM batch_yield
)
SELECT production_id, product_name, yield_ratio,
        ROUND((yield_ratio - avg_yield) /
               NULLIF(sd_yield, 0), 2) AS z_score
FROM scored
WHERE sd_yield > 0
   AND ABS((yield_ratio - avg_yield) / NULLIF(sd_yield, 0)) > 3
ORDER BY ABS((yield_ratio - avg_yield) / NULLIF(sd_yield, 0)) DESC;
```

### Answer

> **Answer**
>
> - **No production-yield outlier was identified** after comparing like products with the correct unit conversion and rounding.
> - Within each product, the observed primary yield is the same across its batches to four decimal places.

### What it means
There is no batch-level yield variation in this dataset to investigate. This is a limitation of the available data: it cannot support realistic process-variation or anomaly-monitoring conclusions. A first unadjusted comparison of kilograms against litres can create false anomalies. Always align units and compare a batch only with the same product.

## Question 13 - Which products require more raw milk per production batch?

### Answer in plain words
No product uses more raw milk per batch than any other. Every one of the 4,000 completed batches consumes exactly 650.00 litres. The total input differs between products only because some products have 334 batches and others have 333. Overall raw-milk input is 2,600,000 litres. So this question reveals that the dataset applies a fixed 650-litre input to each batch; it cannot tell you which product is more milk-hungry in a real factory.

### How we found it
Aggregate all production_input rows by production_id, join the batch to the product master, and average input litres by product. Production inputs can have multiple rows because one run can draw milk from multiple source batches.

```sql
WITH input_by_batch AS (
    SELECT production_id, SUM(input_quantity) AS raw_milk_litres
    FROM silver.production_inputs
    WHERE input_material_type = 'Raw Milk'
    GROUP BY production_id
)
SELECT
    pr.product_name,
    COUNT(*) AS production_batches,
    ROUND(AVG(i.raw_milk_litres), 2) AS avg_raw_milk_litres_per_batch,
    ROUND(SUM(i.raw_milk_litres), 2) AS total_raw_milk_litres
FROM input_by_batch AS i
JOIN silver.production_batches AS b
  ON b.production_id = i.production_id
JOIN silver.products AS pr
  ON pr.product_id = b.product_id
GROUP BY pr.product_id, pr.product_name
ORDER BY avg_raw_milk_litres_per_batch DESC;
```

### Answer

> **Answer**
>
> - No product uses more raw milk per batch: every one of the 4,000 completed batches consumes **650.00 litres**.
> - Overall raw-milk input is **2,600,000 litres**. Total input differs only because some products have 334 batches and others 333.

### What it means
This question reveals that the model applies a fixed 650-litre input to each batch. To compare recipe intensity in a real factory, input quantities for all ingredients and actual batch outputs would be needed. Do not rank products by total input alone: a product with one additional batch will have a larger total even though its per-batch requirement is identical.

## Question 14 - Which products generate the most sales revenue?

### Answer in plain words
Total net sales revenue is Rs 26,734,294.03. The top three products are Pure Cow and Buffalo Ghee at Rs 5,986,642.50, which is 22.39 percent of all revenue, Fresh Malai Paneer at Rs 5,531,071.00, and Pasteurised Table Butter at Rs 5,156,439.08. Together these three products are more than half of all sales value. They deserve the most attention in pricing, demand planning, and availability reviews, but revenue is not profit, and a high-revenue product is not automatically a high-profit one.

### How we found it
Join order lines to the product master and sum line_total. The line_total in this dataset reconciles to quantity fulfilled multiplied by unit selling price less discount amount, so it represents the net value of fulfilled units.

```sql
SELECT
    pr.product_id,
    pr.product_name,
    COUNT(*) AS order_lines,
    ROUND(SUM(l.quantity_fulfilled), 2) AS units_fulfilled,
    ROUND(SUM(l.line_total), 2) AS net_sales_revenue_inr
FROM silver.sales_order_lines AS l
JOIN silver.products AS pr
  ON pr.product_id = l.product_id
GROUP BY pr.product_id, pr.product_name
ORDER BY net_sales_revenue_inr DESC;
```

### Answer

> **Answer**
>
> - Total net sales revenue: **Rs 26,734,294.03**.
> - Pure Cow & Buffalo Ghee: Rs 5,986,642.50 (22.39% of total). Fresh Malai Paneer: Rs 5,531,071.00. Pasteurised Table Butter: Rs 5,156,439.08.

### What it means
These products contribute the largest recorded sales value and may deserve attention in pricing, demand planning, and availability reviews. Revenue does not equal profit. The dataset has no complete product-level cost-of-goods-sold or margin calculation in these tables. High revenue alone does not prove high profitability.

## Question 15 - How many customer orders were not fully fulfilled or were delivered late?

### Answer in plain words
Out of 14,000 orders, 2,834 were not fully fulfilled: 2,227 were partially delivered and 607 were cancelled. The remaining 11,166 were delivered and fully fulfilled. On lateness, the picture is clean: among the 13,393 non-cancelled orders that have an actual delivery date, none was later than the expected date; every one is recorded on the expected date. So the real problem is fulfilment completeness, not late delivery. The partially delivered and cancelled orders need separate investigation, because their causes are probably different.

### How we found it
First summarise ordered and fulfilled quantities by order_id. An order is fully fulfilled when fulfilled quantity equals ordered quantity. Then inspect the order status and compare actual delivery date with expected delivery date; cancelled orders have no actual delivery date.

```sql
WITH order_lines AS (
    SELECT order_id,
           SUM(quantity_ordered) AS ordered_qty,
           SUM(quantity_fulfilled) AS fulfilled_qty
    FROM silver.sales_order_lines
    GROUP BY order_id
)
SELECT
    o.order_status,
    COUNT(*) AS orders,
    COUNT(*) FILTER (
        WHERE l.fulfilled_qty < l.ordered_qty
    ) AS not_fully_fulfilled,
    COUNT(*) FILTER (
        WHERE o.actual_delivery_date IS NOT NULL
          AND o.actual_delivery_date > o.expected_delivery_date
    ) AS late_orders
FROM silver.sales_orders AS o
JOIN order_lines AS l ON l.order_id = o.order_id
GROUP BY o.order_status
ORDER BY o.order_status;
```

### Answer

> **Answer**
>
> - **2,834 orders not fully fulfilled**: 2,227 Partially Delivered and 607 Cancelled.
> - The remaining 11,166 are Delivered and fully fulfilled.
> - Among 13,393 non-cancelled orders with an actual delivery date, **0 are later than the expected date**; all are recorded on the expected date.

### What it means
The primary issue is fulfilment completeness, not recorded delivery lateness. Investigate the 2,227 partially delivered orders separately from the 607 cancelled orders because their operational causes may differ. "On time" is measured only from the date fields provided. The date fields do not reveal delivery time-of-day, partial quantities at each drop, or the reason an order was cancelled.

## Consolidated findings

| Area | Finding | What it suggests |
|---|---|---|
| Procurement | Top spend supplier: Ganesh Jadhav Dairy; Rs 31.75 lakh recalculated spend. | Large spend is primarily associated with high supplied volume. |
| Purchase rates | Supplier average range: Rs 54.40 to Rs 55.84 per litre; weighted overall rate Rs 55.02 per litre. | Review pricing with quality and contract context. |
| Supplier quality | Highest acceptance among suppliers with 30 or more tests: 96.70% for Nitin Jadhav Dairy. | Use both acceptance rate and rate per litre when reviewing value. |
| Cost control | One cost mismatch: PRC-001000; overstatement Rs 6,657.17. | Preserve source value and flag for finance review. |
| Savings scenario | 2% of validated total spend = about Rs 96.38 lakh. | Scenario only; confirm whether rejected milk is paid for. |
| Quality | 2,311 rejected tests; Low SNF is 56.38% of rejections. | Low SNF is the first investigation priority. |
| Collection centres | Boriavi has the highest rejected-volume rate: 13.75%. | Compare centre handling and supplier mix. |
| Production | Every completed batch uses 650 L; no within-product yield outliers. | This dataset has fixed product recipes and limited process variation. |
| Sales | Ghee has the highest sales value: Rs 59.87 lakh. | Revenue ranking is not a profit ranking. |
| Order fulfilment | 2,834 orders not fully fulfilled; 0 late dates among non-cancelled orders. | Focus on partial fulfilment and cancellations. |

### Recommended order for a business review
1. Investigate Low SNF rejections and the suppliers and centres with the highest rejection percentages.
2. Review the one procurement-cost exception before reporting procurement spend.
3. Compare supplier price with acceptance percentage instead of choosing suppliers by price alone.
4. Investigate partial fulfilment and cancellations by product and customer code.
5. Treat production yield as a data-model consistency result, not a plant-efficiency benchmark.

## Data-handling note
Do not overwrite original records simply because a calculation identifies an exception. Keep the original field, create a calculated field, record the rule, and flag the mismatch for review. Likewise, do not claim SQL execution just because a query is included in project documentation: attach the actual psql output or database result when execution has been completed.

## Next step / Related files
- The source PDF: [DairyChain_Business_Questions_and_SQL_Solutions.pdf](../13_Project_Evidence/DairyChain_Business_Questions_and_SQL_Solutions.pdf)
- Business questions overview: [README.md](README.md)
- Key findings: [../06_Business_Findings_and_Impact/key_findings.md](../06_Business_Findings_and_Impact/key_findings.md)
- Guided tour: [../README.md](../README.md)
