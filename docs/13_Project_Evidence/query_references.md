# Query References

> Status: PENDING EVIDENCE

## Purpose
This file answers which SQL queries support DairyChain and where each one lives. It is for a reader who needs to find a query, run it, and check its output.

## In this file
- What was supplied
- Illustrative queries in this set
- How to add a project query
- The 20 business questions (Source 13)

## What was supplied
No project SQL files were supplied, so no project query can be listed here with its file path and its output. Status: PENDING EVIDENCE.

## Illustrative queries in this set
The brief gives three illustrative queries, which are kept in [../07_AI_Assisted_Development/sql_development.md](../07_AI_Assisted_Development/sql_development.md): a production aggregation by product, a FEFO lot ordering query, and a parameterised psycopg query. Those are illustrations from the brief, not project queries. Do not cite them as DairyChain query outputs.

## The 20 business questions (Source 13)
Source: the user-supplied "DairyChain - Business Questions and Analytical Requirements" document (Source 13, 2026-11-11, 12 sections). It defines 20 business questions: Procurement 5 (PR-01 to PR-05), Quality 5 (QL-01 to QL-05), Production 4 (PRD-01 to PRD-04), Sales 6 (S-01 to S-06). The full register is in [../05_Business_Questions_and_Answers/README.md](../05_Business_Questions_and_Answers/README.md), and each question is placed in full in its area file in [../05_Business_Questions_and_Answers/](../05_Business_Questions_and_Answers/).

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

The corresponding SQL implementations and query results are documented separately in BUSINESS_QUESTION_SOLUTIONS.md, which was NOT supplied. No SQL solution or query output is verified for any of the 20 questions yet. Only the recorded reference values may be used as results: QL-01 18,000 / 15,689 / 2,311 / 12.84 percent, PRD-01 4,000 batches, S-01 Rs 26,734,294.03, S-05 11,166 / 2,227 / 607 / 14,000. All other questions have no supplied result yet and are marked PENDING EVIDENCE in their files. When BUSINESS_QUESTION_SOLUTIONS.md is supplied, add each solution here with its question ID, file path, Gold table, grain, full SQL, run date, and output.

## Prepared verification queries - Source 16
Source: the PDF "DairyChain PostgreSQL Codes and Outputs" (Source 16, 2026-11-11, sections 5 and 9). The PDF is a secondary reference document, not a psql transcript, so these queries are prepared queries, not executed queries, and no result is claimed for any of them. The full SQL is kept in one place only, in [../03_Data_Engineering/data_validation.md](../03_Data_Engineering/data_validation.md): the section 9 prepared verification sequence (psql connection template, current_database() / current_user / version(), schema check, Gold table inventory), and the documented SQL examples from sections 3-6 (schema creation, illustrative silver.suppliers DDL, Bronze inspection, supplier aggregation, join, type-casting, TRIM, cost-validation CASE, rejection-rate query, join-cardinality diagnostic). The catalogue and Gold row-count queries in that file were already there from Source 10; the PDF repeats them, so they are not duplicated. Do not cite any of these as DairyChain query outputs until they are run against the real database and the output is recorded here with the run date.

## How to add a project query
For each query, add: the business question it answers, the file path, the Gold table it reads, the grain, the full SQL, the date it was run, and the output. Keep the output with the query, so a reviewer can check the number in the report against the number the query returned.

## Next step / Related files
- Implementation status](implementation_status.md)
- SQL validation](../09_Testing_and_Validation/sql_validation.md)
- Verification record](verification_record.md)
