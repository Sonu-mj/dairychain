# Data Cleaning

> Status: PENDING EVIDENCE

## Purpose
This file answers what cleaning means in DairyChain and what must be documented for every cleaning decision. It is for a reader who needs to know whether a Gold number was changed by cleaning or by the business itself.

## In this file
- Cleaning steps
- Silver cleaning - potential activities to verify
- Rules that must be written down
- What was not supplied

## Cleaning steps
- Standardise types, dates and units.
- Handle missing values by a stated rule, not by silent deletion.
- Remove or flag duplicate records, and record how many were removed.
- Flag invalid or unexpected values for review, rather than changing them without a record.

## Silver cleaning - potential activities to verify
Source data is not always ready for analysis. It may contain: missing values, inconsistent data types, duplicate records, inconsistent date formats, incorrect or invalid values, inconsistent identifiers, and records requiring business-rule validation. The Silver layer provides a dedicated stage for preparing data before analytical aggregation.

The exact cleaning rules should be taken from the actual SQL scripts. The following are potential activities to verify, not a claim that all were implemented:

| Transformation | Objective |
|---|---|
| Data-type conversion | Use appropriate database data types |
| Missing-value handling | Apply defined rules to incomplete records |
| Duplicate handling | Identify and address duplicate records |
| Date standardisation | Make date fields consistent |
| Identifier checks | Maintain entity consistency |
| Business-rule validation | Identify invalid business values |
| Column organisation | Prepare structured tables for downstream processing |

## Rules that must be written down
For each rule, write: the field, the problem found, the rule applied, how many rows it affected, and why that rule is the right one for the business. A cleaning step without a count cannot be checked.

## What was not supplied
No cleaning script, rule list or before-and-after counts were supplied. The Silver layer is described in the README as 10 cleaned tables, but the cleaning rules are stated there as documented separately. Until that document arrives, this file is method only. Status: PENDING EVIDENCE.

## Next step / Related files
- [Transformation logic](transformation_logic.md)
- [Data validation](data_validation.md)
- [Bronze Silver Gold](bronze_silver_gold_layers.md)
