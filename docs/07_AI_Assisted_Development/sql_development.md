# SQL Development


## Purpose
This file answers how SQL was used in DairyChain, with the project SQL example from the user-supplied AI-Assisted Development Methodology, 2026-11-11, section 5. It is for a developer who needs the SQL pattern, and needs to know which queries are project examples and which are illustrative only.

## In this file
- What SQL does in DairyChain
- Project example: procurement batch rejection rate
- Step 1: required information, Step 2: SQL operations, Step 3: SQL implementation, Step 4: validation
- The 5 checks
- Recorded result
- Illustrative queries from the brief
- Notes

## What SQL does in DairyChain
SQL is used for data cleaning, transformation and analytical queries in PostgreSQL. The analytical work includes aggregations with GROUP BY, multi-table joins, CTEs, conditional aggregation, date-based analysis, business calculations, and supplier, product, procurement, quality and sales analysis.

## Project example: procurement batch rejection rate
Business question: What percentage of procurement batches were rejected?

The calculation requires:

Rejection Rate = (Rejected Batches / Total Batches) x 100

### Step 1: Identify the required information
Source: the user-supplied "AI Prompts and Code Examples" document, 2026-11-11, section 4. Translating this business requirement into SQL starts with the required information:

- Total number of batches.
- Number of rejected batches.
- Number of accepted batches.
- Rejection percentage.

### Step 2: Identify the required SQL operations
| Requirement | SQL operation |
|---|---|
| Count all batches | COUNT(*) |
| Count rejected batches | Conditional COUNT |
| Count accepted batches | Conditional COUNT |
| Calculate percentage | Arithmetic calculation |
| Avoid division by zero | NULLIF |

### Step 3: SQL implementation
A SQL implementation for the Gold procurement quality table is:

```sql
SELECT
    COUNT(*) AS total_batches,

    COUNT(*) FILTER (
        WHERE quality_status = 'Rejected'
    ) AS rejected_batches,

    COUNT(*) FILTER (
        WHERE quality_status = 'Accepted'
    ) AS accepted_batches,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE quality_status = 'Rejected'
        ) / NULLIF(COUNT(*), 0),
        2
    ) AS rejection_rate_percentage

FROM gold.procurement_quality_summary;
```

Source note: the table name `gold.procurement_quality_summary` and the column name `quality_status` are user-supplied in the methodology document. Do not treat them as schema-shown until the DDL is supplied.

### The 5 checks
The query should not be trusted just because it executes. The methodology says to check:

1. Does the table contain one record per procurement batch?
2. Are the quality-status values correct?
3. Is the query counting batches rather than summing milk quantity?
4. Does the calculation handle a zero denominator?
5. Does the calculated result match the project's recorded procurement figures?

### Recorded result
| Metric | Recorded result |
|---|---:|
| Total procurement batches | 18,000 |
| Accepted batches | 15,689 |
| Rejected batches | 2,311 |
| Batch rejection rate | 12.84% |

The calculation is:

2311 / 18000 x 100 = 12.84%

### Step 4: Validate the result
Source: the prompts document, section 4. The query result should be compared with these recorded figures when executed against the corresponding project database. The project-level procurement figures are the same as in the table above: 18,000 total batches, 15,689 accepted, 2,311 rejected, rejection rate 12.84 percent.

### What was learned
Writing SQL is not only about remembering syntax. It is also about understanding the business requirement and breaking it into smaller operations. AI can suggest the query structure, but the developer needs to understand why each operation is used and whether the result answers the original question.

This example demonstrates an important development principle: AI can help construct a query, but the business definition and result still need to be checked.

## Illustrative queries from the brief
The queries below come from the Master Project Brief. They are illustrative, not project queries. Use actual table and column names after inspecting the schema.

### Illustrative production aggregation
```sql
SELECT
    product_id,
    SUM(produced_quantity) AS total_produced_quantity
FROM production_batches
GROUP BY product_id
ORDER BY total_produced_quantity DESC;
```

What it does: it sums produced quantity by product, so the highest-output products come first. It does not prove efficiency, because it has no input quantity.

### Illustrative FEFO ordering
FEFO means first-expired, first-out. This query selects eligible lots in FEFO order. Selection and ordering alone do not make a complete inventory allocation transaction.

```sql
SELECT
    lot_id,
    product_id,
    available_quantity,
    expiry_date
FROM inventory_lots
WHERE available_quantity > 0
  AND expiry_date >= CURRENT_DATE
ORDER BY expiry_date ASC, lot_id ASC;
```

### Illustrative parameterised query
Use parameterised queries, never string concatenation with untrusted input. Placeholder style depends on the actual driver.

```python
cursor.execute(
    """
    SELECT procurement_id, supplier_id, quantity
    FROM procurement
    WHERE procurement_id = %s
    """,
    (procurement_id,)
)
record = cursor.fetchone()
```

## Notes
The rejection-rate query and its result come from the document, and the numbers were user-supplied. The table and column names match the Gold column list in the data dictionary. The illustrative queries above are brief illustrations only.

## Next step / Related files
- [Python development](python_development.md)
- [SQL injection prevention](../10_Security_and_Reliability/sql_injection_prevention.md)
- [Query references](../13_Project_Evidence/query_references.md)
