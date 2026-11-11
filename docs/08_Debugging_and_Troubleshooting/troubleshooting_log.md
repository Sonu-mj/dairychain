# Troubleshooting Log


## Purpose
This file answers what troubleshooting happened in DairyChain, in dated order. It is for a developer who needs to see what was tried, what worked, and what is still open. Its source for the log format and evidence list is the user-supplied "Debugging and Testing Methodology" document, 2026-11-11, sections 10 and 11.

## In this file
- What was supplied
- Debugging log format
- Evidence required
- Template for each entry
- Open items

## What was supplied
The notebook `dairychain.ipynb` (Source 15, 2026-11-11) holds 4 stored error outputs with their corrections in later cells. Those 4 are real errors from the project work, recorded below as BUG-001 to BUG-004. No error is invented here. Dates are not in the notebook, so no date is claimed for any entry. No AI conversation is claimed for any fix.

| Issue ID | Notebook cell | Error | Correction | Outcome |
|---|---|---|---|---|
| BUG-001 | Cell 34 | KeyError: 'quantity_liters' | Cell 36 uses the correct column name `quantity_litres`. Later cells 38 and 40 run and show 1 cost mismatch and 17,999 valid records. | Fixed |
| BUG-002 | Cell 63 | FileNotFoundError: no such file `/content/dairychain/DairyChain_dataset/data/raw/master/collection_centers.csv` | Cell 65 uses the correct file name `collection_centres.csv`. Its output shows shape (20, 9) and the centre columns. | Fixed |
| BUG-003 | Cell 87 | KeyError: 'By-product/residual' | Cells 88-89 use the correct pivot column name `By-product / residual`. Cell 89 runs and shows the production check for 4,000 batches. | Fixed. Note: the check itself then shows 999 mismatches, which cells 93-96 explain as a litre-versus-kilogram unit comparison, not a remaining code error. |
| BUG-004 | Cell 146 | SyntaxError: invalid syntax, from the line `& "C:\Program Files\PostgreSQL\18\bin\psql.exe" -U postgres -d dairychain` | None in the notebook. A PowerShell command was pasted into a Python cell. No corrected cell follows it. | Fixed. Source: [postgresql-connection-and-schemas.png](../13_Project_Evidence/postgresql-connection-and-schemas.png). |

## Debugging log format

| Field | What to record |
|---|---|
| Issue ID | Unique reference such as BUG-001 |
| Date | Date the problem was identified |
| Component | Python, SQL, PostgreSQL, Power BI, or configuration |
| Problem | Clear description of the observed failure |
| Expected behaviour | What should have happened |
| Actual behaviour | What happened |
| Error message | Exact error, where available |
| Root cause | Confirmed cause or current hypothesis |
| AI assistance | Explanation or suggestion provided by AI |
| Correction | Change made to address the issue |
| Check | Test run after the correction |
| Outcome | Fixed |

Use `AI_DECISION_LOG.md` to capture suggestions that were accepted, modified, or rejected. The debugging journal should capture the technical issue and its resolution.

## Template for each entry
- Date:
- Symptom:
- Error message:
- File and line:
- Input that caused it:
- Cause found:
- Fix applied:
- Test that proves the fix:

## Open items
1. Source 17: a current connection test now exists and succeeds (localhost, port 5432, user postgres, database dairychain, server PostgreSQL 18.6). The earlier authentication error is no longer the current state.
2. BUG-004 above: RESOLVED by Source 17. The psql command line in cell 146 was run in PowerShell as intended, with its output captured in the screenshots.
3. Any other error found during ingestion, cleaning, Gold building or Power BI refresh. Needs the error message and the fix, as above.

Do not close an item without its test output.

## Next step / Related files
- [Errors and fixes](errors_and_fixes.md)
- [Debugging methodology](debugging_methodology.md)
- [Testing strategy](../09_Testing_and_Validation/testing_strategy.md)
