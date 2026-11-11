# Business Questions and Answers - Overview

> Status: PARTIALLY VERIFIED

## Purpose
This file is the index for the 13 question files in this folder. It is for a reader who wants to find one question, read its method and result, and check its verification status without reading the whole set.

## In this file
- How each file is structured
- The 13 files
- Status labels
- What is not answered here
- The 20 business questions (Source 13)

## How each file is structured
Every question follows the same order: business question, business context, data required, analytical approach, KPI definitions, actual result, direct answer, business interpretation, recommendation, business impact, evidence, verification status. A result without an interpretation is not left standing, and an interpretation without an evidence status is not left standing.

## The 13 files
1. [01_profitability_questions.md](01_profitability_questions.md) - Profitability.
2. [02_profit_drivers_and_cost_leakage.md](02_profit_drivers_and_cost_leakage.md) - Profit drivers and cost leakage.
3. [03_outlet_performance.md](03_outlet_performance.md) - Outlet performance.
4. [04_product_performance.md](04_product_performance.md) - Product performance and profitability.
5. [05_procurement_and_supplier_analysis.md](05_procurement_and_supplier_analysis.md) - Procurement and supplier analysis.
6. [06_production_efficiency.md](06_production_efficiency.md) - Production efficiency and yield.
7. [07_wastage_and_returns.md](07_wastage_and_returns.md) - Wastage and returns.
8. [08_inventory_and_expiry.md](08_inventory_and_expiry.md) - Inventory and expiry risks.
9. [09_sales_and_demand.md](09_sales_and_demand.md) - Sales and demand patterns.
10. [10_expense_analysis.md](10_expense_analysis.md) - Operating expense analysis.
11. [11_energy_and_operations.md](11_energy_and_operations.md) - Energy and operational analysis.
12. [12_anomaly_and_irregularity_findings.md](12_anomaly_and_irregularity_findings.md) - Anomaly and unusual-pattern analysis.
13. [13_management_recommendations.md](13_management_recommendations.md) - Management recommendations.
## How to read status labels
- VERIFIED: the fact is stated in the user-supplied README or brief and is copied exactly.
- PARTIALLY VERIFIED: part of the claim is in the supplied sources, part still needs source evidence.
- PENDING EVIDENCE: the claim needs a source file, query output, test output or screenshot before it can be trusted.
- NOT IMPLEMENTED: the supplied README does not describe this as part of DairyChain.
## The 20 business questions (Source 13)
Source: the user-supplied "DairyChain - Business Questions and Analytical Requirements" document (Source 13, 2026-11-11, 12 sections). It defines 20 business questions to be answered from the PostgreSQL database and Power BI model. Each question names a business objective, required information, relevant database table, expected output, business interpretation, and calculation considerations. The SQL implementations are documented separately in BUSINESS_QUESTION_SOLUTIONS.md, which was NOT supplied, so no SQL solution is verified for any of the 20 questions yet. Query results are now VERIFIED from the model data (Source 23) for PR-01, PR-04, PR-05, QL-01, QL-04, PRD-01, PRD-02, PRD-03, PRD-04, S-01, S-02, S-03, S-04, S-05. PR-03 is now PARTIALLY VERIFIED from the Page 2 screenshot (Source 24, district ranking only, exact litres not readable) and S-06 is now PARTIALLY VERIFIED from the Page 1 and Page 4 screenshots (Source 24, trend shape only, exact daily rows not supplied). Still PENDING EVIDENCE: PR-02, QL-02, QL-03, QL-05, and the exact values for PR-03 and S-06.

### Distribution
| Business area | Number of questions |
|---|---:|
| Procurement | 5 |
| Quality | 5 |
| Production | 4 |
| Sales | 6 |
| **Total** | **20** |

