# Python Development


## Purpose
This file answers how Python was used in DairyChain, with the illustrative validation example from the brief. It is for a developer who needs the Python patterns, and needs to know which example is illustrative and which is project code. The methodology content below is from the user-supplied AI-Assisted Development Methodology, 2026-11-11. The ingestion validation example below is from the user-supplied AI Prompts and Code Examples document, 2026-11-11, section 3, and is representative, not project code. The code review examples below are from the user-supplied "Code Review and Security Practices" document, 2026-11-11, section 3 (Source 5), and are representative, not project code. The Python implementation is in Google Colab notebooks (.ipynb), not separate local scripts. One notebook, `dairychain.ipynb`, has now been received and inspected (Source 15, 2026-11-11). Its actual code is described in "Actual notebook implementation - Source 15" below. The examples in this file stay labelled representative, not project code.

## In this file
- What Python does in DairyChain
- What AI helped with in Python
- How Python work was reviewed
- Illustrative validation example
- Representative ingestion validation example
- Code review: input and file validation
- Code review: data types and missing values
- Code review: error handling
- Patterns to follow
- Notebook inspection checklist - Source 14
- Notes

## What Python does in DairyChain
Python is used for data ingestion and processing, with Pandas for manipulation and transformation. The documented intent is that it reads CSV files, checks them, loads them into PostgreSQL, and supports the cleaning and transformation steps that build Silver and Gold. What the notebook actually does is narrower: it reads the CSV files, profiles them and validates them in Pandas, and never connects to PostgreSQL or writes a Bronze table. See "Actual notebook implementation - Source 15" below. Do not describe the Bronze load as implemented in Python until a load is shown in code or in a run log.

## What AI helped with in Python
From the methodology, AI assisted with code structure, implementation ideas, and error analysis in Python development. The developer's responsibility was to understand, execute, and check the code.

## How Python work was reviewed
Before relying on a Python suggestion, the developer reviewed the operations, input files, transformations, data types, and expected output. A suggestion was not considered correct simply because it looked valid. It needed to be executed in the project environment and its result inspected, then validated against the business requirement by checking counts, calculated values, data consistency, and whether results could be traced back to the underlying tables.

## Illustrative validation example
This example comes from the Master Project Brief. It is illustrative, not project code. Check the actual schema and module names before presenting it as project implementation.

```python
import pandas as pd

def validate_procurement(df: pd.DataFrame) -> list[str]:
    required = ["procurement_id", "supplier_id", "quantity"]
    errors = []
    missing = [column for column in required if column not in df.columns]
    if missing:
        return [f"Missing columns: {missing}"]
    if df["procurement_id"].isna().any():
        errors.append("Procurement IDs cannot be null.")
    if df["procurement_id"].duplicated().any():
        errors.append("Duplicate procurement IDs found.")
    if df["supplier_id"].isna().any():
        errors.append("Supplier IDs cannot be null.")
    quantity = pd.to_numeric(df["quantity"], errors="coerce")
    if quantity.isna().any():
        errors.append("Quantity contains missing or non-numeric values.")
    elif (quantity <= 0).any():
        errors.append("Quantity must be greater than zero.")
    return errors
```

What it does: it checks for missing columns, null ids, duplicate ids, null supplier ids, and quantity values that are missing, non-numeric or not greater than zero. It returns a list of error messages, so the caller can decide what to do next.

## Representative ingestion validation example
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 3. This is a representative validation example, not the exact ingestion script.

### Problem
When loading source data, a successful execution message alone does not prove that the expected records were loaded. The input file and the resulting DataFrame should be inspected.

### Representative Python code
```python
import pandas as pd
from pathlib import Path

# Specify the source file
file_path = Path("data/raw/procurement.csv")

# Check whether the file exists
if not file_path.exists():
    raise FileNotFoundError(
        f"Source file not found: {file_path}"
    )

# Read the CSV file
df = pd.read_csv(file_path)

# Inspect the data
print("Rows and columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Inspect data types
print("\nData types:")
print(df.dtypes)
```

