# Transaction and Data Integrity


## Purpose
This file answers how DairyChain protects data when a write fails part-way through, and why transactions matter for stock and for Gold builds. It is for a developer who needs atomic updates, not half-finished ones. Its source for the SQL logic review below is section 5 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5).

## In this file
- Transactions
- Atomic stock updates
- Integrity checks
- SQL logic review: aggregation level
- SQL logic review: joins before aggregation
- SQL logic review: NULL handling
- SQL logic review: date filters
- SQL logic review: measurement units
- Notes

## Transactions
A transaction groups several writes so they succeed together or fail together. A Gold build, a stock update or a multi-table load that fails half-way must roll back, not leave half the data changed.

## Atomic stock updates
Inventory allocation, when it exists, must update stock and record the allocation in the same transaction. A stock change without its record, or a record without its stock change, leaves the reconciliation broken. The reconciliation rule is: Opening stock plus Signed movement ledger equals Current stock.

## Integrity checks
- Primary keys and foreign keys must be enforced, not only documented. In this database they are not enforced: Source 20 shown that no primary key, foreign key, unique, or check constraint exists on any table in bronze, silver, or gold (`pg_constraint` returned 0 rows). This is a recorded gap, not a design choice. Indexes are also absent: Source 21 shown that no index exists on any table in bronze, silver, or gold (`pg_index` returned 0 rows). See [data_validation.md](../03_Data_Engineering/data_validation.md).
- A Gold build must be re-runnable, and a failed build must not leave a half-built Gold table in place.
- Counts at Bronze, Silver and Gold must be checked after every run.

## SQL logic review: aggregation level
Source: "Code Review and Security Practices", section 5.1. A SQL query can be syntactically correct and still return incorrect business results.

Consider two different business questions:

**Question A:** What percentage of procurement batches were rejected?

Rejected Batches / Total Batches x 100

**Question B:** What percentage of procured milk volume was rejected?

Rejected Milk Volume / Total Milk Volume x 100

Both are valid metrics, but they measure different things.

For DairyChain, the recorded results are:

| Metric | Result |
|---|---:|
| Total procurement batches | 18,000 |
| Rejected batches | 2,311 |
| Batch rejection rate | 12.84% |
| Total milk volume | 8,758,507.64 L |
| Rejected milk volume | 1,117,247.35 L |
| Milk volume rejection rate | 12.76% |

Using the wrong numerator or denominator would produce a misleading business conclusion.

## SQL logic review: joins before aggregation
Source: "Code Review and Security Practices", section 5.2. Joining tables with multiple matching records can multiply rows. For example, if one supplier has multiple procurement records and multiple related records in another table, joining at the wrong level can inflate a SUM.

Before accepting a query, check:

1. What is the primary or unique key of each table?
2. What is the expected relationship between the tables?
3. Is the join one-to-one, one-to-many, or many-to-many?
4. Does the number of rows change unexpectedly after the join?
5. Does the aggregation still represent the intended business metric?

A useful diagnostic is to compare the row count before and after a join.

## SQL logic review: NULL handling
Source: "Code Review and Security Practices", section 5.3. NULL values can change how aggregate functions behave. For example:

```sql
SELECT
    AVG(fat_percentage)
FROM gold.procurement_quality_summary;
```

`AVG` ignores NULL values. The result is therefore the average of available values, not necessarily the average across all procurement batches.

When reviewing a query, ask:

- Are NULL values expected?
- Should missing values be excluded?
- Should they be represented separately?
- Could excluding them bias the result?
- Is the denominator appropriate?

## SQL logic review: date filters
Source: "Code Review and Security Practices", section 5.4. Date filtering must match the intended reporting period. For a timestamp column, this pattern can unintentionally exclude records later in the final day:

```sql
WHERE procurement_timestamp
BETWEEN '2026-01-01' AND '2026-01-31'
```

A safer half-open interval for a timestamp is:

```sql
WHERE procurement_timestamp >= '2026-01-01'
  AND procurement_timestamp <  '2026-02-01'
```

The dates above are illustrative. Actual reporting dates should be determined by the business question and the dataset.

## SQL logic review: measurement units
Source: "Code Review and Security Practices", section 5.5. DairyChain contains production outputs measured in different units. For example:

- Finished product output can be measured in litres.
- Finished product output can also be measured in kilograms.

These quantities must not be summed into one meaningful total without a valid conversion rule. Any calculation combining measurement units should be reviewed carefully.

## Notes
A constraint list output WAS supplied by Source 20: a `pg_constraint` query over bronze, silver, and gold returned 0 rows, so no primary key, foreign key, unique, or check constraint exists on any table.

## Next step / Related files
- [Security review](security_review.md)
- [Data validation](../03_Data_Engineering/data_validation.md)
- [Pipeline execution](../03_Data_Engineering/pipeline_execution.md)
- [KPI definitions](../04_Business_Analytics/kpi_definitions.md)
