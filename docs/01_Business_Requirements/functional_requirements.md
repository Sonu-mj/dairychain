# Functional Requirements


## Purpose
This file answers what the system must do, function by function. It is for a developer or reviewer who wants to check each function against what was supplied.

## In this file
- Ingestion
- Storage and cleaning
- Transformation
- Analysis and reporting

## Ingestion
- Read 10 source CSV files into PostgreSQL. Total supplied record count: 99,584.
- Keep the ingested source data in the Bronze layer before any cleaning changes it.

## Storage and cleaning
- Hold 10 cleaned and structured tables in the Silver layer.
- Apply cleaning and validation rules that are documented separately.

## Transformation
- Build 6 Gold analytical tables: procurement_quality_summary, collection_centre_performance, supplier_performance, production_performance, sales_product_performance, sales_daily_summary. Record counts are in the shown numbers block below.

## Analysis and reporting
- Answer procurement, quality, production and sales questions with SQL aggregations, joins, CTEs, conditional aggregation and date-based analysis.
- Report in Power BI on four pages: Executive Overview, Procurement and Quality Analysis, Production Performance Analysis, and Sales Analysis. Only the visuals listed in the README are claimed for each page. See [../04_Business_Analytics/analytics_methodology.md](../04_Business_Analytics/analytics_methodology.md).
## Numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently shown against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts from Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Intended period: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Non-functional requirements](non_functional_requirements.md)
- Bronze Silver Gold](../03_Data_Engineering/bronze_silver_gold_layers.md)
- Data dictionary](../02_System_Architecture/data_dictionary.md)
