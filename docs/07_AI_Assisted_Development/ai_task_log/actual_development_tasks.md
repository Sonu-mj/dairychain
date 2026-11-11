# Actual Development Tasks

> Status: PENDING EVIDENCE

## Purpose
This file answers which AI-assisted development tasks actually happened in DairyChain, and how each AI suggestion was decided. It is for a reviewer who needs a task record and a decision record, not a general statement that AI was used. Its sources are the Master Project Brief, sections 10 and 12 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, and the user-supplied "AI-Assisted Development Decision Log" document, 2026-11-11, used as Source 7.

## In this file
- What was supplied
- Decision principles
- Decision categories
- Decision register format
- Decision record template
- Current status: register empty by design
- Limitations of AI-assisted development
- Evidence to maintain
- Evidence to add from the prompts document
- AI decision log
- What to add first
- Template for each task

## What was supplied
No AI task log was supplied. No task name, prompt, draft, review note, test result, original error, or verified correction was supplied for DairyChain. The methodology document describes the method and principles, and it names one project SQL example, the rejection-rate query in [../sql_development.md](../sql_development.md), but it does not list dated tasks. The decision log document supplies the decision structure and one illustrative technical example, not historical decisions. Status: PENDING EVIDENCE.

## Decision principles
Source: Decision Log, section 1. Use these principles when evaluating AI-generated suggestions:

- Understand the proposed solution before accepting it.
- Check whether it addresses the actual requirement.
- Consider its impact on the existing implementation.
- Evaluate potential logical errors and security risks.
- Prefer simpler solutions when they meet the same requirement.
- Verify accepted changes through execution and testing.

The purpose of the log is to make AI-assisted development transparent and demonstrate developer judgement. AI can offer multiple solutions. Good engineering requires knowing which solution to use, which to modify, and which to reject.

## Decision categories
Source: Decision Log, section 2. Every important AI suggestion should be recorded under one of four categories.

| Decision | Meaning |
|---|---|
| Accepted | The suggestion was suitable and was accepted after review |
| Modified | The suggestion was useful but needed changes |
| Rejected | The suggestion was unsuitable or incorrect |
| Investigating | More information or testing is needed before making a decision |

A suggestion should not be marked as accepted merely because AI provided a convincing explanation. Do not mark any suggestion accepted, modified, rejected, or tested in this file until its evidence is supplied.

## Decision register format
Source: Decision Log, section 4. Every significant AI-assisted decision should be recorded using this format.

| Field | Description |
|---|---|
| Decision ID | Unique identifier, such as AI-001 |
| Date | Date the suggestion was evaluated |
| Component | Python, SQL, PostgreSQL, Power BI, or architecture |
| Problem | The technical or business problem |
| AI suggestion | What AI proposed |
| Developer decision | Accepted, modified, rejected, or investigating |
| Reason | Technical reasoning behind the decision |
| Implementation | What was actually changed |
| Verification | How the implementation was checked |
| Evidence | Link to code, output, screenshot, or relevant conversation |

## Decision record template
Source: Decision Log, section 4. Copy this template for every new entry.

#### AI-XXX - [Short decision title]

**Date:** [YYYY-MM-DD]

**Component:** [Python / SQL / PostgreSQL / Power BI / Architecture]

**Problem or requirement:**

[Explain what needed to be solved.]

**AI suggestion:**

[Describe the suggested approach. Include the actual prompt or relevant response where available.]

**My decision:**

[Accepted / Modified / Rejected / Investigating]

**Reason for the decision:**

[Explain why the suggestion was suitable, needed modification, or was rejected.]

**Implementation:**

[Describe what was actually implemented. Include the relevant file, SQL query, Python function, or DAX measure.]

**Verification:**

[Describe the test performed and the actual result.]

**Evidence:**

[Add the relevant source file, query output, screenshot, test record, or conversation reference.]

---

## Current status: register empty by design
Source: Decision Log, section 10. This file provides the decision-record structure and one illustrative technical example, in [../../12_Engineering_Decisions/architecture_decisions.md](../../12_Engineering_Decisions/architecture_decisions.md). Historical AI decisions should be added from the actual DairyChain development conversations and implementation evidence. No historical entries were supplied, so the register is empty. No unverified AI acceptance, modification, rejection, or testing event is presented here as a historical fact. Update the status when an investigating decision is resolved, and record the actual date and implementation reference where available.

## Limitations of AI-assisted development
1. **Incorrect logic:** AI may provide code that runs but calculates the wrong result.
2. **Missing context:** AI may not know the complete database schema or project implementation.
3. **Security weaknesses:** Generated code may contain unsafe practices.
4. **Unverified output:** An explanation or code suggestion does not prove successful execution.
5. **Overcomplication:** A suggested solution may be more complex than the requirement.
6. **Business misunderstandings:** AI may misunderstand a metric or business rule unless the requirement is clearly explained.

AI output must be reviewed and tested before it is used as part of the project.

## Evidence to maintain
Collect these from the actual project before making more detailed claims:

- Examples of AI-assisted Python implementation.
- Examples of AI-assisted SQL development.
- Original errors and the corresponding verified corrections.
- Relevant PostgreSQL query outputs.
- Data quality and reconciliation results.
- Power BI DAX measures and relationship screenshots.
- Test cases with actual execution results.
- Decisions where an AI suggestion was modified or rejected.

These records should be linked to the relevant implementation files and reports wherever possible. None of them was supplied yet.

## Evidence to add from the prompts document
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 12. To make that document an accurate record of DairyChain development, add the following evidence where available. None of these was supplied yet, so all five items remain PENDING EVIDENCE:

1. A genuine Python prompt and the corresponding implementation.
2. A genuine SQL prompt and the query that was reviewed.
3. An actual debugging conversation showing an error and its verified correction.
4. A Power BI or DAX example from the implemented dashboard.
5. An example where an AI suggestion was modified or rejected, with the technical reason.

Do not publish private credentials, access tokens, database passwords, or other secrets in prompts or code examples.

## AI decision log
Source: the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 10. Use `AI_DECISION_LOG.md` to capture suggestions that were accepted, modified, or rejected. The debugging journal should capture the technical issue and its resolution. The Decision Log document, Source 7, is now the structure for that log: see the decision register format and template above. No AI decision log entries were supplied yet, so no suggestion is recorded here as accepted, modified, or rejected. Do not back-fill this section with invented decisions.

## What to add first
When the log is built, add these tasks first, in this order:
1. Requirement clarification for procurement, quality, production and sales.
2. Schema review for Bronze, Silver and Gold.
3. Python ingestion drafting and review.
4. SQL transformation drafting and review for the 6 Gold tables.
5. Power BI DAX measure drafting and review.
6. Debugging entries, with the error, the cause and the fix.
7. Test-case preparation, with the executed output.
8. Documentation drafting and review.

## Template for each task
- Date:
- Task:
- Requirement in one sentence:
- Prompt used:
- AI suggestion:
- Developer change after review:
- Test or check:
- Status:

Do not back-fill this file with invented tasks. Add a task only when its prompt, draft and test can be shown.

## Next step / Related files
- [AI task log README](README.md)
- [How AI was used](../how_ai_was_used.md)
- [Architecture decisions](../../12_Engineering_Decisions/architecture_decisions.md)
- [Verification file](../../../VERIFICATION_AND_MISSING_INFO.md)
