# Limitations and Future Analysis

> Status: PARTIALLY VERIFIED

## Purpose
This file answers what limits DairyChain today and what analysis could follow once the missing evidence arrives. It is for a reader who needs the boundary of the current work and a realistic next step.

## In this file
- Limitations
- Current scope limits
- Power BI model limitations (Source 11)
- Future analysis
- Future architecture improvements
- Power BI model future improvements (Source 11)
- Future improvements from the README

## Limitations
- No source code, SQL, CSVs, tests or Power BI file were supplied, so no code, query or test claim is verified from source.
- Profit cannot be calculated, because COGS, discounts, returns and operating expenses were not supplied.
- Yield cannot be calculated as a single figure. Raw milk input total is now VERIFIED from the model data (Source 23): 2,600,000.0 L. For litre batches finished plus byproduct equals the input exactly; for kg batches the outputs are in kg while the input is recorded in litres, so no comparable yield exists without a density conversion, which was not supplied.
- No supplier, centre, outlet or daily ranking can be given, because the breakdown rows were not supplied. Product ranking is now supplied from the model data (Source 23): Pure Cow and Buffalo Ghee is the top revenue product at Rs 5,986,642.50.
- Wastage, returns, inventory, expenses and energy are not in the README scope, so no finding is given for them.
- The intended period, 1 Nov 2025 to 31 Oct 2026, is now VERIFIED for the data range from the model data (Source 23): procurement timestamps run 2025-11-01 to 2026-10-31; sales daily order_date runs 2025-11-02 to 2026-10-31.
- Column names, types, and nullability are now VERIFIED by Source 18 (238 columns). Keys and constraints are VERIFIED ABSENT by Sources 20 and 21 (0 rows). No DDL was supplied, so no DDL is claimed.
- Silver cleaning rules are not verified, because no rule list or before-and-after counts were supplied.
- Power BI relationships are now VERIFIED by Source 23 (pbixray): only 1 relationship exists in the model, `gold procurement_quality_summary[supplier_id]` to `gold supplier_performance[supplier_id]`, M:1, Single, active; none of the 10 intended dimension relationships exists. The exact source expressions for procurement_date and production_date are also VERIFIED as DAX calculated columns. Source 11 explains that procurement_date and production_date are date-level fields derived from the relevant timestamps.

## Current scope limits
This architecture describes the implemented project workflow at a logical level. The following capabilities should not be claimed without additional implementation evidence. Status: NOT IMPLEMENTED.

- Cloud deployment.
- Scheduled pipeline execution.
- Apache Airflow orchestration.
- Incremental data loading.
- Real-time data ingestion.
- Automated database backups.
- Production monitoring and alerting.
- CI/CD deployment.
- Automated schema migration.

These are potential future improvements, not established components of the current architecture.

## Power BI model limitations (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 12). The documented model contains summary tables at different aggregation levels. This is suitable for the current reporting requirements but creates analytical limitations.

- A date filter cannot narrow product-level sales summaries without a date-product-level source table.
- Product filters cannot narrow daily sales revenue without product-level daily sales data or an appropriate bridge.
- Supplier summaries do not provide the same detail as individual procurement batches.
- Collection-centre summaries cannot replace procurement-level detail.
- Some cross-analysis questions require more detailed source data than the current Gold tables expose.

These limitations should be explained rather than hidden by creating relationships that do not represent genuine business relationships.

## Future analysis
Once the missing evidence arrives, the next analysis is: profit by product and period; yield by batch, product and shift; rejection by reason, supplier and centre; fulfilment by reason, product and day; and expense by category. Each analysis must follow the Q and A format, with its query output kept as evidence.

## Future architecture improvements
Potential future improvements, prioritised by actual operational need rather than added only to increase the technology stack:

1. Introduce a workflow orchestrator to manage pipeline execution and dependencies.
2. Implement incremental loading when source data and change tracking requirements support it.
3. Add automated data-quality checks and validation reports.
4. Implement structured logging and pipeline failure notifications.
5. Introduce role-based database access for different application responsibilities.
6. Add automated tests for transformations and business metrics.
7. Explore cloud-hosted database and reporting infrastructure.

## Power BI model future improvements (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 13). These are potential improvements and should not be described as implemented components of the current model. Status: NOT IMPLEMENTED.

1. A daily product sales fact table containing both date and product identifiers.
2. A more detailed order-level sales table for distinct order analysis.
3. Dedicated date-role handling if multiple date definitions are required.
4. A consistent business-key and dimension design across the reporting model.
5. Automated checks for duplicate dimension keys and unmatched fact records.
6. Documentation of all active relationships, cardinality, and filter direction.

## Future improvements from the README
The README lists these as future possibilities, not current features: automated and incremental ingestion, pipeline orchestration with Apache Airflow, automated data quality checks, pipeline failure logging and monitoring, cloud-based storage and processing, more detailed forecasting, advanced supplier and production analysis, and automated testing and deployment. Status: NOT IMPLEMENTED.

## Next step / Related files
- [Executive summary](executive_summary.md)
- [Verification file](../../VERIFICATION_AND_MISSING_INFO.md)
- [Implementation status](../13_Project_Evidence/implementation_status.md)
