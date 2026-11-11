# Product Performance and Profitability


## Purpose
This file answers which products sell most and which contribute most to profit, as far as the supplied numbers allow. It is for a manager who needs product decisions based on revenue and fulfilment, not on revenue alone.

## In this file
- Which products sell the most?
- Which products contribute more to profitability?

## Business question
Which products sell the most?

## Business context
Product sales show demand and revenue concentration. If a few products carry most revenue, a problem with one product matters more than a problem with a small one.

## Data required
Gold table sales_product_performance, 12 rows, one per product. The 12 product rows are now from the model data read with pbixray get_table (Source 23). Total revenue Rs 26,734,294.03 and total orders 14,000 are supplied.

## Analytical approach
Sum revenue and quantity by product, rank the products, and show each product share of total revenue. Use the Gold table, not a re-aggregation of raw orders, so the grain stays at product level.

## KPI definitions
Product revenue share equals product revenue divided by total revenue, times 100.

## Actual result
Product ranking from the model data (Source 23): Pure Cow and Buffalo Ghee Rs 5,986,642.50 is the top revenue product, followed by Fresh Malai Paneer Rs 5,531,071.00 and Pasteurised Table Butter Rs 5,156,439.08. Full table in [../04_Business_Analytics/sales_analysis.md](../04_Business_Analytics/sales_analysis.md).

## Direct answer
Pure Cow and Buffalo Ghee generates the highest sales revenue, Rs 5,986,642.50, 22.39 percent of total revenue.

## Business interpretation
The project has 12 products in the Gold table, and the rows are now supplied from the model data (Source 23). The top 3 products carry 62.37 percent of revenue, so a problem with one of them matters more than a problem with a small one.

## Recommendation
The 12 rows are now supplied (Source 23). Next: supply the 364 daily rows, with revenue, orders and quantity fulfilled, and the cancellation and partial-delivery reasons.

## Business impact
Measured impact: none. Expected benefit: a product ranking would show where to protect supply and fulfilment first.

## Evidence
Source: README names the table and its 12 rows. Product rows now from the model data read with pbixray get_table (Source 23).

## Business question
Which products contribute more to business profitability?

## Business context
A product contributes to profit only after its cost is removed. A high-revenue product with a high cost can contribute less than a smaller product with a low cost.


## Analytical approach
Rank products by gross profit once product COGS is known, and compare that rank with the revenue rank.

## KPI definitions
Product gross profit equals product net revenue minus product COGS.


## Business interpretation
Do not present a product as high-profit from its sales alone. That is the exact error the brief warns against.

## Recommendation
Supply product COGS with the product revenue rows.

## Business impact
Measured impact: none. Expected benefit: product profit would guide pricing, promotion and production focus.


## Next step / Related files
- Sales analysis](../04_Business_Analytics/sales_analysis.md)
- Profitability analysis](../04_Business_Analytics/profitability_analysis.md)
- Q and A sales](09_sales_and_demand.md)
