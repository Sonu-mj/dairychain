# Sales and Demand Patterns


## Purpose
This file answers how sales performed, how fulfilment differed from orders, and what demand patterns can be shown. It is for a manager who needs revenue with fulfilment, not revenue alone.

## In this file
- Which products and days performed best?
- How did fulfilment compare with orders?
- S-01 to S-06: sales questions from Source 13

## Business question
Which products sell the most, and how does sales performance change over time?

## Business context
Product and daily views show demand concentration and trends. A daily summary can show a peak or a fall that a period total hides.

## Data required
Gold tables sales_product_performance, 12 rows, and sales_daily_summary, 364 rows. Total revenue Rs 26,734,294.03 and total orders 14,000 are supplied.

## Analytical approach
Sum revenue by product and by day, rank products, and plot daily revenue. Use the Gold tables at their stated grain. Do not claim forecasting or predictive demand modelling unless it is implemented and shown.

## KPI definitions
Product revenue share equals product revenue divided by total revenue, times 100. Daily revenue is the sum for that day.

## Actual result
Product ranking is now from the model data (Source 23) - see S-02. Totals are shown as README statements and now also checked against the model data.

## Direct answer
The top revenue product is Pure Cow and Buffalo Ghee, Rs 5,986,642.50.

## Business interpretation
The project has the right Gold tables for this question: 12 products and 364 days.

## Recommendation
Supply the 364 daily rows, with revenue, orders and quantity fulfilled. The 12 product rows are now supplied (Source 23).

## Business impact
Measured impact: none. Expected benefit: a product and daily view would show where demand is strong and where it falls.

## Evidence
Source: README names both Gold tables and their counts. Product rows now from the model data (Source 23).

## Business question
How much of what was ordered was fulfilled, and how many orders were not delivered in full?

## Business context
Fulfilment shows what reached the customer. An order count alone hides partial delivery and cancellation.


## Analytical approach
Divide quantity fulfilled by quantity ordered. Count orders by status and check that the status counts add to total orders.

## KPI definitions
Fulfilment rate by quantity equals quantity fulfilled divided by quantity ordered, times 100. Delivered share equals delivered orders divided by total orders, times 100.

## Actual result
Quantity fulfilled 161,036.41 of 181,804 ordered. Fulfilled share, calculated: 88.58 percent. Unfulfilled quantity, calculated: 20,767.59. Delivered 11,166, 79.76 percent. Cancelled 607, 4.34 percent. Orders not delivered in full, calculated: 2,834.

## Direct answer
About 1 in 5 orders was not delivered in full, and about 1 in 9 units ordered was not fulfilled.

## Business interpretation
This is a fulfilment gap, not a proven cause. No cause is claimed.

## Recommendation
Supply cancellation and partial-delivery reasons, by product and by day. Then check whether a product, a day or a reason explains the gap.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: fixing the main fulfilment reason would raise delivered orders above 11,166.

## Evidence
Source: user-supplied README, 2026-11-11, sales section.

## Business question
S-01 - What is the total sales revenue generated?

## Business context
Determine the overall revenue generated through sales. This provides an overall view of the recorded sales revenue and can be used as a foundation for analysing sales performance by date, product, and category.

## Data required
Gold tables gold.sales_daily_summary and gold.sales_product_performance. Required: total_revenue.

## Analytical approach
Use one appropriate reporting source for the calculation. Both daily and product-level sales tables contain revenue at different grains. Do not add the two revenue totals together.

## KPI definitions
Total sales revenue equals SUM(total_revenue) from one grain only, in rupees.

## Actual result
Total sales revenue Rs 26,734,294.03.

## Direct answer
Total sales revenue is Rs 26,734,294.03.

## Business interpretation
This is a sales result, not a profit result. Revenue alone does not prove profit.

## Recommendation
Use the daily table for trends and the product table for product comparison, and never add the two together.

## Business impact
Measured impact: none was supplied in profit terms, so none is claimed. Expected benefit: a shown revenue total anchors every sales comparison.

## Evidence
Source: Source 13, S-01, user-supplied 2026-11-11, recorded project reference Rs 26,734,294.03. Also in the user-supplied README, 2026-11-11. Source 23: total checked against the model data read with pbixray get_table (daily sum and product sum both Rs 26,734,294.03).

## Business question
S-02 - Which products generate the highest sales revenue?

