# Profitability Questions


## Purpose
This file answers whether DairyChain is profitable from revenue alone. It is for a manager who needs profit and margin, not revenue alone.

## In this file
- What is overall profitability?
- Are high-revenue products high-profit products?

## Note on the 20 business questions (Source 13)
Source 13 defines 20 business questions across procurement, quality, production, and sales. The 20 questions are placed in full in [05_procurement_and_supplier_analysis.md](05_procurement_and_supplier_analysis.md), [06_production_efficiency.md](06_production_efficiency.md), and [09_sales_and_demand.md](09_sales_and_demand.md), with the register in [README.md](README.md).

## Business question
What is the overall business profitability?

## Business context
A business can earn high revenue and still earn low profit, because procurement, production, wastage, returns, rent and salaries consume revenue. Profit is the test, not revenue.

## Data required
Sales revenue is supplied: Rs 26,734,294.03.

## Analytical approach
Use the formulas in the KPI file: Net revenue equals Gross sales minus Discounts minus Sales returns. Gross profit equals Net revenue minus COGS. Operating profit equals Gross profit minus Operating Expenses. Define COGS first, and do not subtract the same cost twice.

## KPI definitions
Gross profit margin equals (Gross Profit / Net Revenue) x 100. Operating profit margin equals (Operating Profit / Net Revenue) x 100.

## Actual result
Revenue is Rs 26,734,294.03.

## Direct answer
Profitability cannot be stated from the supplied numbers. Revenue alone does not prove profit.

## Business interpretation
Revenue is a sales result. Without COGS and operating expenses, any profit number would be invented. The honest result is that the profit question is open, not that profit is high or low.

## Recommendation
Supply the COGS definition, discount and returns fields, and operating expense records. Then calculate net revenue, gross profit and operating profit, and add the outputs here.

## Business impact
Measured impact: none was supplied, so none is claimed. Expected benefit: once the inputs exist, management can see margin by product and by period.

## Evidence
Source: user-supplied README, 2026-11-11, sales section only.

## Business question
Are high-revenue products necessarily high-profit products?

## Business context
A product can sell a lot at a low margin, or sell less at a high margin. Revenue ranking and profit ranking are different rankings, and only cost data can tell them apart.


## Analytical approach
Rank products by revenue, then rank the same products by gross profit once COGS is known. Compare the two rankings.

## KPI definitions
Gross profit by product equals product net revenue minus product COGS. Gross profit margin by product equals product gross profit divided by product net revenue, times 100.


## Business interpretation
Do not call a top-selling product a top-profit product until its cost is known. That mistake is common, and this file does not make it.

## Recommendation
Supply product revenue and product COGS. Then add both rankings here.

## Business impact
Measured impact: none. Expected benefit: management can protect margin, not only volume.

## Evidence
Source: README names sales_product_performance with 12 rows.

## Next step / Related files
- Profitability analysis](../04_Business_Analytics/profitability_analysis.md)
- KPI definitions](../04_Business_Analytics/kpi_definitions.md)
- Profit drivers](02_profit_drivers_and_cost_leakage.md)
