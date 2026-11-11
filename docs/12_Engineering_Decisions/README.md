# Engineering Decisions - Overview

> Status: PARTIALLY VERIFIED

## Purpose
This file is the index for the engineering decisions folder. It is for a reader who needs to know why DairyChain was built this way, what was chosen, and what was rejected, with a reason for each choice.

## In this file
- The decisions
- How to read them
- What is not a decision

## The decisions
- [python_and_sql_decisions.md](python_and_sql_decisions.md) - why Python does processing and SQL does relational analysis.
- [database_decisions.md](database_decisions.md) - why PostgreSQL was chosen for structured business data.
- [architecture_decisions.md](architecture_decisions.md) - why the Bronze, Silver and Gold layers were chosen, plus the technical decision example on keeping production units separate.
- [rejected_approaches.md](rejected_approaches.md) - what was considered and rejected, and why.

## AI decision log
The AI decision log is in [../07_AI_Assisted_Development/ai_task_log/actual_development_tasks.md](../07_AI_Assisted_Development/ai_task_log/actual_development_tasks.md). It records each significant AI suggestion as Accepted, Modified, Rejected, or Investigating, with the reason, implementation, verification, and evidence. No historical AI decisions were supplied, so the register is empty by design. The units-separate example in [architecture_decisions.md](architecture_decisions.md) is a technical design example, not an AI decision.

## How to read them
Each decision names the choice, the reason, the alternative, and the evidence that would prove the choice was right. A decision without a reason is a preference, not an engineering decision.

## What is not a decision
A tool named in the README is not automatically a decision that was tested. It is a choice that is documented here, with its reason, and marked PENDING EVIDENCE where its test was not supplied.

## Next step / Related files
- [Python and SQL decisions](python_and_sql_decisions.md)
- [Database decisions](database_decisions.md)
- [Architecture decisions](architecture_decisions.md)
- [AI decision log](../07_AI_Assisted_Development/ai_task_log/actual_development_tasks.md)