### What AI assistance can contribute
AI can help explain the validation operations, suggest additional checks, and identify potential issues in the ingestion logic.

### What to check
1. Is the correct source file being read?
2. Does the DataFrame contain the expected number of rows and columns?
3. Are the column names correct?
4. Are missing values expected or unexpected?
5. Are duplicate records possible?
6. Are the data types suitable for the next pipeline stage?

**Important:** This is a representative validation example. It should not be described as the exact ingestion script unless it matches the code actually used in DairyChain.

## Code review: input and file validation
Source: "Code Review and Security Practices", section 3.1. Representative example, not project code.

**Potential problem:** Assuming that an input file always exists and has the expected structure. A safer approach is to check the file before processing it.

```python
from pathlib import Path
import pandas as pd

file_path = Path("data/raw/procurement.csv")

if not file_path.exists():
    raise FileNotFoundError(
        f"Required input file is missing: {file_path}"
    )

df = pd.read_csv(file_path)

if df.empty:
    raise ValueError("The input file contains no records.")

required_columns = {
    "procurement_id",
    "quantity_litres",
    "quality_status"
}

missing_columns = required_columns - set(df.columns)

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )
```

**What this protects against:**

- Missing input files.
- Empty datasets.
- Unexpected source schemas.
- Processing files that do not meet basic requirements.

The column names in this example are illustrative and should be adjusted to the actual source file.

## Code review: data types and missing values
Source: "Code Review and Security Practices", section 3.2. Representative example, not project code.

The data type of a column affects calculations and transformations. For example:

- Procurement quantities should be numeric.
- Dates should be interpreted as dates or timestamps.
- Identifier columns should be handled consistently.
- Missing values should be examined before calculations.

Representative validation:

```python
# Check the current column types
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Check duplicate records
print("Duplicate rows:", df.duplicated().sum())

# Inspect numeric values
print(df["quantity_litres"].describe())
```

These checks help identify problems before data is inserted into the database.

**Important:** Missing values and duplicates are not always errors. Their meaning depends on the business rules and the source data.

## Code review: error handling
Source: "Code Review and Security Practices", section 3.3. Representative example, not project code.

A risky implementation may catch every exception and continue without reporting the actual failure. For example:

```python
try:
    process_data()
except Exception:
    pass
```

This hides errors and can make an unsuccessful operation appear successful.

A better approach is to preserve useful error information and stop when an operation cannot safely continue.

```python
try:
    process_data()

except FileNotFoundError:
    raise

except Exception as error:
    print(f"Data processing failed: {error}")
    raise
```

For production use, structured logging should generally replace simple print statements, and error messages should avoid exposing sensitive information.

## Patterns to follow
- Inspect data before transforming it.
- Handle missing values by a stated rule.
- Identify duplicates by key, not by eye.
- Validate numeric types with coercion, and report the rows that fail.
- Handle dates in Asia/Kolkata, and keep the unit with every quantity.
- Log errors, and do not silently drop rows.

## Actual notebook implementation - Source 15
Notebook `dairychain.ipynb`, user-supplied 2026-11-11, inspected from the file itself (1.4 MB, 148 code cells, 0 markdown cells, 157 stored outputs: 54 execute_result, 51 stream, 48 display_data, 4 error). All `execution_count` values are None.

### Imports
Only five imports appear in the whole notebook: `pandas as pd`, `os`, `zipfile`, `from google.colab import files`, `matplotlib.pyplot as plt` (cells 0-2, 4, 64, 138-140). No database library is imported: no `psycopg`, no `sqlalchemy`, no `create_engine`, no `to_sql`. No credentials appear in the notebook: no password, secret or token string was found.

