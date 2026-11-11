# Assumptions and Constraints

> Status: PENDING EVIDENCE

## Purpose
This file answers what was assumed, what limits the project, and what would change a result if the assumption were wrong. It is for a reader who wants the boundary of every claim.

## In this file
- Assumptions
- Constraints
- What would change the findings

## Assumptions
- The 10 CSV files are the complete source for the period. Status: PENDING EVIDENCE. No file list was supplied.
- The intended period is 1 Nov 2025 to 31 Oct 2026, in Asia/Kolkata, in INR. Status: INTENDED, TO VERIFY.
- Gold record counts in the README are the result of the stated pipeline. Status: PENDING EVIDENCE against source files.

## Constraints
- No source code, SQL, CSVs, tests or Power BI file were found on the VM or on github.com/Sonu-mj on 2026-11-11. All schema, code and test claims in this set are therefore marked PENDING EVIDENCE.
- The earlier brief reported a PostgreSQL authentication error during database creation. Status: RESOLVED by Source 17. A successful connection is now verified (localhost, port 5432, user postgres, database dairychain, server PostgreSQL 18.6). A successful load run must still not be claimed without a run log.

## What would change the findings
- If the period, the CSV list, or the unit handling differs from the README, the procurement, production and sales totals change with it. That is why the verification file lists exactly what is still needed.

## Next step / Related files
- Objectives and scope](../00_Project_Overview/objectives_and_scope.md)
- Implementation status](../13_Project_Evidence/implementation_status.md)
- Verification file](../../VERIFICATION_AND_MISSING_INFO.md)
