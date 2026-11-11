# DairyChain Documentation - Guided Tour


## Purpose
This file is the guided tour for the whole DairyChain documentation set. It is for a first-time reader, a reviewer, or an interviewer who wants to follow the project end to end in story order, from the business problem to the evidence.

## In this file
- Business Problem
- Requirements
- System Design
- Data Engineering
- Python and SQL
- Business Analytics
- Questions and Actual Answers
- Business Findings
- Management Recommendations
- AI-assisted development, Testing, Debugging, Security, Performance, Engineering Decisions

## Business Problem
Start here to learn what problem DairyChain solves and why a dairy business needs joined-up procurement, quality, production and sales data. Read [00_Project_Overview/project_summary.md](00_Project_Overview/project_summary.md) for the one-page summary, and [00_Project_Overview/business_context.md](00_Project_Overview/business_context.md) for the dairy workflow.

## Requirements
Read [01_Business_Requirements/business_requirements.md](01_Business_Requirements/business_requirements.md) to learn what the business asked for, [01_Business_Requirements/functional_requirements.md](01_Business_Requirements/functional_requirements.md) for what the system must do, [01_Business_Requirements/non_functional_requirements.md](01_Business_Requirements/non_functional_requirements.md) for quality and limits, and [01_Business_Requirements/assumptions_and_constraints.md](01_Business_Requirements/assumptions_and_constraints.md) for what was assumed and what was left out.

## System Design
Read [02_System_Architecture/system_architecture.md](02_System_Architecture/system_architecture.md) to learn how the layers fit together, [02_System_Architecture/data_flow.md](02_System_Architecture/data_flow.md) to follow a record from CSV to Power BI, [02_System_Architecture/database_design.md](02_System_Architecture/database_design.md) for the layer design, and [02_System_Architecture/data_dictionary.md](02_System_Architecture/data_dictionary.md) for the tables and columns that are actually named in the supplied sources.

## Data Engineering
Read [03_Data_Engineering/data_ingestion.md](03_Data_Engineering/data_ingestion.md), [03_Data_Engineering/data_validation.md](03_Data_Engineering/data_validation.md), [03_Data_Engineering/data_cleaning.md](03_Data_Engineering/data_cleaning.md), [03_Data_Engineering/transformation_logic.md](03_Data_Engineering/transformation_logic.md), [03_Data_Engineering/bronze_silver_gold_layers.md](03_Data_Engineering/bronze_silver_gold_layers.md) and [03_Data_Engineering/pipeline_execution.md](03_Data_Engineering/pipeline_execution.md) to learn how raw CSV data becomes clean, report-ready tables.

## Python and SQL
Read [07_AI_Assisted_Development/python_development.md](07_AI_Assisted_Development/python_development.md) and [07_AI_Assisted_Development/sql_development.md](07_AI_Assisted_Development/sql_development.md) to learn how Python and SQL were used, with the illustrative examples from the brief. The method sections in [04_Business_Analytics/analytics_methodology.md](04_Business_Analytics/analytics_methodology.md) show how the same tools answer business questions.

## Business Analytics
Read [04_Business_Analytics/analytics_methodology.md](04_Business_Analytics/analytics_methodology.md) for the method, [04_Business_Analytics/kpi_definitions.md](04_Business_Analytics/kpi_definitions.md) for every KPI name and formula used in the same way everywhere, then [04_Business_Analytics/procurement_analysis.md](04_Business_Analytics/procurement_analysis.md), [04_Business_Analytics/production_analysis.md](04_Business_Analytics/production_analysis.md) and [04_Business_Analytics/sales_analysis.md](04_Business_Analytics/sales_analysis.md) for the three areas with supplied numbers.

## Questions and Actual Answers
Read [05_Business_Questions_and_Answers/README.md](05_Business_Questions_and_Answers/README.md) and the 13 numbered files in that folder to learn each question, the method, and the actual result.

## Business Findings
Read [06_Business_Findings_and_Impact/executive_summary.md](06_Business_Findings_and_Impact/executive_summary.md) and [06_Business_Findings_and_Impact/key_findings.md](06_Business_Findings_and_Impact/key_findings.md) to learn what the supplied numbers actually support, and what they do not support.

## Management Recommendations
Read [06_Business_Findings_and_Impact/recommendations.md](06_Business_Findings_and_Impact/recommendations.md) and [05_Business_Questions_and_Answers/13_management_recommendations.md](05_Business_Questions_and_Answers/13_management_recommendations.md) to learn what management could investigate next, with each recommendation tied to its source.

## AI-assisted development, Testing, Debugging, Security, Performance, Engineering Decisions
Read [07_AI_Assisted_Development/README.md](07_AI_Assisted_Development/README.md) for the AI workflow, [09_Testing_and_Validation/testing_strategy.md](09_Testing_and_Validation/testing_strategy.md) for testing, [08_Debugging_and_Troubleshooting/debugging_methodology.md](08_Debugging_and_Troubleshooting/debugging_methodology.md) for debugging, [10_Security_and_Reliability/security_review.md](10_Security_and_Reliability/security_review.md) for security, [11_Performance_Optimization/query_optimization.md](11_Performance_Optimization/query_optimization.md) for performance, and [12_Engineering_Decisions/README.md](12_Engineering_Decisions/README.md) for the decisions and the approaches that were rejected.

## Numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently shown against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts from Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Intended period: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.
## Next step / Related files
- Root README](../README.md)
- Check file](../VERIFICATION_AND_MISSING_INFO.md)
