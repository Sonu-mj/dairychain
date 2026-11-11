# Inventory Analysis

> Status: NOT IMPLEMENTED

## Purpose
This file answers what DairyChain can say about inventory and expiry from the supplied sources, which is that it cannot say anything yet. It is for a reader who must not mistake a planned topic for a finding.

## In this file
- Question
- Why it matters
- Data used
- Method
- Result
- What it means
- What to do next

## Question
What inventory is available, which lots are near expiry, and is stock issued first-expired, first-out?

## Why it matters
Dairy stock expires. Stock that is not tracked can expire unsold, be issued in the wrong order, or disagree with the recorded movements. Each of those is a direct financial loss.

## Data used
No inventory tables, lots, movements or expiry dates were named in the README. No inventory Gold table is listed. Status: NOT IMPLEMENTED in the supplied README scope.

## Method
The method, when inventory data exists, is: reconcile Opening stock plus Signed movement ledger equals Current stock; list lots by expiry date for FEFO, first-expired, first-out; and flag lots near expiry and slow-moving stock. The illustrative FEFO ordering query from the brief is in [../07_AI_Assisted_Development/sql_development.md](../07_AI_Assisted_Development/sql_development.md). Ordering alone is not allocation, and allocation needs a transaction.

## Result
No inventory result is reported. No stock, lot, expiry or movement number was supplied.

## What it means
No inventory claim can be made for DairyChain from the supplied sources. Any inventory finding in a review of this project would need new evidence.

## What to do next
Supply inventory lot and movement tables, with product, quantity, unit, expiry date and movement type. Then run the reconciliation, the FEFO list and the expiry-risk list, and add the outputs here.

## Next step / Related files
- Q and A inventory](../05_Business_Questions_and_Answers/08_inventory_and_expiry.md)
- Data dictionary](../02_System_Architecture/data_dictionary.md)
- SQL development](../07_AI_Assisted_Development/sql_development.md)