## Business context
Identify the products contributing the most revenue. This helps identify the products contributing most to sales revenue and can support product performance comparisons and decisions about sales priorities.

## Data required
Gold table gold.sales_product_performance. Required: product_name, category, total_revenue.

## Analytical approach
Use the product-level revenue field, order by total_revenue descending, and show the top five or top six products. Avoid joining the summary to another table in a way that duplicates its values.

## KPI definitions
Product revenue equals total_revenue for that product.

## Actual result
Product revenue ranking from the model data read with pbixray get_table (Source 23). Ranked by total revenue, highest first.

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

The top 3 products carry 62.37 percent of revenue. Product revenue sums to Rs 26,734,294.03, matching the daily total exactly. Product-associated orders sum to 28,000, not 14,000 - see the shown proof in [sales_analysis.md](../04_Business_Analytics/sales_analysis.md): an order appears once per product, so product-level `total_orders` must not be summed as a distinct order count.

## Direct answer
Pure Cow and Buffalo Ghee generates the highest sales revenue, Rs 5,986,642.50, 22.39 percent of total revenue, followed by Fresh Malai Paneer at Rs 5,531,071.00 and Pasteurised Table Butter at Rs 5,156,439.08.

## Business interpretation
Revenue is concentrated: the top 3 products carry almost two-thirds of revenue, so a supply or fulfilment problem with one of them matters more than a problem with a small product. Spiced Masala Buttermilk is the smallest revenue product at Rs 432,450.00, 1.62 percent.

## Recommendation
Protect supply and fulfilment for the top 3 products first. Then supply the 364 daily rows to see whether revenue concentration changes over time.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: the ranking shows where revenue is concentrated.

## Evidence
Source: Source 13, S-02, user-supplied 2026-11-11. Product rows now from the model data read with pbixray get_table (Source 23).

## Business question
S-03 - How are orders distributed across product categories?

## Business context
Understand how order activity is distributed across product categories. This provides an indication of the order activity associated with each product category and can help compare category-level sales activity.

## Data required
Gold table gold.sales_product_performance. Required: category, total_orders.

## Analytical approach
Group by category and sum total_orders. The product-level table contains one record per product. An order may contain products from multiple categories, so summing product-level total_orders by category may count product-associated orders rather than unique orders. Do not label this result as a distinct order count by category unless the underlying data supports that definition. A true distinct order count by category requires suitable order-level detail containing both order identifiers and product categories.

## KPI definitions
Product-associated orders by category equals SUM(total_orders) grouped by category. This is not a distinct order count.

## Actual result
Category breakdown from the model data read with pbixray get_table (Source 23). Category totals are sums of the shown product rows.

| Category | Product-associated orders | Total revenue (Rs) |
|---|---:|---:|
| Liquid Milk | 9307 | 3,258,914.70 |
| Fat Rich | 7031 | 13,497,989.08 |
| Fermented | 4627 | 2,214,356.75 |
| Coagulated | 2341 | 5,531,071.00 |
| Beverage | 4694 | 2,231,962.50 |
| **Total** | **28,000** | **26,734,294.03** |

Fat Rich carries the most revenue (Rs 13,497,989.08, 50.49 percent of total revenue) and Liquid Milk carries the most product-associated orders (9,307).

## Direct answer
Fat Rich is the largest category by revenue at Rs 13,497,989.08; Liquid Milk has the most product-associated orders at 9,307.

## Business interpretation
Category totals must be read as product-associated orders, not as distinct orders: the category order total is 28,000, while distinct orders are 14,000. An order can contain products from multiple categories.

## Recommendation
Use these category totals labelled as product-associated orders. Supply order-level detail if a distinct order count by category is needed.

## Business impact
Measured impact: none. Expected benefit: the category view shows where order activity and revenue sit.

## Evidence
Source: Source 13, S-03, user-supplied 2026-11-11. Category rows computed from the shown product rows (Source 23 model data).

## Business question
S-04 - What is the sales quantity fulfilment rate?

## Business context
Measure how much of the ordered quantity was fulfilled. This indicates the proportion of ordered sales quantity that was fulfilled. A lower percentage may indicate that a larger portion of the ordered quantity remained unfulfilled.

## Data required
Gold table gold.sales_daily_summary. Required: quantity_ordered, quantity_fulfilled.

