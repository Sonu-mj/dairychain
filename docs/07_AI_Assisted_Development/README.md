# AI-Assisted Development - Overview

> Status: PARTIALLY VERIFIED

## Purpose
This file is the index for the AI-assisted development folder. It is for a reader who needs to know how AI was used in DairyChain, what the developer still owned, and where each part of the method is documented. Its source is the user-supplied "AI-Assisted Development Methodology" document, 2026-11-11, used in full. That document is a statement of method and principles, not a task log, so no specific AI task, prompt, error or fix is claimed here beyond what it says.

## In this file
- The principle
- The files in this folder
- Security and code review checklist
- Limitations
- What AI did not do

## The principle
AI tools were used as development assistants, not as replacements for technical understanding or verification. The developer knows Python and SQL, and used AI to improve speed, efficiency and problem-solving, while retaining responsibility for implementation decisions. Generated code and suggestions should be reviewed, executed and validated before being treated as correct.

> AI helped accelerate development. Technical decisions, execution, verification, and responsibility remained with me.

## The files in this folder
- [development_workflow.md](development_workflow.md) - the stages table, the 6-step problem-first workflow, and the less-reliable approach against the approach used.
- [how_ai_was_used.md](how_ai_was_used.md) - purpose, project context and processing flow, the stages table, and the key learning.
- [python_development.md](python_development.md) - Python work from the methodology, with the illustrative validation example from the brief.
- [sql_development.md](sql_development.md) - the rejection-rate SQL example in full, with its 5 checks and recorded result.
- [prompt_engineering.md](prompt_engineering.md) - the focused-request principle and the representative debugging prompt template, plus the weak prompt against the better engineering prompt from the brief, Example A (vague against useful Python ingestion prompt), the recommended prompt structure, and the AI-assist against developer-responsibility table from the prompts document.
- [code_review.md](code_review.md) - the review criteria table from the methodology, plus the checklist from the brief.
- [debugging_with_ai.md](debugging_with_ai.md) - the debugging approach in full, and why targeted debugging matters.
- [testing_with_ai.md](testing_with_ai.md) - suggested, executed, passed and unverified tests, and the verification areas for Python, SQL and Power BI.
- [ai_task_log/README.md](ai_task_log/README.md) and [ai_task_log/actual_development_tasks.md](ai_task_log/actual_development_tasks.md) - the task log, the limitations, and the evidence to maintain. No task log was supplied.

## AI-assisted development decision log
The user-supplied "AI-Assisted Development Decision Log" document, 2026-11-11 (Source 7), is integrated into [ai_task_log/actual_development_tasks.md](ai_task_log/actual_development_tasks.md) and [ai_task_log/README.md](ai_task_log/README.md). It supplies the decision principles, the Accepted, Modified, Rejected, Investigating categories, the evaluation framework, the decision register format and AI-XXX record template, the rules for recording modified and rejected suggestions, and the 7 accuracy rules, summarised as a cross-reference in [testing_with_ai.md](testing_with_ai.md). Its technical example on keeping production units separate is in [../12_Engineering_Decisions/architecture_decisions.md](../12_Engineering_Decisions/architecture_decisions.md), labelled a technical design example, not an AI decision. No historical AI decisions were supplied, so the register is empty by design. Do not mark any suggestion accepted, modified, rejected, or tested until its evidence is supplied.

## AI prompts and code examples
The user-supplied "AI Prompts and Code Examples" document, 2026-11-11, is integrated into this folder as representative prompt templates and code illustrations, not as exact historical chat prompts or exact copies of the original project scripts. It covers the vague prompt against the useful prompt in [prompt_engineering.md](prompt_engineering.md), the ingestion validation example in [python_development.md](python_development.md), the business-question-to-SQL steps in [sql_development.md](sql_development.md), the SQL error and Python debugging templates in [debugging_with_ai.md](debugging_with_ai.md), the SQL logic review template in [code_review.md](code_review.md), and the Accept, Modify, Reject, Investigate decision framework in [testing_with_ai.md](testing_with_ai.md). Its Power BI and DAX section is cross-linked from [prompt_engineering.md](prompt_engineering.md) to the representative DAX measures in [../04_Business_Analytics/kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md). Those DAX measures are representative, not verified Power BI measures. Actual conversation excerpts and implementation code should replace or supplement these templates when available.

## Code review and security practices
The user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5), is integrated into this folder and into docs/10_Security_and_Reliability/. It adds the core principle that code should be understood, reviewed, executed, and verified before it is trusted, the risk table, the Python file-validation and error-handling examples in [python_development.md](python_development.md), the AI review prompt template, the four-question correction evaluation, and the key learning in [code_review.md](code_review.md). Its SQL logic review (aggregation level, joins, NULL handling, date filters, units) is in [../10_Security_and_Reliability/transaction_and_data_integrity.md](../10_Security_and_Reliability/transaction_and_data_integrity.md), its credential, SQL injection and access-control sections are in the other files in docs/10_Security_and_Reliability/, and its Power BI review table is in [../04_Business_Analytics/kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md). It distinguishes recommended practices from controls that must be confirmed in actual code, and it does not claim that every security measure in it has already been implemented.

## Security and code review checklist
Source: "Code Review and Security Practices", section 7. Use this checklist when reviewing a new or AI-assisted implementation. These are items to check, not completed items. The full checklist is also in [../10_Security_and_Reliability/security_review.md](../10_Security_and_Reliability/security_review.md).

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

## Limitations
AI assistance has limits, and the methodology names 6 of them. They are listed in full in [ai_task_log/actual_development_tasks.md](ai_task_log/actual_development_tasks.md): incorrect logic, missing context, security weaknesses, unverified output, overcomplication, and business misunderstandings. For these reasons, AI output must be reviewed and tested before it is used as part of the project.

## What AI did not do
AI did not replace the developer's responsibility, did not verify the pipeline, and did not supply the DairyChain results in this set. The results come only from the user-supplied README. The methodology also states that its comparisons describe development principles, and they should not be interpreted as a record of specific incidents unless supported by the project's development history.

## Next step / Related files
- [Development workflow](development_workflow.md)
- [How AI was used](how_ai_was_used.md)
- [Prompt engineering](prompt_engineering.md)
- [Code review](code_review.md)
