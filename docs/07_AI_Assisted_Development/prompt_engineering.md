# Prompt Engineering

> Status: PARTIALLY VERIFIED

## Purpose
This file answers how to instruct AI well in DairyChain, with a weak prompt against a better engineering prompt. It is for a developer who wants useful AI help without handing over judgement. Its sources are the Master Project Brief, section 7 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, and sections 1, 2, 10 and 11 of the user-supplied AI Prompts and Code Examples document, 2026-11-11. All prompts from that document are representative templates, not claimed to be exact historical chat prompts.

## In this file
- Weak prompt
- Better engineering prompt
- Why the better prompt works
- The focused-request principle
- Representative debugging prompt template
- Example A: vague against useful, Python ingestion
- Recommended prompt structure
- AI assistance against developer responsibility
- More examples

## Weak prompt
"Write Python code for procurement."

Why it is weak: it names no schema, no validation rule, no interface and no test. It invites a generic answer that may use the wrong fields.

## Better engineering prompt
"Inspect the existing procurement module and database schema. Identify the required validation rules. Implement validation without changing existing function interfaces. Handle missing required columns, null identifiers, duplicates and invalid quantities. Include meaningful error messages and tests. Explain assumptions and identify any schema mismatch before proposing changes."

Why it is better: it names the module, the schema, the rules, the interface limit, the edge cases, the tests and the need to report assumptions before changing anything.

## Why the better prompt works
A good prompt gives AI the context a developer would need: the existing code, the real fields, the limits, and the way success will be checked. It asks for explanation as well as code, so the developer can review the reasoning, not only the output.

## The focused-request principle
From the methodology, section 4 step 2: instead of asking AI to generate an entire application or pipeline at once, use focused requests related to the task. This made it easier to inspect the proposed logic and identify where a mistake could occur. A focused request names the specific task, the expected behaviour, and the check that will prove the result.

## Representative debugging prompt template
This is a representative prompt template from the methodology, section 7. It is not a claim that these exact words were used in a particular debugging session.

> I am working on the DairyChain project. This code is responsible for [specific task]. I expected [expected behaviour], but I received the following error: [complete error message].
>
> Explain the likely root cause. Identify the exact part of the code that may be responsible. Suggest the smallest appropriate correction and explain how I can test whether the correction works. Do not rewrite unrelated parts of the program.

A useful debugging request contains: the intended behaviour, the relevant code, the complete error message, the command or operation that produced the error, the expected result, and the actual result.

## Example A: vague against useful, Python ingestion
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 2. Both prompts below are representative templates, not claimed to be exact historical chat prompts.

Vague request:

> Write Python code to load CSV files into PostgreSQL.

Why it is vague: it does not explain the folder structure, database configuration, target schema, table naming rules, or validation requirements.

More useful request:

> I am developing the data ingestion stage of DairyChain. The source data is provided in CSV files, and PostgreSQL is used as the database.
>
> Help me design a Python ingestion approach that loads each source file into the Bronze schema.
>
> Before suggesting code, explain the steps involved. Include appropriate checks for file availability, column names, row counts, data types, and database loading errors.
>
> Do not hardcode database passwords. Keep the implementation focused on ingestion and explain how I can verify that the records were loaded correctly.

Why the second request is better: it provides project context, defines the expected result, identifies important validation requirements, and asks for an explanation rather than only code.

## Recommended prompt structure
Source: the prompts document, section 10. Use this structure for future AI-assisted development tasks:

```text
PROJECT CONTEXT:
Explain which part of DairyChain is being developed.

TASK:
Describe the exact technical requirement.

CURRENT IMPLEMENTATION:
Provide the relevant code, SQL, schema, or configuration.

EXPECTED RESULT:
Explain what should happen.

ACTUAL RESULT:
Explain what happened or provide the complete error.

CONSTRAINTS:
Mention existing project structure, tools, and
implementation requirements.

REQUEST:
Ask for an explanation, targeted solution,
possible edge cases, and verification steps.
```

This structure helps make technical discussions more specific and reduces irrelevant or overly broad suggestions.

## AI assistance against developer responsibility
Source: the prompts document, section 11.

| AI can assist with | Developer remains responsible for |
|---|---|
| Suggesting Python code | Understanding and executing the code |
| Suggesting SQL queries | Confirming business logic and query results |
| Explaining database errors | Reproducing and resolving the issue |
| Suggesting test cases | Running tests and recording evidence |
| Reviewing possible security issues | Confirming and implementing appropriate controls |
| Suggesting DAX measures | Checking calculations and filter behaviour |
| Explaining architecture options | Selecting and documenting the actual architecture |

AI assistance does not transfer responsibility for the correctness, security, or reliability of the application.

## More examples
- SQL: "Use the Gold table procurement_quality_summary at batch grain. Write a query that returns rejection rate by supplier, with the count and volume behind each rate. Do not invent a column name. List any column you could not find in the schema."
- Debugging: "Here is the traceback and the failing file and line. The input was X and the expected output was Y. List the likely causes, in order, and the smallest check that would rule each one out."
- Testing: "List test cases for this validation function, including missing values, duplicates, negative quantities and invalid dates. For each case, state the input and the expected error."
- Security: "Review this query for SQL injection risk and for JOIN duplication that would double-count revenue. State the risk, the line, and the fix."

## Next step / Related files
- [How AI was used](how_ai_was_used.md)
- [Code review](code_review.md)
- [Development workflow](development_workflow.md)
- [Debugging with AI](debugging_with_ai.md)