## Analytical approach
Divide quantity fulfilled by quantity ordered. Quantity fulfilment rate is not the same as the percentage of orders delivered successfully. These should be treated as separate operational metrics.

## KPI definitions
Quantity fulfilment rate equals (Quantity Fulfilled / Quantity Ordered) x 100.

## Actual result
Quantity ordered 181,804. Quantity fulfilled 161,036.41. Quantity fulfilment rate, calculated: 88.58 percent. Unfulfilled quantity, calculated: 20,767.59.

## Direct answer
88.58 percent of the ordered quantity was fulfilled.

## Business interpretation
About 1 in 9 units ordered was not fulfilled. This is a quantity gap, not the same as the order-status gap in S-05.

## Recommendation
Supply fulfilment by product and by day, with reasons for unfulfilled quantity.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: a fulfilment view would show where quantity is lost.

## Evidence
Source: Source 13, S-04, user-supplied 2026-11-11. Totals from the user-supplied README, 2026-11-11. Source 23: totals checked against the model data (quantity fulfilled 161,036.41 of 181,804 ordered, 88.58 percent).


## Business context
Understand the distribution of orders across fulfilment statuses.

## Data required
Gold table gold.sales_daily_summary. Required: delivered_orders, partially_delivered_orders, cancelled_orders, total_orders.

## Analytical approach
Count orders by status and check that the status counts reconcile with total orders when the statuses are mutually exclusive and collectively exhaustive under the source definition. The overall project reference is 14,000 orders.

## KPI definitions
Delivered share equals (Delivered Orders / Total Orders) x 100.

## Actual result
Delivered 11,166, 79.76 percent. Cancelled 607, 4.34 percent. Total 14,000.


## Business interpretation
About 1 in 5 orders was not delivered in full.

## Recommendation
Supply cancellation and partial-delivery reasons, by product and by day.

## Business impact
Measured impact: none was supplied in rupees, so none is claimed. Expected benefit: fixing the main fulfilment reason would raise delivered orders above 11,166.

## Evidence
Source: Source 13, S-05, user-supplied 2026-11-11, recorded project reference 11,166 / 2,227 / 607 / 14,000. Also in the user-supplied README, 2026-11-11. Source 23: totals checked against the model data (11,166 / 2,227 / 607 / 14,000).

## Business question
S-06 - How does sales revenue change over time?

## Business context
Understand daily revenue patterns and identify changes in sales performance. This helps management observe daily revenue patterns and identify periods of higher or lower recorded sales. It can also support trend comparisons and further investigation of unusual changes.

## Data required
Gold table gold.sales_daily_summary. Required: order_date, total_revenue.

## Analytical approach
Use the daily summary table and the date-level grain. Order the result chronologically. Do not join daily revenue to product-level records unless the intended analysis requires detailed sales data and the join is designed to preserve the correct revenue allocation.

## KPI definitions
Daily revenue equals total_revenue for that order_date.

## Actual result
The trend SHAPE is now described from the dashboard screenshots (Source 24, 2026-11-11): Page 1 "Monthly Revenue" line shows monthly revenue about 2.1M to 2.4M per month, Nov 2025 to Sep 2026, with peaks around Mar 2026 and Aug 2026 and a low around Feb 2026; Page 4 "Daily Sales Revenue Trend" shows daily revenue about 40K to 110K per day, Apr 2026 to Oct 2026, highly variable day to day with no smooth trend visible, and that chart is filtered to 01-04-2026 to 06-10-2026. No exact monthly or daily value is readable from the charts, so none is claimed. Result: (trend shape only).

## Direct answer
Revenue is variable with no smooth trend: monthly totals stay roughly between 2.1M and 2.4M, and daily revenue jumps between about 40K and 110K. No exact peak or low day can be named without the daily rows.

## Business interpretation
The project has the right table for this question, 364 daily rows, but the rows are missing.

## Recommendation
Supply the 364 daily rows with order_date and total_revenue, then plot them chronologically.

## Business impact
Measured impact: none. Expected benefit: a daily view would show when revenue rises and falls.

## Evidence
Source: Source 13, S-06, user-supplied 2026-11-11.

## Next step / Related files
- Sales analysis](../04_Business_Analytics/sales_analysis.md)
- Product performance](04_product_performance.md)
- Key findings](../06_Business_Findings_and_Impact/key_findings.md)
