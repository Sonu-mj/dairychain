# Profitability Questions

> Status: PENDING EVIDENCE

## Purpose
This file answers whether DairyChain is profitable, and why that question cannot be answered from revenue alone. It is for a manager who needs profit, margin and the missing inputs named clearly.

## In this file
- What is overall profitability?
- Are high-revenue products high-profit products?

## Note on the 20 business questions (Source 13)
Source 13 defines 20 business questions across procurement, quality, production, and sales. None of the 20 questions covers profit, because no COGS, discounts, returns, or operating expenses were supplied. The 20 questions are placed in full in [05_procurement_and_supplier_analysis.md](05_procurement_and_supplier_analysis.md), [06_production_efficiency.md](06_production_efficiency.md), and [09_sales_and_demand.md](09_sales_and_demand.md), with the register in [README.md](README.md). No profit answer is added from them here.

## Business question
What is the overall business profitability?

## Business context
A business can earn high revenue and still earn low profit, because procurement, production, wastage, returns, rent and salaries consume revenue. Profit is the test, not revenue.

## Data required
Sales revenue is supplied: Rs 26,734,294.03. Discounts, sales returns, COGS and operating expenses are not supplied. No profit Gold table is listed.

## Analytical approach
Use the formulas in the KPI file: Net revenue equals Gross sales minus Discounts minus Sales returns. Gross profit equals Net revenue minus COGS. Operating profit equals Gross profit minus Operating Expenses. Define COGS first, and do not subtract the same cost twice.

## KPI definitions
Gross profit margin equals (Gross Profit / Net Revenue) x 100. Operating profit margin equals (Operating Profit / Net Revenue) x 100.

## Actual result
No profit result was supplied. Revenue is Rs 26,734,294.03. Gross profit, operating profit and both margins are PENDING EVIDENCE.

## Direct answer
Profitability cannot be stated from the supplied numbers. Revenue alone does not prove profit.

## Business interpretation
Revenue is a sales result. Without COGS and operating expenses, any profit number would be invented. The honest result is that the profit question is open, not that profit is high or low.

## Recommendation
Supply the COGS definition, discount and returns fields, and operating expense records. Then calculate net revenue, gross profit and operating profit, and add the outputs here.

## Business impact
Measured impact: none was supplied, so none is claimed. Expected benefit: once the inputs exist, management can see margin by product and by period.

## Evidence
Evidence: user-supplied README, 2026-11-11, sales section only. No profit query output was supplied.

## Verification status
PENDING EVIDENCE


## Business question
Are high-revenue products necessarily high-profit products?

## Business context
A product can sell a lot at a low margin, or sell less at a high margin. Revenue ranking and profit ranking are different rankings, and only cost data can tell them apart.

## Data required
Product revenue is in sales_product_performance, 12 rows, but the product breakdown was not supplied. Product cost was not supplied.

## Analytical approach
Rank products by revenue, then rank the same products by gross profit once COGS is known. Compare the two rankings.

## KPI definitions
Gross profit by product equals product net revenue minus product COGS. Gross profit margin by product equals product gross profit divided by product net revenue, times 100.

## Actual result
No product revenue or product profit breakdown was supplied. Result: PENDING EVIDENCE.

## Direct answer
This question cannot be answered from the supplied numbers.

## Business interpretation
Do not call a top-selling product a top-profit product until its cost is known. That mistake is common, and this file does not make it.

## Recommendation
Supply product revenue and product COGS. Then add both rankings here.

## Business impact
Measured impact: none. Expected benefit: management can protect margin, not only volume.

## Evidence
Evidence: README names sales_product_performance with 12 rows. No product rows were supplied.

## Verification status
PENDING EVIDENCE

## Next step / Related files
- Profitability analysis](../04_Business_Analytics/profitability_analysis.md)
- KPI definitions](../04_Business_Analytics/kpi_definitions.md)
- Profit drivers](02_profit_drivers_and_cost_leakage.md)
