# Security Review

> Status: PENDING EVIDENCE

## Purpose
This file answers what security DairyChain needs, what is implemented, and what is only recommended. It is for a reader who must not mistake a recommendation for a control that exists. Its sources are the Master Project Brief and sections 1, 2, 7 and 10 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5).

## In this file
- Core principle
- Why reviewing AI-generated code matters
- Implemented controls
- Recommended controls
- Security and code review checklist
- Known limitations and evidence requirements
- What was not supplied

## Core principle
Source: "Code Review and Security Practices", section 1. AI can help generate code quickly, but generated code is not automatically correct, secure, or suitable for an existing project. During DairyChain development, it was important to distinguish between code that merely executes and code that correctly implements the intended business requirement.

> Code should be understood, reviewed, executed, and verified before it is trusted.

This document distinguishes between recommended engineering practices and controls that must be confirmed in the actual project code. It does not claim that every security measure below has already been implemented.

## Why reviewing AI-generated code matters
Source: "Code Review and Security Practices", section 2.

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

## Implemented controls
No security control can be listed as implemented from the supplied sources, because no security configuration, access record or review output was supplied. Status: PENDING EVIDENCE for every control below.

## Recommended controls
- Keep credentials out of code and out of the repository. Use environment variables.
- Give the database user only the privileges it needs.
- Validate file and input data before loading it.
- Log errors without logging credentials or sensitive business records.
- Plan backup and recovery for the PostgreSQL database.

## Security and code review checklist
Source: "Code Review and Security Practices", section 7. Use this checklist when reviewing a new or AI-assisted implementation. These are items to check, not completed items. No item below is marked complete, because no review record was supplied.

### Python

- [ ] Required files and columns are validated.
- [ ] Data types are appropriate for the operations.
- [ ] Missing values are handled according to business rules.
- [ ] Duplicate records are investigated.
- [ ] Exceptions are not silently ignored.
- [ ] File paths and configuration are handled appropriately.
- [ ] Logs do not expose credentials or sensitive information.

### PostgreSQL and SQL

- [ ] SQL statements use parameters for untrusted values.
- [ ] Joins are checked for duplicate multiplication.
- [ ] Aggregation levels match the business requirement.
- [ ] NULL handling is understood.
- [ ] Date filters use appropriate boundaries.
- [ ] Division-by-zero scenarios are handled.
- [ ] Database privileges are limited to necessary operations.

### Power BI

- [ ] DAX measures match their business definitions.
- [ ] Relationships use the correct keys.
- [ ] Filter propagation is checked.
- [ ] Slicer interactions are tested.
- [ ] Different measurement units are not incorrectly combined.
- [ ] Dashboard values are reconciled with database results.

### Git and project configuration

- [ ] Passwords and access tokens are not committed.
- [ ] `.env` files are excluded from Git.
- [ ] A safe configuration example is provided where needed.
- [ ] Unnecessary temporary files are excluded.
- [ ] Dependencies are documented.
- [ ] No confidential database exports are committed accidentally.

## Known limitations and evidence requirements
Source: "Code Review and Security Practices", section 10. This document describes the security review practices that should guide DairyChain development. The following claims require additional project evidence before they can be described as completed controls:

- Database credentials are stored securely.
- All SQL operations use parameterised queries.
- Database roles follow least-privilege access.
- All input files are validated before ingestion.
- Automated security checks are executed.
- Power BI calculations have been independently reconciled.
- All code has undergone a formal security review.

A checklist item should only be marked complete after the corresponding implementation or test has been inspected.

## What was not supplied
No credential setup, privilege list, access control record or backup plan was supplied. Do not claim any of them as implemented. Add each control here only when its configuration or output can be shown.

## Next step / Related files
- [SQL injection prevention](sql_injection_prevention.md)
- [Credential management](credential_management.md)
- [Access control](access_control.md)
- [Transaction and data integrity](transaction_and_data_integrity.md)
- [Code review](../07_AI_Assisted_Development/code_review.md)
