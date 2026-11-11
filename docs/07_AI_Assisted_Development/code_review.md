# Code Review


## Purpose
This file answers how to review AI-suggested code before it is trusted in DairyChain. It is for a developer who needs a checklist that catches wrong fields, double-counting and unsafe SQL. Its sources are the Master Project Brief checklist, section 8 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, and sections 1, 2, 8, 9 and 11 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5).

## In this file
- Core principle
- Why reviewing AI-generated code matters
- The review criteria table from the methodology
- The checklist from the brief
- Representative prompt: reviewing SQL logic
- How AI can help with code review
- How to evaluate a suggested correction
- Key learning
- How to use it
- What a failed review means
- Notes

## Core principle
AI can help generate code quickly, but generated code is not automatically correct, secure, or suitable for an existing project. During DairyChain development, it was important to distinguish between code that merely executes and code that correctly implements the intended business requirement.

> Code should be understood, reviewed, executed, and shown before it is trusted.

This document distinguishes between recommended engineering practices and controls that must be confirmed in the actual project code. It does not claim that every security measure below has already been implemented.

## Why reviewing AI-generated code matters
AI-generated code can introduce several types of problems.

| Risk | Example |
|---|---|
| Incorrect business logic | Calculating batch rejection rate using milk volume |
| Incorrect SQL joins | Joining tables in a way that duplicates records |
| Data-quality problems | Ignoring missing values or duplicate records |
| Security weaknesses | Exposing database credentials in source code |
| SQL injection | Constructing SQL statements using untrusted input |
| Poor error handling | Hiding database or file-processing errors |
| Performance problems | Loading or processing unnecessarily large datasets |
| Maintainability issues | Repeating logic or creating unnecessarily complex code |

A successful execution does not prove that the code is correct.

## The review criteria table from the methodology
AI-generated code can contain more than syntax errors. It can also introduce incorrect business logic, insecure configuration, and maintainability problems. For DairyChain, code review should consider the following areas:

| Area | What needs to be checked |
|---|---|
| Credentials | Database passwords and secrets should not be hardcoded or committed to Git |
| Configuration | Database connections should use appropriate configuration or environment variables |
| SQL logic | Joins, filters, grouping, and calculations must match the business requirement |
| Data handling | Missing values, duplicate records, invalid data types, and unexpected values must be considered |
| Error handling | Failures should be visible and should not be silently ignored |
| Database operations | Table names, schemas, data types, and transaction behaviour must be checked |
| Maintainability | Code should be understandable and should not contain unnecessary duplication |
| Input handling | External inputs should be validated; SQL parameters should be used instead of unsafe string construction |

These are review criteria, not a claim that every listed security control has already been implemented. The final project documentation should identify which controls are actually present in the code.

## The checklist from the brief
- Does it solve the actual requirement?
- Does it use the correct fields?
- Does it preserve business logic?
- Are edge cases handled?
- Are NULLs handled correctly?
- Could JOINs duplicate financial values?
- Are transactions handled properly?
- Is the code secure?
- Does it match the existing architecture?
- Are dependencies necessary?
- Can the implementation be tested independently?

## Representative prompt: reviewing SQL logic
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 6. This is a representative prompt template, not a claim that these exact words were used in a particular review session.

> Review the following SQL query for the DairyChain analytics project.
> Check:
> 1. Whether the joins could duplicate records.
> 2. Whether the aggregation level is correct.
> 3. Whether NULL values could affect the calculation.
> 4. Whether the filters match the business requirement.
> 5. Whether the query uses the correct unit of measurement.
> Explain each potential issue separately.
> Do not assume that a query is correct just because it executes successfully.

Why this matters: a SQL query can execute successfully and still return incorrect results. For example, joining two tables with multiple matching rows can multiply records and inflate a SUM calculation. The developer must understand the relationship between the tables and the intended level of aggregation.

## How AI can help with code review
Source: "Code Review and Security Practices", section 8. AI can be asked to review code using a focused prompt. This is a representative review prompt, not a claim that these exact words were used.

> Review this code from the DairyChain project.
> Act as a Python, SQL, and data engineering code reviewer.
> Identify:
> 1. Possible logical errors.
> 2. Security weaknesses.
> 3. Incorrect SQL joins or aggregations.
> 4. Missing error handling.
> 5. Data-quality risks.
> 6. Performance and maintainability concerns.
> For every issue, explain why it is a problem and identify the affected code.
> Classify issues as critical, high, medium, or low priority.
> Suggest the smallest practical correction. Do not claim that the code is secure or correct without sufficient evidence.

AI review should be treated as an additional review aid, not a security audit or guarantee.

## How to evaluate a suggested correction
Source: "Code Review and Security Practices", section 9. A proposed correction should be evaluated using four questions:

**1. Does it fix the actual problem?**

The solution must address the root cause, not merely hide the error.

**2. Does it preserve existing behaviour?**

A small fix should not unintentionally change unrelated transformations or calculations.

**3. Does it introduce another risk?**

A correction should also be checked for security, data consistency, and maintainability.

**4. Can I check it independently?**

The correction should be executed and tested against an appropriate expected result.

## Key learning
Source: "Code Review and Security Practices", section 11. AI-assisted code development requires more than checking whether a program runs. It requires understanding the data, business logic, database structure, application configuration, and possible security risks. During DairyChain development, the important lesson was that faster code generation is useful only when it is supported by careful review and check.

> AI can suggest an implementation. The developer must be able to explain why it is appropriate, identify what could go wrong, and check that it works as intended.

## How to use it
Review the draft against the schema first, then against the business rule, then against the edge cases. Run the code and check the output against a second method.

## What a failed review means
A failed review is not a reason to accept a weaker draft. It is a reason to fix the field, the JOIN grain, the NULL handling or the transaction, and review again. The fix and the re-check are recorded in the debugging log.

## Notes
The criteria and checklist above are as user-supplied method.

## Next step / Related files
- [Debugging with AI](debugging_with_ai.md)
- [Testing with AI](testing_with_ai.md)
- [SQL injection prevention](../10_Security_and_Reliability/sql_injection_prevention.md)
- [Security review](../10_Security_and_Reliability/security_review.md)
