# Business Requirements


## Purpose
This file answers what business problems DairyChain must solve and what a good answer looks like for each one. It is for a manager or reviewer who wants the business need before any technical detail.

## In this file
- The core problem
- Requirements by business area
- How success is judged

## The core problem
A dairy business can see each stage on its own and still miss where losses occur. Procurement, quality, production and sales are connected, so a decision in one stage changes the result in the next. The business needs one joined view that shows where milk is lost, which suppliers and centres need attention, how production performs, and which products contribute most to revenue.

## Requirements by business area
- Procurement: show total milk procured, cost, and performance by supplier, district and collection centre.
- Quality: show accepted and rejected milk, rejection rates, fat and SNF, and rejection reasons.
- Production: show batches, raw milk input, finished output, byproducts and duration, by shift and product.

## How success is judged
Success is a report a manager can act on: a number, the method behind it, and the source it came from. A number without a method or a source is not a finding in this documentation set. Every Q and A file in folder 05 follows that rule.
## Numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently shown against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts from Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Intended period: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Functional requirements](functional_requirements.md)
- Project summary](../00_Project_Overview/project_summary.md)
- Analytics methodology](../04_Business_Analytics/analytics_methodology.md)
