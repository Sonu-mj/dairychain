# Wastage and Returns

> Status: NOT IMPLEMENTED

## Purpose
This file answers what DairyChain can say about wastage and returns, which is that neither is described in the supplied README scope. It is for a reader who needs the method kept ready, without an invented answer.

## In this file
- How much wastage occurs, and what is it worth?
- How do returns affect net revenue?

## Business question
How much wastage occurs, and what is its financial value?

## Business context
Wastage reduces saleable product and creates avoidable cost. Its value depends on quantity, product and the stage where it happened.

## Data required
No wastage table, quantity, category, reason, product, batch or value was named in the README. No wastage Gold table is listed.

## Analytical approach
When wastage data exists: sum wastage quantity by product, batch, category and reason, value it at the relevant cost, and divide by the appropriate total quantity basis for the wastage rate.

## KPI definitions
Wastage rate equals (Wastage quantity / Appropriate total quantity basis) x 100.

## Actual result
No wastage result was supplied. Result: NOT IMPLEMENTED.

## Direct answer
No wastage amount, rate or value can be given for DairyChain.

## Business interpretation
Wastage is a real dairy risk, but it is not a DairyChain finding in the supplied sources. Claiming a wastage number here would be invention.

## Recommendation
Supply wastage records with quantity, unit, category, reason, product, batch and date. Then add the ranking and the value here.

## Business impact
Measured impact: none. Expected benefit: a wastage view would show which stage to investigate first.

## Evidence
Evidence: none supplied. README scope is procurement, quality, production and sales.

## Verification status
NOT IMPLEMENTED


## Business question
How do returns affect net revenue?

## Business context
Returns reduce net revenue, create handling cost and affect inventory. Not every returned item is a complete loss, because some stock may be recoverable.

## Data required
No returns table, quantity, value, reason or recoverable amount was named in the README. Sales returns as a field were not supplied.

## Analytical approach
When returns data exists: separate returned sales value, refund value, recoverable inventory and actual loss. Calculate the return rate as returned quantity divided by relevant sold quantity, times 100. Do not double-count a return as both lost revenue and lost stock.

## KPI definitions
Return rate equals (Returned quantity / Relevant sold quantity) x 100. Net revenue equals Gross sales minus Discounts minus Sales returns.

## Actual result
No returns result was supplied. Result: NOT IMPLEMENTED.

## Direct answer
No returns impact can be given for DairyChain.

## Business interpretation
Returns are not the same as cancelled orders. Cancelled orders are supplied in sales, 607 orders, and are not returns. Do not use the cancelled count as a returns number.

## Recommendation
Supply returns records with product, quantity, value, reason, refund and recoverable stock. Then calculate net revenue with returns included.

## Business impact
Measured impact: none. Expected benefit: a returns view would show which products or operations need attention.

## Evidence
Evidence: none supplied.

## Verification status
NOT IMPLEMENTED

## Next step / Related files
- Sales analysis](../04_Business_Analytics/sales_analysis.md)
- Profitability analysis](../04_Business_Analytics/profitability_analysis.md)
- Inventory and expiry](08_inventory_and_expiry.md)
