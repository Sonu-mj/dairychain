# Development Workflow

> Status: PARTIALLY VERIFIED

## Purpose
This file answers how work moved from a business requirement to validated code in DairyChain. It is for a developer who needs the workflow, not a list of tools. Its source is sections 3, 4 and 6 of the user-supplied AI-Assisted Development Methodology, 2026-11-11.

## In this file
- How AI was integrated, by stage
- The 6-step problem-first workflow
- Less-reliable approach against the approach used
- What counts as done

## How AI was integrated, by stage
AI was treated as a technical assistant at different stages of the development lifecycle. The developer stayed responsible at every stage.

| Development stage | How AI was used | My responsibility |
|---|---|---|
| Requirement analysis | Helped break business requirements into technical tasks | Define what the project needed to achieve |
| Solution planning | Explored possible implementation approaches | Select an approach suitable for the project |
| Python development | Assisted with code structure, implementation ideas, and error analysis | Understand, execute, and verify the code |
| SQL development | Assisted with queries, joins, transformations, and analytical logic | Check query logic and validate results |
| PostgreSQL | Helped investigate connection and database-related issues | Configure, execute, and verify database operations |
| Power BI | Assisted with DAX, relationships, and visual configuration | Check measures, filters, and reported values |
| Debugging | Helped interpret errors and suggest possible fixes | Reproduce the problem and test the correction |
| Documentation | Helped organise technical explanations | Ensure documentation accurately represented the implementation |

## The 6-step problem-first workflow
The developer followed a problem-first approach rather than blindly requesting complete code.

### Step 1: Understand the requirement
Before requesting an implementation, identify what the task needed to accomplish. For example, a business requirement such as measuring milk rejection should first be translated into clear analytical requirements: identify the total number of procurement batches, identify the number of rejected batches, calculate the rejection percentage, and confirm which quality-status values represent accepted and rejected batches. This made the implementation problem more specific.

### Step 2: Ask AI for a focused solution
Instead of asking AI to generate an entire application or pipeline at once, use focused requests related to the task. This made it easier to inspect the proposed logic and identify where a mistake could occur.

### Step 3: Review the suggested implementation
Review the output before relying on it. For Python, this meant examining the operations, input files, transformations, data types, and expected output. For SQL, this meant checking the selected columns, joins, filtering conditions, grouping logic, and calculations.

### Step 4: Execute and inspect the result
A code suggestion was not considered correct simply because it looked valid. It needed to be executed in the project environment and its result inspected.

### Step 5: Debug when something failed
When an error occurred, use the error message and relevant code to investigate the issue. Focus on identifying the cause of the failure instead of replacing the entire implementation without understanding the problem.

### Step 6: Validate the output
Check whether the output made sense for the business requirement. This included checking counts, calculated values, data consistency, and whether analytical results could be traced back to the underlying tables.

## Less-reliable approach against the approach used
| Less reliable approach | Approach used in my development methodology |
|---|---|
| Accepting generated code without understanding it | Reviewing the logic before using the code |
| Asking AI to rewrite an entire program for every error | Investigating the failing component and considering a targeted fix |
| Trusting a query because it executes successfully | Checking the query logic and resulting values |
| Assuming a dashboard measure is correct because it displays a number | Checking its calculation, data source, relationships, and filters |
| Treating an AI explanation as proof | Confirming behaviour through execution and inspection |
| Copying an implementation without considering the project structure | Checking whether the proposed implementation fits the existing pipeline |

These comparisons describe the development principles used to guide AI assistance. They should not be interpreted as a record of specific incidents unless supported by the project's development history.

## What counts as done
A task is done when the code runs, the output is checked against a second method, the tests for that task are recorded, and the documentation names the evidence. A task that only has a draft is not done. The developer owns every step. AI can draft, explain and suggest, but the developer decides whether the draft solves the requirement, uses the right fields, and is safe to run.

## Next step / Related files
- [How AI was used](how_ai_was_used.md)
- [Code review](code_review.md)
- [Debugging with AI](debugging_with_ai.md)
