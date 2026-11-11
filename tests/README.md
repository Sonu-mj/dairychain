# Tests

No formal test suite exists yet. Nothing here is marked passed.

What exists so far, as evidence rather than tests:

- Validation checks inside `scripts/dairychain.ipynb` (duplicates, missing values, cost mismatches, rejection-rule consistency), recorded in `docs/09_Testing_and_Validation/`.
- Live database checks recorded in `docs/13_Project_Evidence/`: table inventory, column dump, Gold row counts, zero constraints, zero indexes.
- Four real bugs found and fixed while building the notebook, logged as BUG-001 to BUG-004 in `docs/08_Debugging_and_Troubleshooting/`.

Add test files here when they exist, with their run output. Do not mark any test passed without execution evidence.
