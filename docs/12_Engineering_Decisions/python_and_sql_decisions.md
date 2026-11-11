# Python and SQL Decisions


## Purpose
This file answers why Python and SQL split the work in DairyChain the way they do. It is for a developer who needs to know which tool to use for a new task.

## In this file
- The split
- Why Python for processing
- Why SQL for analysis
- When to use each

## The split
Python does ingestion, cleaning and transformation. SQL does relational analysis, aggregation and Gold building. Power BI does presentation. Each tool does the job it is best at, and no tool is asked to do the job of another.

## Why Python for processing
Python, with Pandas, is suited to reading CSV files, checking types and values, handling missing data, and transforming records before they reach the database. It is flexible for file-level work, and its errors can be logged per file and per row.

## Why SQL for analysis
SQL is suited to joins, aggregations, CTEs and date-based analysis on structured data in PostgreSQL. A question that needs a sum by supplier, centre, product or day is a SQL question, and its result can be checked by counting rows at the right grain.

## When to use each
- Use Python to move, check and clean data.
- Use SQL to aggregate, join and summarise data.
- Use Power BI and DAX to present a Gold result, not to rebuild it from raw data.
- Do not re-implement a SQL aggregation in Python for a report, and do not re-implement a Python cleaning step in SQL for a file load.

## Next step / Related files
- Database decisions](database_decisions.md)
- Architecture decisions](architecture_decisions.md)
- Analytics methodology](../04_Business_Analytics/analytics_methodology.md)
