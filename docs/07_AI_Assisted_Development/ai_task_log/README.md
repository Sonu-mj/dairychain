# AI Task Log - Overview

> Status: PENDING EVIDENCE

## Purpose
This file answers what the AI task log is for and how to add a task to it, and how to record what happened to each AI suggestion. It is for a developer who needs a record of what AI helped with, task by task, instead of a general claim. Its sources are the Master Project Brief, sections 10 and 12 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, and the user-supplied "AI-Assisted Development Decision Log" document, 2026-11-11, used as Source 7.

## In this file
- What the log is
- What each entry must contain
- Decision evaluation framework
- Recording modified suggestions
- Recording rejected suggestions
- Limitations of AI-assisted development
- Evidence to maintain
- Where the entries live

## What the log is
The AI task log is a dated record of AI-assisted tasks in DairyChain. Each entry names the task, the prompt, the draft, the review, the fix and the result. It is the evidence that AI was used as an assistant, with the developer in charge. The decision log in [actual_development_tasks.md](actual_development_tasks.md) is the companion record: it records the decision on each significant suggestion as Accepted, Modified, Rejected, or Investigating.

## What each entry must contain
- Date and task name.
- The business requirement in one sentence.
- The prompt used, or a short summary of it.
- What AI suggested.
- What the developer changed after review.
- The test or check that proves the result.
- The status: done, in progress, or rejected.

## Decision evaluation framework
Source: Decision Log, section 3. Before accepting an AI-generated implementation, consider these questions.

### Technical correctness
- Does the suggested implementation solve the stated problem?
- Is the code syntactically and logically correct?
- Does it use the correct columns, tables, and data types?

### Business correctness
- Does the calculation match the business definition?
- Does it measure the intended quantity?
- Are the assumptions reasonable?

### Compatibility
- Does the suggestion fit the existing DairyChain architecture?
- Does it work with the existing Python and PostgreSQL implementation?
- Will it create problems in downstream transformations or Power BI?

### Security
- Does it expose credentials?
- Does it introduce SQL injection risks?
- Does it require permissions that are unnecessary?

### Maintainability
- Is the implementation understandable?
- Does it add unnecessary complexity?
- Can another developer maintain it?

### Verification
- Has the suggested implementation been executed?
- Has its output been inspected?
- Is there independent evidence that it works?

## Recording modified suggestions
Source: Decision Log, section 6. Sometimes AI provides a useful solution but the implementation needs to be adjusted. For example, a suggested SQL query may calculate a percentage correctly but use the wrong measurement for the business question. In that situation, record:

1. What AI proposed.
2. What was unsuitable about the original suggestion.
3. What was changed.
4. Why the revised implementation was more appropriate.
5. How the final result was validated.

The purpose is to show the developer's contribution rather than merely recording that AI generated code. No modified-suggestion case was supplied yet, so none is recorded here.

## Recording rejected suggestions
Source: Decision Log, section 7. Rejecting an AI suggestion can also be an important engineering decision. Examples of reasons to reject a suggestion include:

- It does not match the actual database schema.
- It introduces unnecessary complexity.
- It produces incorrect business calculations.
- It creates a security weakness.
- It uses an incompatible measurement unit.
- It changes unrelated parts of working code.
- It cannot be verified with the available evidence.

A rejection should include a clear technical explanation, not simply state that the suggestion did not work. No rejected-suggestion case was supplied yet, so none is recorded here.

## Limitations of AI-assisted development
AI assistance has limitations that need to be recognised. The methodology lists 6:

1. **Incorrect logic:** AI may provide code that runs but calculates the wrong result.
2. **Missing context:** AI may not know the complete database schema or project implementation.
3. **Security weaknesses:** Generated code may contain unsafe practices.
4. **Unverified output:** An explanation or code suggestion does not prove successful execution.
5. **Overcomplication:** A suggested solution may be more complex than the requirement.
6. **Business misunderstandings:** AI may misunderstand a metric or business rule unless the requirement is clearly explained.

For these reasons, AI output must be reviewed and tested before it is used as part of the project.

## Evidence to maintain
The following evidence should be collected from the actual project before making more detailed claims:

- Examples of AI-assisted Python implementation.
- Examples of AI-assisted SQL development.
- Original errors and the corresponding verified corrections.
- Relevant PostgreSQL query outputs.
- Data quality and reconciliation results.
- Power BI DAX measures and relationship screenshots.
- Test cases with actual execution results.
- Decisions where an AI suggestion was modified or rejected.

These records should be linked to the relevant implementation files and reports wherever possible. None of these items was supplied with the methodology document, so all of them remain PENDING EVIDENCE.

## Where the entries live
Entries live in [actual_development_tasks.md](actual_development_tasks.md). No entries were supplied with the README or with the methodology document, and no historical AI decisions were supplied with the decision log document, so that file states what is missing and what to add first. Evidence and traceability: where possible, connect each decision record to Colab notebook (.ipynb) files, SQL scripts, PostgreSQL query outputs, DAX measures, Power BI screenshots, test results, relevant AI conversations, and Git commit references, once available. Do not include confidential conversation content, credentials, database passwords, or access tokens.

## Next step / Related files
- [Actual development tasks](actual_development_tasks.md)
- [How AI was used](../how_ai_was_used.md)
- [Development workflow](../development_workflow.md)
