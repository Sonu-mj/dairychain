# Debugging Methodology

> Status: PARTIALLY VERIFIED

## Purpose
This file answers how to debug DairyChain in a fixed order, so a fix is proven and not guessed. It is for a developer who needs to find a cause, fix it once, and keep the fix from breaking something else. Its source is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, sections 1, 2 and 3, in full.

## In this file
- The method
- The 9-step approach
- How debugging was approached with AI
- The 8-step structured workflow
- Isolation
- Regression
- Recording
- Status

## The method
Debugging is an important part of software and data engineering. Code may contain syntax errors, incorrect logic, configuration problems, database issues, or unexpected data conditions. During DairyChain development, AI assistance was useful for investigating technical problems and exploring possible corrections. However, an AI-generated correction should not automatically be considered a successful fix.

The purpose of the method is a disciplined debugging and testing approach:

1. Understand the expected behaviour.
2. Reproduce the problem.
3. Collect the relevant error and code.
4. Investigate the root cause.
5. Evaluate possible solutions.
6. Apply a targeted correction.
7. Execute the affected component again.
8. Validate the output.
9. Record the result and supporting evidence.

Core principle:

> A fix is successful only when the original problem is resolved and the expected behaviour is verified.

## How debugging was approached with AI
AI was treated as a debugging assistant rather than asked to replace the entire implementation. The important distinction was between asking for a quick replacement and asking for an explanation of the actual failure.

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

## The 8-step structured workflow

### Step 1: Understand the expected behaviour
Before investigating an error, establish what the code is supposed to do. For example, for a data-ingestion operation:

- Read the correct source file.
- Identify the expected columns.
- Load the records into the intended Bronze table.
- Preserve the required data.
- Report failures rather than silently ignoring them.

Without a clear expected result, it is difficult to decide whether a correction is actually appropriate.

### Step 2: Reproduce the error
Run the affected operation again and identify:

- The command or operation being executed.
- The file or function involved.
- The complete error message.
- The line where execution failed, if available.
- Whether the problem happens consistently or intermittently.

Reproducing the problem helps distinguish the original failure from a new issue.

### Step 3: Collect relevant evidence
Before asking AI for assistance, collect the information needed to understand the issue.

| Information | Why it matters |
|---|---|
| Relevant code | Identifies the operation being performed |
| Complete error message | Helps locate the failure |
| Expected behaviour | Defines what the implementation should achieve |
| Actual behaviour | Shows what happened |
| Input data or schema | Helps identify data and compatibility issues |
| Environment details | Helps identify dependency and configuration problems |

Sensitive values, passwords, and access tokens must be removed before sharing logs or configuration with an AI tool.

### Step 4: Investigate the root cause
An error message identifies a failure, but the underlying cause may be elsewhere. For example, a database insertion error may be caused by:

- A column-name mismatch.
- An incompatible data type.
- A missing required value.
- An incorrect table name.
- A database connection problem.
- A constraint violation.

The correction should address the actual cause, not merely suppress the error message.

### Step 5: Evaluate the AI suggestion
Before applying the proposed correction, ask:

1. Does the explanation match the actual error?
2. Does the suggested change fit the existing implementation?
3. Does it affect any other pipeline stage?
4. Could it introduce a data-quality or security problem?
5. Is there a way to test it independently?

A suggested solution that cannot be explained should not be accepted blindly.

### Step 6: Apply a targeted correction
Change only the relevant component when possible. This makes it easier to understand what changed and whether the correction resolved the issue.

### Step 7: Test again
Execute the affected operation after the correction. Check both the original problem and the expected output. An error disappearing does not necessarily mean the implementation is now correct.

### Step 8: Record the outcome
Record the problem, likely root cause, correction, test performed, and final status. Do not mark a problem as resolved until there is evidence that the corrected implementation works.

## Isolation
Isolate the failing component before changing anything else. A change to two parts at once hides which change fixed the fault, and hides which change broke the next test.

## Regression
After a fix, run the tests that passed before the fix. A fix that breaks a passing test is not a fix. It is a new fault.

## Recording
Record the root cause and the resolution in [troubleshooting_log.md](troubleshooting_log.md). A fix that is not recorded will be fixed again, badly, the next time it appears.

## Status
The method above is user-supplied, 2026-11-11, and is PARTIALLY VERIFIED as method. No debugging journal was supplied, so no DairyChain error can be listed here as a real debugging example. See [errors_and_fixes.md](errors_and_fixes.md).

## Next step / Related files
- [Errors and fixes](errors_and_fixes.md)
- [Troubleshooting log](troubleshooting_log.md)
- [Debugging with AI](../07_AI_Assisted_Development/debugging_with_ai.md)
