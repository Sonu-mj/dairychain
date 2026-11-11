# Actual Development Tasks


## Purpose
This file answers which AI-assisted development tasks actually happened in DairyChain, and how each AI suggestion was decided. It is for a reviewer who needs a task record and a decision record, not a general statement that AI was used. Its sources are the Master Project Brief, sections 10 and 12 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, and the user-supplied "AI-Assisted Development Decision Log" document, 2026-11-11, used as Source 7.

## In this file
- What was supplied
- Decision principles
- Decision categories
- Decision register format
- Decision record template
- The register holds no entries.
- Limitations of AI-assisted development
- Evidence to maintain
- AI decision log
- Template for each task

## What the sources hold
The methodology document describes the method and principles, and it names one project SQL example, the rejection-rate query in [../sql_development.md](../sql_development.md). The decision log document supplies the decision structure and one illustrative technical example.

## Decision principles
Source: Decision Log, section 1. Use these principles when evaluating AI-generated suggestions:

- Understand the proposed solution before accepting it.
- Check whether it addresses the actual requirement.
- Consider its impact on the existing implementation.
- Evaluate potential logical errors and security risks.
- Prefer simpler solutions when they meet the same requirement.
- Check accepted changes through execution and testing.

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

**Check:**

[Describe the test performed and the actual result.]

**Source:**

[Add the relevant source file, query output, screenshot, test record, or conversation reference.]

---

## The register
Source: Decision Log, section 10. This file provides the decision-record structure and one illustrative technical example, in [../../12_Engineering_Decisions/architecture_decisions.md](../../12_Engineering_Decisions/architecture_decisions.md). Historical AI decisions should be added from the actual DairyChain development conversations and implementation evidence. Update the entry when an investigating decision is resolved, and record the actual date and implementation reference where available.

## Limitations of AI-assisted development
1. **Incorrect logic:** AI may provide code that runs but calculates the wrong result.
2. **Missing context:** AI may not know the complete database schema or project implementation.
3. **Security weaknesses:** Generated code may contain unsafe practices.
5. **Overcomplication:** A suggested solution may be more complex than the requirement.
6. **Business misunderstandings:** AI may misunderstand a metric or business rule unless the requirement is clearly explained.

AI output must be reviewed and tested before it is used as part of the project.

## Evidence to maintain
Collect these from the actual project before making more detailed claims:

- Examples of AI-assisted Python implementation.
- Examples of AI-assisted SQL development.
- Original errors and the corresponding shown corrections.
- Relevant PostgreSQL query outputs.
- Data quality and reconciliation results.
- Power BI DAX measures and relationship screenshots.
- Test cases with actual execution results.
- Decisions where an AI suggestion was modified or rejected.

These records should be linked to the relevant implementation files and reports wherever possible.

## AI decision log
Source: the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 10. Capture suggestions that were accepted, modified, or rejected in the decision register. The debugging journal should capture the technical issue and its resolution. The Decision Log document, Source 7, is the structure for that log: see the decision register format and template above. Do not back-fill this section with invented decisions.

## Template for each task
- Date:
- Task:
- Requirement in one sentence:
- Prompt used:
- AI suggestion:
- Developer change after review:
- Test or check:

Do not back-fill this file with invented tasks. Add a task only when its prompt, draft and test can be shown.

## Next step / Related files
- [AI task log README](README.md)
- [How AI was used](../how_ai_was_used.md)
- [Architecture decisions](../../12_Engineering_Decisions/architecture_decisions.md)
- [check file](../../../VERIFICATION_AND_MISSING_INFO.md)
