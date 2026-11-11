# Inventory and Expiry Risks

> Status: NOT IMPLEMENTED

## Purpose
This file answers what inventory is at risk of expiry in DairyChain, which is that no inventory data was supplied. It is for a reader who needs the reconciliation and FEFO method, without a stock number being invented.

## In this file
- What inventory is available, and what is at risk?
- Is stock issued first-expired, first-out?

## Business question
What inventory is currently available, and which lots are at risk of expiry?

## Business context
Dairy stock expires, so available stock, expiry dates and slow movement decide what can still be sold and what will be lost.

## Data required
No inventory lots, stock balances, movements or expiry dates were named in the README. No inventory Gold table is listed.

## Analytical approach
When inventory data exists: reconcile Opening stock plus Signed movement ledger equals Current stock; list lots by expiry date; flag lots near expiry and slow-moving products.

## KPI definitions
Inventory balance equals Opening stock plus Signed stock movements.

## Actual result
No inventory result was supplied. Result: NOT IMPLEMENTED.

## Direct answer
No stock level, expiry list or slow-movement finding can be given for DairyChain.

## Business interpretation
An inventory claim without lots and movements would be a guess. This file keeps the method and the evidence list, and leaves the answer open.

## Recommendation
Supply inventory lot and movement tables with product, quantity, unit, expiry date and movement type.

## Business impact
Measured impact: none. Expected benefit: an expiry list would let management sell or use at-risk stock first.

## Evidence
Evidence: none supplied.

## Verification status
NOT IMPLEMENTED


## Business question
Is inventory issued according to FEFO, first-expired, first-out?

## Business context
FEFO means the lot that expires first is used first. It reduces expiry loss, but only if allocation follows the same order as selection.

## Data required
No lots, expiry dates or allocation records were supplied.

## Analytical approach
Select eligible lots ordered by expiry date, then lot id, as in the illustrative FEFO query in the SQL development file. Then check whether allocation actually followed that order, in a transaction that is safe for concurrent updates. Selection alone is not allocation.

## KPI definitions
FEFO ordering: expiry date ascending, then lot id ascending, for lots with available quantity above zero and expiry date on or after the current date.

## Actual result
No FEFO result was supplied. Result: NOT IMPLEMENTED.

## Direct answer
FEFO compliance cannot be judged for DairyChain from the supplied sources.

## Business interpretation
The brief is clear on this point: identifying eligible lots is not the same as allocating stock. Both steps need evidence.

## Recommendation
Supply lot and allocation records, with the transaction logic used for stock updates.

## Business impact
Measured impact: none. Expected benefit: FEFO compliance would reduce expiry loss.

## Evidence
Evidence: none supplied. Illustrative query only, from the brief.

## Verification status
NOT IMPLEMENTED

## Next step / Related files
- Inventory analysis](../04_Business_Analytics/inventory_analysis.md)
- SQL development](../07_AI_Assisted_Development/sql_development.md)
- Data dictionary](../02_System_Architecture/data_dictionary.md)
