# Raw data

This folder holds the 10 source CSV files the project was built from, 99,584 records in total:

- suppliers.csv (200 rows)
- collection_centres.csv (20 rows)
- products.csv (12 rows)
- milk_procurement.csv (18,000 rows)
- quality_tests.csv (18,000 rows)
- production_batches.csv (4,000 rows)
- production_inputs.csv (9,352 rows)
- production_outputs.csv (8,000 rows)
- sales_orders.csv (14,000 rows)
- sales_order_lines.csv (28,000 rows)

The CSV files are not in this repo yet. They were read in Google Colab from `DairyChain_dataset_full.zip`. Add the zip or the 10 CSV files here to reproduce the pipeline. Row counts and column names are recorded in `docs/02_System_Architecture/data_dictionary.md` and verified against the live PostgreSQL database in `docs/13_Project_Evidence/`.
