# SQL

This folder will hold the SQL that builds the six Gold tables and their dependencies:

- procurement_quality_summary (18,000 rows)
- collection_centre_performance (20 rows)
- supplier_performance (200 rows)
- production_performance (4,000 rows)
- sales_product_performance (12 rows)
- sales_daily_summary (364 rows)

The Gold SQL has not been supplied yet. It is the biggest open gap in this project. The table structures and row counts are verified against the live PostgreSQL database (see `docs/13_Project_Evidence/`), but the transformation logic that produced Silver and Gold inside PostgreSQL has not been located or verified, so no SQL has been written here. Do not add guessed SQL. Add only the SQL that was actually run.
