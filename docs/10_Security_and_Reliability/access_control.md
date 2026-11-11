# Access Control

> Status: PENDING EVIDENCE

## Purpose
This file answers who can read and change DairyChain data, as far as the supplied sources say. It is for a reader who needs to know whether access was actually controlled or only assumed. Its source is section 4.3 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5). The permissions model below is a recommendation to follow, not a claim that it is implemented.

## In this file
- What was supplied
- What access control should cover
- Database permissions: least privilege
- Status

## What was supplied
No access control record, user list, role list or privilege list was supplied. Status: PENDING EVIDENCE.

## What access control should cover
- Who can read Bronze, Silver and Gold, and who can write to each layer.
- Who can run the pipeline, and who can change the SQL that builds Gold.
- Who can view the Power BI report, and who can change its measures.
- Which database privileges each user holds, and why each privilege is needed.

## Database permissions: least privilege
Applications should not automatically receive unnecessary database privileges. A suitable permissions model should consider:

- Whether an application only needs to read data.
- Whether a process needs to insert records into Bronze.
- Whether a transformation needs to modify Silver or Gold.
- Whether administrative operations should be restricted.

The principle of least privilege means granting only the permissions necessary for the task. For example, a dashboard connection that only reads Gold tables should not need permission to alter database schemas or delete source records.

The actual role configuration must be inspected before claiming that permissions are separated in DairyChain.

## Status
Do not claim any access control as implemented. Add the user and privilege list here only when it can be shown from the database or the repository.

## Next step / Related files
- [Security review](security_review.md)
- [Credential management](credential_management.md)
- [Transaction and data integrity](transaction_and_data_integrity.md)