### Consolidated register
| ID | Business question | Area | Primary source |
|---|---|---|---|
| PR-01 | What is the total quantity of milk procured? | Procurement | Procurement quality |
| PR-02 | Which suppliers contribute the highest milk volume? | Procurement | Supplier performance |
| PR-03 | Which supplier districts contribute the most milk? | Procurement | Procurement quality |
| PR-04 | What is the average milk quantity per batch? | Procurement | Procurement quality |
| PR-05 | How does procurement vary across shifts? | Procurement | Procurement quality |
| QL-01 | What percentage of procurement batches are rejected? | Quality | Procurement quality |
| QL-02 | Which suppliers have the highest rejection rates? | Quality | Supplier performance and procurement quality |
| QL-03 | Which collection centres have the highest rejected milk volume? | Quality | Collection centre performance |
| QL-04 | What are the most common rejection reasons? | Quality | Procurement quality |
| QL-05 | How do fat and SNF differ between accepted and rejected milk? | Quality | Procurement quality |
| PRD-01 | How many production batches were processed? | Production | Production performance |
| PRD-02 | How much raw milk was processed? | Production | Production performance |
| PRD-03 | What is the average production duration? | Production | Production performance |
| PRD-04 | What is finished output by product and unit? | Production | Production performance |
| S-01 | What is the total sales revenue? | Sales | Sales daily summary |
| S-02 | Which products generate the highest revenue? | Sales | Sales product performance |
| S-03 | How are orders distributed across categories? | Sales | Sales product performance |
| S-04 | What is the quantity fulfilment rate? | Sales | Sales daily summary |
| S-05 | How many orders were delivered, partial, or cancelled? | Sales | Sales daily summary |
| S-06 | How does revenue change over time? | Sales | Sales daily summary |

The 20 questions are placed in full in their area files: PR-01 to PR-05 and QL-01 to QL-05 in [05_procurement_and_supplier_analysis.md](05_procurement_and_supplier_analysis.md), PRD-01 to PRD-04 in [06_production_efficiency.md](06_production_efficiency.md), S-01 to S-06 in [09_sales_and_demand.md](09_sales_and_demand.md). Each question is placed in full in one file only and cross-linked from the other files, not duplicated.

### How these questions support business decisions
| Business area | Potential decision support |
|---|---|
| Procurement | Understand milk collection volume, supplier contribution, and shift patterns |
| Quality | Identify rejection patterns and suppliers or centres requiring investigation |
| Production | Monitor processing activity, input volume, production duration, and output |
| Sales | Understand revenue, product contribution, order fulfilment, and sales trends |

These analyses support investigation and decision-making. They do not automatically establish the cause of a business problem or prescribe an operational action. The 20 questions do not cover profit: no COGS, discounts, returns, or operating expenses were supplied, so no profit answer is given in this set. See [01_profitability_questions.md](01_profitability_questions.md).

## Verified numbers used in this file
All numbers below come only from the user-supplied README, 2026-11-11, not independently verified against source code.
- Source: 10 CSV files, 99,584 total records.
- Bronze: ingested source data in PostgreSQL. Silver: 10 cleaned tables. Gold: 6 tables.
- Gold tables: procurement_quality_summary 18,000; collection_centre_performance 20; supplier_performance 200; production_performance 4,000; sales_product_performance 12; sales_daily_summary 364. Row counts VERIFIED by Source 19 (live database COUNT(*), user-supplied screenshot 2026-11-11, total 22,596).
- Procurement: 18,000 batches, 15,689 accepted, 2,311 rejected, batch rejection 12.84 percent, total milk 8,758,507.64 L, rejected milk 1,117,247.35 L, volume rejection 12.76 percent.
- Production: 4,000 batches. Finished litre-based 1,484,135.25 L, byproduct litre-based 466,514.75 L, finished kg-based 266,416.65 kg, byproduct kg-based 402,413.85 kg. Litre and kg must stay separate.
- Sales: revenue Rs 26,734,294.03, 14,000 orders, quantity ordered 181,804, quantity fulfilled 161,036.41, delivered 11,166, partially delivered 2,227, cancelled 607.
- Intended period, to verify: 1 Nov 2025 to 31 Oct 2026, Asia/Kolkata, INR.

## Next step / Related files
- Analytics methodology](../04_Business_Analytics/analytics_methodology.md)
- Key findings](../06_Business_Findings_and_Impact/key_findings.md)
- Guided tour](../README.md)
