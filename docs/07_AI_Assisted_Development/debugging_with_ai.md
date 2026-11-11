# Debugging with AI

> Status: PARTIALLY VERIFIED

## Purpose
This file answers how debugging worked in DairyChain, step by step, and what a debugging record must contain. It is for a developer who needs to fix an error once and prove the fix. Its sources are the Master Project Brief debugging workflow and section 7 of the user-supplied AI-Assisted Development Methodology, 2026-11-11, in full.

## In this file
- How debugging was approached
- Approach to debugging with AI
- Evaluating an AI suggestion
- What a useful debugging request contains
- Representative debugging prompt template
- Representative prompt: investigating a SQL error
- Representative prompt: debugging Python code
- Why targeted debugging matters
- The 12-step debugging workflow
- What to record
- Status

## How debugging was approached
Debugging was an important part of AI-assisted development. The approach was to provide enough technical context for the issue to be investigated. When an error occurred, the developer used the error message and relevant code to investigate the issue, and focused on identifying the cause of the failure instead of replacing the entire implementation without understanding the problem.

## Approach to debugging with AI
Source: the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, section 2. AI was treated as a debugging assistant rather than asked to replace the entire implementation. The important distinction was between asking for a quick replacement and asking for an explanation of the actual failure.

Less effective approach:

> My code is not working. Give me correct code.

This gives AI very little information. It may generate a completely different implementation without identifying the original problem.

More useful approach:

> I am working on the data ingestion stage of DairyChain.
>
> The intended operation is to load the source data into the PostgreSQL Bronze schema.
>
> Here is the relevant Python code:
>
> [Insert code]
>
> Here is the complete error message:
>
> [Insert error]
>
> Explain the likely root cause. Identify the exact statement causing the issue. Suggest a minimal correction and explain how I can verify that the correction works.
>
> Do not rewrite unrelated parts of the existing implementation.

This provides context and encourages a focused investigation.

## Evaluating an AI suggestion
Source: the same methodology document, section 3 step 5. Before applying a proposed correction, ask:

1. Does the explanation match the actual error?
2. Does the suggested change fit the existing implementation?
3. Does it affect any other pipeline stage?
4. Could it introduce a data-quality or security problem?
5. Is there a way to test it independently?

A suggested solution that cannot be explained should not be accepted blindly.

## What a useful debugging request contains
- The intended behaviour.
- The relevant code.
- The complete error message.
- The command or operation that produced the error.
- The expected result.
- The actual result.

## Representative debugging prompt template
This is a representative prompt template, not a claim that these exact words were used in a particular debugging session.

> I am working on the DairyChain project. This code is responsible for [specific task]. I expected [expected behaviour], but I received the following error: [complete error message].
>
> Explain the likely root cause. Identify the exact part of the code that may be responsible. Suggest the smallest appropriate correction and explain how I can test whether the correction works. Do not rewrite unrelated parts of the program.

## Why targeted debugging matters
Replacing an entire program can introduce new problems and make it harder to understand the original issue. A targeted debugging approach helps preserve working code, isolate the problem, and make the correction easier to verify.

## Representative prompt: investigating a SQL error
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 5. This is a representative prompt template, not a claim that these exact words were used in a particular debugging session.

> I am working with PostgreSQL in the DairyChain project.
>
> Here is my SQL query:
>
> [Insert the complete SQL query]
>
> This is the error:
>
> [Insert the complete error message]
>
> Explain what the error means in simple technical terms.
>
> Identify the likely cause and the specific part of the query responsible. Suggest the smallest appropriate correction.
>
> Explain how I can verify that the corrected query produces the intended result. Do not rewrite unrelated parts of the query.

Why this approach is useful: it gives AI the information needed to investigate a specific issue instead of asking it to generate a completely different query. It also encourages understanding the cause of the error rather than simply copying a replacement query.

## Representative prompt: debugging Python code
Source: the prompts document, section 7. This is a representative prompt template, not a claim that these exact words were used in a particular debugging session.

> I am working on the Python data processing stage of DairyChain.
>
> The intended operation is:
>
> [Describe the intended operation]
>
> Here is the relevant code:
>
> [Insert the relevant code]
>
> Here is the complete error:
>
> [Insert the error]
>
> Help me identify the root cause.
>
> First explain why the error may be occurring. Then suggest a targeted correction and explain how to test it. Do not change the overall project structure unless necessary.

### What should happen after receiving a suggested fix?
- Understand the proposed correction.
- Apply it to the relevant code.
- Execute the affected operation again.
- Check whether the original error is resolved.
- Check whether the output is still correct.
- Check whether the correction introduced a new issue.

A message saying that the correction should work is not evidence that it has passed testing.

## The 12-step debugging workflow
1. Observe the error.
2. Capture the traceback or database message.
3. Identify the failing file and line.
4. Check inputs and data types.
5. Reproduce the issue.
6. Isolate the failing component.
7. Use AI to investigate possible causes.
8. Evaluate the suggested fix.
9. Apply the smallest appropriate change.
10. Re-run the failing scenario.
11. Run regression tests.
12. Record the root cause and resolution.

## What to record
For each error, record: the error message, the file and line, the input that caused it, the cause found, the fix applied, the test that proves the fix, and the date. A fix without a test is a guess that happened to work once.

## Status
No debugging journal was supplied, so no DairyChain error can be listed here as a real debugging example. The brief reported an earlier PostgreSQL authentication error during database creation. Status: RESOLVED by Source 17, which verifies a successful connection. Do not invent other errors. See [../08_Debugging_and_Troubleshooting/errors_and_fixes.md](../08_Debugging_and_Troubleshooting/errors_and_fixes.md).

## Next step / Related files
- [Code review](code_review.md)
- [Debugging methodology](../08_Debugging_and_Troubleshooting/debugging_methodology.md)
- [Testing with AI](testing_with_ai.md)
- [Prompt engineering](prompt_engineering.md)
