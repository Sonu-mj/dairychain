# Anomaly and Irregularity Findings


## Purpose
This file answers which unusual patterns were found in DairyChain, and which patterns are only possible checks until the breakdowns arrive. It is for a reader who needs anomalies separated from normal variation.

## In this file
- What unusual patterns are in the supplied totals?
- What checks should run on the breakdowns?

## Business question
What unusual patterns are visible in the supplied totals?

## Business context
An anomaly is a value that does not fit the pattern of the rest of the data. A total alone can suggest where to look, but it cannot prove an anomaly in a single batch, supplier or day.

## Data required
Supplied totals: procurement, production and sales as listed in the README. No batch, supplier, centre, product or daily rows were supplied.

## Analytical approach
Check the totals for internal consistency first: accepted plus rejected equals total batches; status counts add to total orders; Gold counts match the README. Then, when rows arrive, flag batches, suppliers, centres, products and days that sit far from their group.

## KPI definitions
Batch rejection rate, volume rejection rate, fulfilment rate and delivered share, as defined in the KPI file.

## Actual result
Consistency checks pass on the supplied totals: 15,689 plus 2,311 equals 18,000; 11,166 plus 2,227 plus 607 equals 14,000. No batch, supplier, centre, product or daily anomaly was supplied.

## Direct answer
No row-level anomaly can be reported. The totals are internally consistent, and that is the only anomaly finding the supplied numbers support.

## Business interpretation
Consistency is a useful check, but it is not the same as finding an outlier. A consistent total can still hide a bad batch, so the row-level check is still needed.

## Recommendation
Supply the batch, supplier, centre, product and daily rows. Then run the outlier checks and add the flagged rows here with their values.

## Business impact
Measured impact: none. Expected benefit: flagged rows would show where to investigate first.

## Evidence
Source: README totals.

## Business question
Which operational variations need management attention?

## Business context
Variation that is large, repeated or linked to a cost needs attention. Variation that is small and random does not.

## Data required
Only period totals were supplied. No variation by supplier, centre, product, shift or day was supplied.

## Analytical approach
When rows arrive: compare rejection rate by supplier and centre, yield by batch and shift, and fulfilment by product and day. Look for a repeated pattern, not a single high or low value.

## KPI definitions
Rejection rate, yield and fulfilment rate by group, as defined in the KPI file.


## Business interpretation
Naming a supplier, centre or product here would be invention. The question is kept open until the breakdowns arrive.

## Recommendation
Supply the breakdowns listed in the question above, with reasons where the data holds them.

## Business impact
Measured impact: none. Expected benefit: a repeated pattern would direct the first investigation.


## Next step / Related files
- Procurement analysis](../04_Business_Analytics/procurement_analysis.md)
- Sales analysis](../04_Business_Analytics/sales_analysis.md)
- Management recommendations](13_management_recommendations.md)