### Ingestion
Cells 4 and 6 upload `DairyChain_dataset_full.zip` and unzip it to `/content/dairychain`. Cell 11 lists the four raw folders. Cells 13-78 read 10 CSV files with `pd.read_csv` from `/content/dairychain/DairyChain_dataset/data/raw`: `master/suppliers.csv`, `master/collection_centres.csv`, `master/products.csv`, `procurement/milk_procurement.csv`, `procurement/quality_tests.csv`, `production/production_batches.csv`, `production/production_inputs.csv`, `production/production_outputs.csv`, `sales/sales_orders.csv`, `sales/sales_order_lines.csv`. Row counts from stored outputs: 200, 18,000, 18,000, 20, 12, 4,000, 8,000, 9,352, 14,000, 28,000, total 99,584, matching the README total. Full column lists are in [data_dictionary.md](../02_System_Architecture/data_dictionary.md) under "Source CSV files - Source 15".

### Transformations
- Timestamp cleaning: cells 30-32 find one non-ISO timestamp, PRC-000500 `10/11/2025 19:19`, and parse it with `pd.to_datetime(format='mixed', dayfirst=True, errors='coerce')` to 2025-11-10 19:19:00.
- Cost: cell 36 `calculated_cost = quantity_litres * purchase_rate_per_litre`, cell 37 `cost_difference = total_purchase_cost - calculated_cost`, cells 39-40 `cost_status` valid (17,999) or COST_MISMATCH (1, PRC-001000, difference 6,657.17).
- Rejection rules: cell 61 defines SNF below 8.2, fat below 3.2, acidity above 0.17, temperature above 8.5C, and checks each rule for inconsistent records: 0 for all four.
- Status flags: cell 82 flags missing temperature (1 record) and missing rejection reason (15,689 accepted rows, expected), and cell 82 also flags delivery dates (607 cancelled orders with no delivery date).
- Summaries: supplier summaries by rejection rate (cells 101-105, highest SUP-0087 at 26.05 percent), centre summaries and dominant rejection reason per centre (cells 124-130, CC-018 Low SNF 66.59 percent), a CC-018 deep dive (cells 131-137), production input/output checks split by unit (cells 87-96), sales fulfilment at line level and order level (cells 84-86).
- Charts: 8 matplotlib figures (cells 138-145): CC-018 supplier reasons, centre rejection rate, centre reason heatmap, monthly rejection trend, rejected milk by reason, production frequency by product, batches by shift, revenue by product. Chart values are images, not text, so no chart value is quoted here.
- Cell 141 also produces a pandas DeprecationWarning about `DataFrameGroupBy.apply` on grouping columns. It is a warning, not an error, and the chart still renders.

### What the notebook holds
The notebook uses pandas, os, zipfile, google.colab, and matplotlib only. The only PostgreSQL mention is cell 146, a PowerShell `psql.exe` command pasted as a Python cell, which produced a SyntaxError (BUG-004). The notebook prints no package versions; the only version hint is a Python 3.13 path in a traceback. Do not invent a pandas or Python version and do not create an assumed requirements.txt.

## Notebook inspection checklist - Source 14, answered by Source 15
Code cells: 148, all code. Imports: pandas, os, zipfile, google.colab.files, matplotlib.pyplot. PostgreSQL connection: none in code. Ingestion operations: zip upload, unzip, 10 CSV reads, profiling. Transformations: listed above. Execution outputs: 157 stored outputs, including 4 errors (BUG-001 to BUG-004 in [troubleshooting_log.md](../08_Debugging_and_Troubleshooting/troubleshooting_log.md)). Dependencies: identify the actual packages used and their versions from the notebooks where verifiable only. Only the package names above are verifiable; no version is. Do not invent package versions and do not create an assumed requirements.txt. Do not mark Python implementation as missing simply because there is no scripts/ folder.

## Notes
. One Colab notebook has been received and inspected, so the Python reading, profiling, validation and summary code above is, and its stored outputs are. The examples earlier in this file stay and representative examples only, not project code. The PostgreSQL load, Silver and Gold steps are still : no database code exists in the notebook.

## Next step / Related files
- [SQL development](sql_development.md)
- [Data ingestion](../03_Data_Engineering/data_ingestion.md)
- [Code review](code_review.md)
- [Security review](../10_Security_and_Reliability/security_review.md)
