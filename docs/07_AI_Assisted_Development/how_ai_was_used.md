# How AI Was Used

> Status: PARTIALLY VERIFIED

## Purpose
This file answers where AI helped in DairyChain and where the developer stayed in charge. It is for a reviewer who needs the AI contribution stated plainly, without overstating it. Its source is sections 1, 2, 3 and 11 of the user-supplied AI-Assisted Development Methodology, 2026-11-11.

## In this file
- Purpose of AI use
- Project context and processing flow
- How AI was integrated, by stage
- The 13 uses from the brief
- Key learning
- Status

## Purpose of AI use
DairyChain was developed using a combination of the developer's technical knowledge and AI-assisted development. The objective was not to make AI build the entire project independently. AI was used as a development assistant to improve speed, explore implementation approaches, understand errors, and reduce repetitive work. The developer remained responsible for understanding the business requirements, deciding what the system needed to do, reviewing the suggested logic, running the code, checking the outputs, and determining whether the implementation was correct.

> AI helped accelerate development. Technical decisions, execution, verification, and responsibility remained with me.

## Project context and processing flow
DairyChain is a dairy supply chain analytics project that brings together procurement, milk quality, production, and sales information. The documented processing flow is:

1. Python-based data ingestion.
2. Loading source data into the PostgreSQL Bronze layer.
3. Cleaning and transforming data into the Silver layer using SQL.
4. Preparing analytical tables in the Gold layer.
5. Connecting the Gold layer to Power BI for reporting and analysis.

The project uses Python, SQL, PostgreSQL, and Power BI for different stages of the workflow. AI assistance was used across development activities, but the tools did not replace the need to understand how these components work together.

## How AI was integrated, by stage
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

## The 13 uses from the brief
The Master Project Brief lists 13 uses of AI assistance. They are consistent with the methodology above, and they are the method stated in the brief and the README:
1. Requirement clarification.
2. Breaking work into smaller implementation tasks.
3. Database and schema review.
4. Python code drafting.
5. SQL query construction.
6. Code explanation.
7. Error investigation.
8. Debugging.
9. Code refactoring.
10. Test-case preparation.
11. Security review.
12. Performance improvement.
13. Documentation.

What each use means in practice: clarification and task breakdown turn a business question into a small, testable task. Schema review checks that a draft uses the real tables and columns, not a guessed name. Code drafting and SQL construction save time, but the draft is not trusted until it runs and its output is checked. Explanation, error investigation and debugging help the developer understand a failure, not hide it. Refactoring, test preparation, security review and performance work are checked the same way: run it, measure it, record it.

## Key learning
Working with AI changed how the developer approached development tasks. Instead of treating programming as only writing code, the focus moved to understanding the problem, selecting an appropriate implementation, reviewing the logic, investigating errors, and validating the outcome. Python and SQL remained important because the developer needed to understand what the code was doing. AI helped reduce the time spent exploring solutions and investigating issues, but it could not replace technical understanding or independent verification.

> Using AI effectively is not just about generating code faster. It is about being able to understand, evaluate, debug, test, and take responsibility for the code it helps produce.

## Status
The method above is PARTIALLY VERIFIED as a user-supplied methodology document. No task log was supplied, so no specific AI task in DairyChain can be listed as completed here. See [ai_task_log/actual_development_tasks.md](ai_task_log/actual_development_tasks.md). Status for the task record: PENDING EVIDENCE.

## Next step / Related files
- [Development workflow](development_workflow.md)
- [Prompt engineering](prompt_engineering.md)
- [AI task log](ai_task_log/actual_development_tasks.md)
