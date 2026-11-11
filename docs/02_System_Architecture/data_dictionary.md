# Data Dictionary


## Purpose
This file answers which tables are named in the supplied sources, what each Gold table contains column by column, and which column details are still unknown. It is for a reader who needs to write or check a query without guessing a column name.

## In this file
- Important note on this dictionary
- Medallion layers at a glance
- Tables named in the sources
- Shown column types (Source 18)
- Gold Table 1 - Procurement Quality Summary
- Gold Table 2 - Collection Centre Performance
- Gold Table 3 - Supplier Performance
- Gold Table 4 - Production Performance
- Gold Table 5 - Sales Product Performance
- Gold Table 6 - Sales Daily Summary
- Dimension tables (Source 11)
- Source CSV files - Source 15
- Known mismatch: dim_date mapping columns - explained as derived date fields
- Power BI model - from Source 23 (pbixray): DAX, relationships, dims, model data
- How to use this file

## Important note on this dictionary
The column lists below are documented columns with business meanings, supplied by the user in the "DairyChain - Database Architecture" document (Source 10, 2026-11-11, sections 5-10). They replace the earlier business-level field descriptions from Source 8. The column names and business meanings are copied exactly from Source 10.

Data types and nullability are now from Source 18 (pasted `information_schema.columns` output, 238 rows, user-supplied 2026-11-11): see "shown column types - Source 18" below and the Type column in each Gold table. Primary keys, foreign keys, unique constraints, and check constraints are now absent in Source 20 (a `pg_constraint` query over bronze, silver, and gold returned 0 rows, user-supplied screenshot 2026-11-11). Indexes are absent in Source 21 (a `pg_index` query over bronze, silver, and gold returned 0 rows, user-supplied screenshot 2026-11-11). Do not assume a key or a constraint from the column name alone. Do not use a column in a join until its key is checked in the database definition from the actual database definition.

Bronze and Silver table names are from Source 17 (psql table inventory, 26 rows total, user-supplied screenshots 2026-11-11). Bronze, Silver, and Gold columns, with types, are now from Source 18 and listed in full below.

## Medallion layers at a glance
DairyChain uses the Medallion Architecture: Bronze, then Silver, then Gold. Every table in this dictionary belongs to one of the three layers, and its layer is labelled in the section or table where it appears.

| Layer | Schema | Tables | Columns | Rows | What the layer holds |
|---|---|---:|---:|---:|---|
| Bronze | `bronze` | 10 | 82 | 99,584 | Raw ingestion as-is: source CSV data loaded into PostgreSQL without cleaning, every column `text` |
| Silver | `silver` | 10 | 83 | 99,584 | Cleaned and typed: the same records with proper data types and cleaning applied |
| Gold | `gold` | 6 | 73 | 22,596 | Business-ready aggregates: analytical tables for reporting in Power BI |

Bronze and Silver hold the same 10 table names: `collection_centres`, `milk_procurement`, `production_batches`, `production_inputs`, `production_outputs`, `products`, `quality_tests`, `sales_order_lines`, `sales_orders`, `suppliers`. Gold holds 6 tables: `procurement_quality_summary` (18,000), `collection_centre_performance` (20), `supplier_performance` (200), `production_performance` (4,000), `sales_product_performance` (12), `sales_daily_summary` (364). Source: table names from Source 17, column names and types from Source 18, Gold row counts from Source 19, Bronze and Silver row totals from Source 25 (99,584 each). Silver kept all 99,584 rows, so cleaning dropped 0 rows at the Bronze-to-Silver step.

The Colab notebook (Source 15) shows pandas validation and transformation logic, but it has no SQL and no Bronze load, so it must not be read as the database transformation.

## Source CSV files - Source 28

The 10 source CSV files are now supplied as files, not only described in the notebook. Source 28 is the user-supplied `DairyChain_dataset_full.zip` (2026-11-11), copied to `data/raw/` flat (10 files) and kept as evidence at [DairyChain_dataset_full.zip](../13_Project_Evidence/DairyChain_dataset_full.zip). Each CSV was SHA256-checked against the supplied `SHA256SUMS.txt` (all 10 OK) and recounted with `wc -l`: suppliers 200, collection_centres 20, products 12, milk_procurement 18,000, quality_tests 18,000, production_batches 4,000, production_inputs 9,352, production_outputs 8,000, sales_orders 14,000, sales_order_lines 28,000. Total 99,584 rows, matching the README exactly.

Comparison against the documented Bronze columns: the CSV headers were compared against the Bronze column lists in this file, table by table, in order. All 10 tables agree exactly, 82 columns in total, 0 differences. The zip's own `DATA_DICTIONARY.md` (copied to [dataset_DATA_DICTIONARY.md](../13_Project_Evidence/dataset_DATA_DICTIONARY.md)) also agrees with the documented columns and row counts. The manifest (`data/manifests/manifest.json`, generated 2026-11-09T09:24:37Z) is in the repo under `data/`.

The dataset is synthetic, not real operational dairy data. The modelling assumptions are in the zip README and in `docs/00_Project_Overview/project_summary.md`. One consequence for this dictionary: the manifest states primary keys and foreign keys for the CSV files (for example `supplier_id` on suppliers, `supplier_id` and `collection_centre_id` on milk_procurement), but those keys exist only in the generated files. In PostgreSQL they are absent (Source 20, 0 constraints on any table). Do not read the manifest's keys as database keys.

## Tables named in the sources

### Table inventory - Source 17
Source: two user-supplied psql screenshots, 2026-11-11 (connection and schema query, then table inventory query). The inventory query was `SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog') AND table_type = 'BASE TABLE' ORDER BY table_schema, table_name;` and returned 26 rows: bronze 10, gold 6, silver 10. The bronze and silver lists are identical. Files: [postgresql-connection-and-schemas.png](../13_Project_Evidence/postgresql-connection-and-schemas.png) and [postgresql-table-inventory.png](../13_Project_Evidence/postgresql-table-inventory.png).

| Schema | Table |
|---|---|
| bronze | collection_centres |
| bronze | milk_procurement |
| bronze | production_batches |
| bronze | production_inputs |
| bronze | production_outputs |
| bronze | products |
| bronze | quality_tests |
| bronze | sales_order_lines |
| bronze | sales_orders |
| bronze | suppliers |
| gold | collection_centre_performance |
| gold | procurement_quality_summary |
| gold | production_performance |
| gold | sales_daily_summary |
| gold | sales_product_performance |
| gold | supplier_performance |
| silver | collection_centres |
| silver | milk_procurement |
| silver | production_batches |
| silver | production_inputs |
| silver | production_outputs |
| silver | products |
| silver | quality_tests |
| silver | sales_order_lines |
| silver | sales_orders |
| silver | suppliers |

### Gold tables - rows and grain (Source 10 lists, row counts from Source 19)
| Table | Layer | Records | Grain |
|---|---:|---:|---|
| procurement_quality_summary | Gold | 18,000 | One row per procurement batch |
| collection_centre_performance | Gold | 20 | One row per collection centre |
| supplier_performance | Gold | 200 | One row per supplier |
| production_performance | Gold | 4,000 | One row per production batch |
| sales_product_performance | Gold | 12 | One row per product |
| sales_daily_summary | Gold | 364 | One row per date |

Row counts above are from Source 19: a UNION ALL COUNT(*) query over the 6 Gold tables, supplied as a user-supplied screenshot 2026-11-11, returned 18,000, 20, 200, 4,000, 12, and 364, total 22,596, matching the documented values exactly. The Source 17 inventory proves the tables exist.

## Column types - Source 18

Source: pasted `information_schema.columns` output, user-supplied 2026-11-11 (Source 18), saved verbatim as [information_schema_columns_238_rows.txt](../13_Project_Evidence/information_schema_columns_238_rows.txt). The query returned 238 rows: Bronze 82, Gold 73, Silver 83. Counts were recomputed from the pasted output and match the (238 rows) footer. No run date was in the pasted output, so no run date is claimed. This output does NOT show primary keys, foreign keys, unique constraints, or indexes, so none of those are claimed from it.

Key findings:
- Bronze: every one of the 82 columns is data_type `text`, is_nullable YES, and no column_default is shown for any row.
- Silver: typed. See the conversions in the tables below, for example `operating_capacity_litres` integer and opening/closing time as time without time zone in `collection_centres`, `quantity_litres` numeric(12,2) in `milk_procurement`, and `registration_date` date in `suppliers`.
- Silver `milk_procurement` has 13 columns, three more than Bronze `milk_procurement` (10): `calculated_purchase_cost`, `cost_difference`, and `cost_status` are added in Silver. Those three columns also appear in Gold `procurement_quality_summary`.
- Silver `suppliers` has only 7 columns, against 9 in Bronze `suppliers`: `status` and `contact_reference` are NOT in `silver.suppliers` in this output. This is a shown difference, not an assumption: the 238-row total confirms the count, and the ordinals run 1 to 7 with no gap.
- Gold: all 6 tables, 73 columns. Every Gold column name matches the documented list from Source 10 exactly, in the same order, with zero mismatches (checked column by column). Types are now shown, including `procurement_timestamp` timestamp with time zone, `quantity_litres` numeric(12,2), `purchase_rate_per_litre` numeric(10,2), `total_purchase_cost` numeric(12,2), and fat, SNF, temperature, and acidity numeric(6,3) in `procurement_quality_summary`.
- All 238 rows show is_nullable YES and no column_default. No column in any layer is marked NOT NULL and no default is defined, according to this output.
- Precision and scale are shown only where the output gives them. `numeric` without a precision in the output means no precision was recorded for that column, not that the column has no scale. `bigint` rows show precision 64 and scale 0 in the output; that is the 64-bit width, not a declared precision, so it is shown as plain `bigint` in the Gold tables and as precision 64 in the Bronze and Silver tables below.

### Bronze columns - Source 18

**bronze.collection_centres** - 9 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `collection_centre_id` | text | - | - | YES |
| 2 | `centre_name` | text | - | - | YES |
| 3 | `village` | text | - | - | YES |
| 4 | `district` | text | - | - | YES |
| 5 | `state` | text | - | - | YES |
| 6 | `operating_capacity_litres` | text | - | - | YES |
| 7 | `opening_time` | text | - | - | YES |
| 8 | `closing_time` | text | - | - | YES |
| 9 | `status` | text | - | - | YES |

**bronze.milk_procurement** - 10 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `procurement_id` | text | - | - | YES |
| 2 | `batch_id` | text | - | - | YES |
| 3 | `supplier_id` | text | - | - | YES |
| 4 | `collection_centre_id` | text | - | - | YES |
| 5 | `procurement_timestamp` | text | - | - | YES |
| 6 | `shift` | text | - | - | YES |
| 7 | `quantity_litres` | text | - | - | YES |
| 8 | `purchase_rate_per_litre` | text | - | - | YES |
| 9 | `total_purchase_cost` | text | - | - | YES |
| 10 | `acceptance_status` | text | - | - | YES |

**bronze.production_batches** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `production_id` | text | - | - | YES |
| 2 | `product_id` | text | - | - | YES |
| 3 | `production_start` | text | - | - | YES |
| 4 | `production_end` | text | - | - | YES |
| 5 | `shift` | text | - | - | YES |
| 6 | `production_status` | text | - | - | YES |
| 7 | `supervisor_id` | text | - | - | YES |

**bronze.production_inputs** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `production_input_id` | text | - | - | YES |
| 2 | `production_id` | text | - | - | YES |
| 3 | `source_batch_id` | text | - | - | YES |
| 4 | `input_material_type` | text | - | - | YES |
| 5 | `input_quantity` | text | - | - | YES |
| 6 | `unit_of_measure` | text | - | - | YES |
| 7 | `input_timestamp` | text | - | - | YES |

**bronze.production_outputs** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `output_id` | text | - | - | YES |
| 2 | `production_id` | text | - | - | YES |
| 3 | `product_id` | text | - | - | YES |
| 4 | `output_type` | text | - | - | YES |
| 5 | `output_quantity` | text | - | - | YES |
| 6 | `unit_of_measure` | text | - | - | YES |
| 7 | `output_classification` | text | - | - | YES |

**bronze.products** - 8 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `product_id` | text | - | - | YES |
| 2 | `product_name` | text | - | - | YES |
| 3 | `category` | text | - | - | YES |
| 4 | `unit_of_measure` | text | - | - | YES |
| 5 | `standard_pack_size` | text | - | - | YES |
| 6 | `shelf_life_days` | text | - | - | YES |
| 7 | `selling_price` | text | - | - | YES |
| 8 | `active_status` | text | - | - | YES |

**bronze.quality_tests** - 10 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `test_id` | text | - | - | YES |
| 2 | `batch_id` | text | - | - | YES |
| 3 | `test_timestamp` | text | - | - | YES |
| 4 | `fat_percentage` | text | - | - | YES |
| 5 | `snf_percentage` | text | - | - | YES |
| 6 | `temperature_c` | text | - | - | YES |
| 7 | `acidity` | text | - | - | YES |
| 8 | `quality_status` | text | - | - | YES |
| 9 | `rejection_reason` | text | - | - | YES |
| 10 | `laboratory_id` | text | - | - | YES |

**bronze.sales_order_lines** - 8 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `order_line_id` | text | - | - | YES |
| 2 | `order_id` | text | - | - | YES |
| 3 | `product_id` | text | - | - | YES |
| 4 | `quantity_ordered` | text | - | - | YES |
| 5 | `quantity_fulfilled` | text | - | - | YES |
| 6 | `unit_selling_price` | text | - | - | YES |
| 7 | `discount_amount` | text | - | - | YES |
| 8 | `line_total` | text | - | - | YES |

**bronze.sales_orders** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `order_id` | text | - | - | YES |
| 2 | `customer_code` | text | - | - | YES |
| 3 | `order_timestamp` | text | - | - | YES |
| 4 | `order_status` | text | - | - | YES |
| 5 | `expected_delivery_date` | text | - | - | YES |
| 6 | `actual_delivery_date` | text | - | - | YES |
| 7 | `payment_status` | text | - | - | YES |

**bronze.suppliers** - 9 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `supplier_id` | text | - | - | YES |
| 2 | `supplier_name` | text | - | - | YES |
| 3 | `village` | text | - | - | YES |
| 4 | `district` | text | - | - | YES |
| 5 | `state` | text | - | - | YES |
| 6 | `supplier_type` | text | - | - | YES |
| 7 | `registration_date` | text | - | - | YES |
| 8 | `status` | text | - | - | YES |
| 9 | `contact_reference` | text | - | - | YES |


### Silver columns - Source 18

**silver.collection_centres** - 9 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `collection_centre_id` | text | - | - | YES |
| 2 | `centre_name` | text | - | - | YES |
| 3 | `village` | text | - | - | YES |
| 4 | `district` | text | - | - | YES |
| 5 | `state` | text | - | - | YES |
| 6 | `operating_capacity_litres` | integer | 32 | 0 | YES |
| 7 | `opening_time` | time without time zone | - | - | YES |
| 8 | `closing_time` | time without time zone | - | - | YES |
| 9 | `status` | text | - | - | YES |

**silver.milk_procurement** - 13 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `procurement_id` | text | - | - | YES |
| 2 | `batch_id` | text | - | - | YES |
| 3 | `supplier_id` | text | - | - | YES |
| 4 | `collection_centre_id` | text | - | - | YES |
| 5 | `procurement_timestamp` | timestamp with time zone | - | - | YES |
| 6 | `shift` | text | - | - | YES |
| 7 | `quantity_litres` | numeric | 12 | 2 | YES |
| 8 | `purchase_rate_per_litre` | numeric | 10 | 2 | YES |
| 9 | `total_purchase_cost` | numeric | 12 | 2 | YES |
| 10 | `calculated_purchase_cost` | numeric | - | - | YES |
| 11 | `cost_difference` | numeric | - | - | YES |
| 12 | `cost_status` | text | - | - | YES |
| 13 | `acceptance_status` | text | - | - | YES |

**silver.production_batches** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `production_id` | text | - | - | YES |
| 2 | `product_id` | text | - | - | YES |
| 3 | `production_start` | timestamp without time zone | - | - | YES |
| 4 | `production_end` | timestamp without time zone | - | - | YES |
| 5 | `shift` | text | - | - | YES |
| 6 | `production_status` | text | - | - | YES |
| 7 | `supervisor_id` | text | - | - | YES |

**silver.production_inputs** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `production_input_id` | text | - | - | YES |
| 2 | `production_id` | text | - | - | YES |
| 3 | `source_batch_id` | text | - | - | YES |
| 4 | `input_material_type` | text | - | - | YES |
| 5 | `input_quantity` | numeric | 12 | 2 | YES |
| 6 | `unit_of_measure` | text | - | - | YES |
| 7 | `input_timestamp` | timestamp without time zone | - | - | YES |

**silver.production_outputs** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `output_id` | text | - | - | YES |
| 2 | `production_id` | text | - | - | YES |
| 3 | `product_id` | text | - | - | YES |
| 4 | `output_type` | text | - | - | YES |
| 5 | `output_quantity` | numeric | 12 | 2 | YES |
| 6 | `unit_of_measure` | text | - | - | YES |
| 7 | `output_classification` | text | - | - | YES |

**silver.products** - 8 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `product_id` | text | - | - | YES |
| 2 | `product_name` | text | - | - | YES |
| 3 | `category` | text | - | - | YES |
| 4 | `unit_of_measure` | text | - | - | YES |
| 5 | `standard_pack_size` | text | - | - | YES |
| 6 | `shelf_life_days` | integer | 32 | 0 | YES |
| 7 | `selling_price` | numeric | 10 | 2 | YES |
| 8 | `active_status` | text | - | - | YES |

**silver.quality_tests** - 10 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `test_id` | text | - | - | YES |
| 2 | `batch_id` | text | - | - | YES |
| 3 | `test_timestamp` | timestamp without time zone | - | - | YES |
| 4 | `fat_percentage` | numeric | 6 | 3 | YES |
| 5 | `snf_percentage` | numeric | 6 | 3 | YES |
| 6 | `temperature_c` | numeric | 6 | 3 | YES |
| 7 | `acidity` | numeric | 6 | 3 | YES |
| 8 | `quality_status` | text | - | - | YES |
| 9 | `rejection_reason` | text | - | - | YES |
| 10 | `laboratory_id` | text | - | - | YES |

**silver.sales_order_lines** - 8 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `order_line_id` | text | - | - | YES |
| 2 | `order_id` | text | - | - | YES |
| 3 | `product_id` | text | - | - | YES |
| 4 | `quantity_ordered` | numeric | 12 | 2 | YES |
| 5 | `quantity_fulfilled` | numeric | 12 | 2 | YES |
| 6 | `unit_selling_price` | numeric | 12 | 2 | YES |
| 7 | `discount_amount` | numeric | 12 | 2 | YES |
| 8 | `line_total` | numeric | 12 | 2 | YES |

**silver.sales_orders** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `order_id` | text | - | - | YES |
| 2 | `customer_code` | text | - | - | YES |
| 3 | `order_timestamp` | timestamp without time zone | - | - | YES |
| 4 | `order_status` | text | - | - | YES |
| 5 | `expected_delivery_date` | date | - | - | YES |
| 6 | `actual_delivery_date` | date | - | - | YES |
| 7 | `payment_status` | text | - | - | YES |

**silver.suppliers** - 7 columns

| Ordinal | Column | Data type | Precision | Scale | Nullable |
|---:|---|---|---:|---:|---|
| 1 | `supplier_id` | text | - | - | YES |
| 2 | `supplier_name` | text | - | - | YES |
| 3 | `village` | text | - | - | YES |
| 4 | `district` | text | - | - | YES |
| 5 | `state` | text | - | - | YES |
| 6 | `supplier_type` | text | - | - | YES |
| 7 | `registration_date` | date | - | - | YES |


### Gold columns - Source 18

Gold column types are shown in the Type column of each Gold table section below (Gold Table 1 to Gold Table 6), taken from this same output. Gold has 73 columns in total: collection_centre_performance 10, procurement_quality_summary 23, production_performance 12, sales_daily_summary 9, sales_product_performance 9, supplier_performance 10.


## Source CSV files - Source 15
The source schema below comes from the notebook `dairychain.ipynb` (Source 15, 2026-11-11), from its `pd.read_csv` calls and stored outputs. These are source CSV columns, not Gold columns and not database columns. Do not use them as DDL. The notebook reads them from `/content/dairychain/DairyChain_dataset/data/raw`, after unzipping `DairyChain_dataset_full.zip`. Column order is the order shown in the stored outputs.

| File | Rows | Columns | Column list |
|---|---|---|---|
| `master/suppliers.csv` | 200 | 9 | supplier_id, supplier_name, village, district, state, supplier_type, registration_date, status, contact_reference |
| `master/collection_centres.csv` | 20 | 9 | collection_centre_id, centre_name, village, district, state, operating_capacity_litres, opening_time, closing_time, status |
| `master/products.csv` | 12 | 8 | product_id, product_name, category, unit_of_measure, standard_pack_size, shelf_life_days, selling_price, active_status |
| `procurement/milk_procurement.csv` | 18,000 | 10 | procurement_id, batch_id, supplier_id, collection_centre_id, procurement_timestamp, shift, quantity_litres, purchase_rate_per_litre, total_purchase_cost, acceptance_status |
| `procurement/quality_tests.csv` | 18,000 | 10 | test_id, batch_id, test_timestamp, fat_percentage, snf_percentage, temperature_c, acidity, quality_status, rejection_reason, laboratory_id |
| `production/production_batches.csv` | 4,000 | 7 | production_id, product_id, production_start, production_end, shift, production_status, supervisor_id |
| `production/production_inputs.csv` | 9,352 | 7 | production_input_id, production_id, source_batch_id, input_material_type, input_quantity, unit_of_measure, input_timestamp |
| `production/production_outputs.csv` | 8,000 | 7 | output_id, production_id, product_id, output_type, output_quantity, unit_of_measure, output_classification |
| `sales/sales_orders.csv` | 14,000 | 7 | order_id, customer_code, order_timestamp, order_status, expected_delivery_date, actual_delivery_date, payment_status |
| `sales/sales_order_lines.csv` | 28,000 | 8 | order_line_id, order_id, product_id, quantity_ordered, quantity_fulfilled, unit_selling_price, discount_amount, line_total |

Total source rows: 99,584, matching the README total. Derived columns added by the notebook itself, not in the CSVs: `procurement_timestamp_clean`, `calculated_cost`, `cost_difference`, `cost_status` on procurement; `temperature_status`, `rejection_reason_status`, `test_timestamp_clean` on quality tests; `duration_minutes` on production batches; `delivery_date_status`, `delivery_delay_days` on sales orders; `calculated_line_total` on sales order lines.

Column-name differences to note, all visible in the notebook:
- The quantity column is `quantity_litres`, not `quantity_liters`. Cell 34 used the American spelling and failed with a KeyError (BUG-001).
- The centres file is `collection_centres.csv`, not `collection_centers.csv`. Cell 63 used the American spelling and failed with a FileNotFoundError (BUG-002).
- Procurement uses `acceptance_status` and quality tests use `quality_status` for the same Accepted/Rejected outcome. The notebook checks they match and finds 0 mismatches in 18,000 records (cells 99, 100, 115).
- Production output classification values are `Primary product` and `By-product / residual`, with spaces around the slash. Cell 87 used `By-product/residual` and failed with a KeyError (BUG-003).
- The Gold column `quantity_litres` matches the source column of the same name.

## Gold Table 1 - Procurement Quality Summary

**Table:** `gold.procurement_quality_summary`

**Grain:** One record per procurement batch.

**Recorded row count:** 18,000.

### Purpose
This table contains batch-level procurement and milk quality information. It supports analysis of procurement volume, supplier performance, collection-centre activity, purchase costs, and milk quality.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `procurement_id` | text | Procurement record identifier |
| `batch_id` | text | Batch identifier |
| `procurement_timestamp` | timestamp with time zone | Date and time of procurement |
| `shift` | text | Procurement shift |
| `supplier_id` | text | Supplier identifier |
| `supplier_name` | text | Supplier name |
| `supplier_district` | text | Supplier district |
| `collection_centre_id` | text | Collection centre identifier |
| `centre_name` | text | Collection centre name |
| `centre_district` | text | Collection centre district |
| `quantity_litres` | numeric(12,2) | Milk quantity in litres |
| `purchase_rate_per_litre` | numeric(10,2) | Purchase rate per litre |
| `total_purchase_cost` | numeric(12,2) | Recorded total purchase cost |
| `calculated_purchase_cost` | numeric | Calculated purchase cost |
| `cost_difference` | numeric | Difference between recorded and calculated cost |
| `cost_status` | text | Cost comparison status |
| `fat_percentage` | numeric(6,3) | Milk fat percentage |
| `snf_percentage` | numeric(6,3) | Milk SNF percentage |
| `temperature_c` | numeric(6,3) | Temperature in Celsius |
| `acidity` | numeric(6,3) | Acidity measurement |
| `quality_status` | text | Accepted or rejected quality status |
| `rejection_reason` | text | Recorded reason for rejection |
| `laboratory_id` | text | Laboratory identifier |

### Business applications
This table can answer questions such as:

- How much milk was procured?
- How many batches were accepted or rejected?
- What was the milk-volume rejection rate?
- Which suppliers contributed the most milk?
- Which districts contributed the most procurement volume?
- What were the average fat and SNF measurements?
- What were the main rejection reasons?
- Were there differences between recorded and calculated purchase costs?

### Important calculation distinction
Two different rejection metrics can be calculated from this table. They must not be treated as interchangeable.

**Batch rejection rate**

Rejected Batches / Total Batches x 100

Recorded result: 2,311 / 18,000 x 100 = 12.84 percent.

**Milk-volume rejection rate**

Rejected Milk Volume / Total Milk Volume x 100

Recorded result: 1,117,247.35 L / 8,758,507.64 L x 100 = 12.76 percent.

## Gold Table 2 - Collection Centre Performance

**Table:** `gold.collection_centre_performance`

**Grain:** One record per collection centre.

**Recorded row count:** 20.

### Purpose
This table provides a collection-centre-level summary of milk procurement and quality performance.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `collection_centre_id` | text | Collection centre identifier |
| `centre_name` | text | Collection centre name |
| `centre_district` | text | Collection centre district |
| `total_batches` | bigint | Total procurement batches |
| `total_milk_litres` | numeric | Total milk volume |
| `accepted_milk_litres` | numeric | Accepted milk volume |
| `rejected_milk_litres` | numeric | Rejected milk volume |
| `rejection_rate_percentage` | numeric | Milk rejection percentage |
| `average_fat_percentage` | numeric | Average fat percentage |
| `average_snf_percentage` | numeric | Average SNF percentage |

### Business applications
- Compare collection-centre procurement volume.
- Identify centres with higher rejected milk volume.
- Compare rejection percentages.
- Review average milk quality measurements.
- Identify collection centres that may require further investigation.

### Grain consideration
A record in this table represents a centre, not a batch. Therefore `COUNT(*)` returns the number of centre records, not the total number of procurement batches. The `total_batches` column should be used when analysing batch counts across centres.

## Gold Table 3 - Supplier Performance

**Table:** `gold.supplier_performance`

**Grain:** One record per supplier.

**Recorded row count:** 200.

### Purpose
This table provides a supplier-level view of procurement and milk quality.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `supplier_id` | text | Supplier identifier |
| `supplier_name` | text | Supplier name |
| `supplier_district` | text | Supplier district |
| `total_batches` | bigint | Total procurement batches |
| `total_milk_litres` | numeric | Total milk volume |
| `accepted_milk_litres` | numeric | Accepted milk volume |
| `rejected_milk_litres` | numeric | Rejected milk volume |
| `rejection_rate_percentage` | numeric | Supplier rejection percentage |
| `average_fat_percentage` | numeric | Average fat percentage |
| `average_snf_percentage` | numeric | Average SNF percentage |

### Business applications
- Identify suppliers contributing the highest milk volume.
- Compare accepted and rejected milk.
- Review supplier-level rejection percentages.
- Compare average quality measurements.
- Identify suppliers requiring further quality investigation.

### Grain consideration
This is a supplier-level summary table. A supplier may have multiple procurement batches, but only one summary record in this table. For batch-level investigation, use `procurement_quality_summary`.

## Gold Table 4 - Production Performance

**Table:** `gold.production_performance`

**Grain:** One record per production batch.

**Recorded row count:** 4,000.

### Purpose
This table provides production-batch information required to analyse processing volume, finished output, byproduct output, and production duration.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `production_id` | text | Production batch identifier |
| `product_id` | text | Product identifier |
| `product_name` | text | Product name |
| `production_start` | timestamp without time zone | Production start timestamp |
| `production_end` | timestamp without time zone | Production end timestamp |
| `production_duration_minutes` | numeric | Production duration in minutes |
| `shift` | text | Production shift |
| `production_status` | text | Production status |
| `total_raw_milk_litres` | numeric | Raw milk input in litres |
| `finished_product_quantity` | numeric | Finished product output |
| `byproduct_quantity` | numeric | Byproduct output |
| `unit_of_measure` | text | Unit used for output measurement |

### Business applications
- Count production batches.
- Analyse raw milk input.
- Compare finished product output.
- Review production duration.
- Analyse output by product.
- Compare production shifts.
- Examine production quantities by unit of measurement.

### Important unit consideration
The project contains production output measured in both litres and kilograms. These measurements must be analysed separately. For example, 100 litres of output and 100 kilograms of output cannot simply be added together to produce a meaningful total. The `unit_of_measure` column is therefore important for correct analytical calculations. Production batches split as 3,001 litre-based batches and 999 kg-based batches, total 4,000 (Source 9).

## Gold Table 5 - Sales Product Performance

**Table:** `gold.sales_product_performance`

**Grain:** One record per product.

**Recorded row count:** 12.

### Purpose
This table provides product-level sales performance.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `product_id` | text | Product identifier |
| `product_name` | text | Product name |
| `category` | text | Product category |
| `total_orders` | bigint | Total orders associated with the product |
| `total_quantity_ordered` | numeric | Total quantity ordered |
| `total_quantity_fulfilled` | numeric | Total quantity fulfilled |
| `total_discount` | numeric | Total discount |
| `total_revenue` | numeric | Total revenue |
| `average_selling_price` | numeric | Average selling price recorded for the product |

### Business applications
- Rank products by revenue.
- Compare product categories.
- Analyse quantities ordered and fulfilled.
- Compare discounts.
- Identify products with higher average selling prices.
- Understand product-level sales performance.

### Interpretation consideration
`average_selling_price` is a product-level field. An unweighted average of this field across products is not necessarily the same as the weighted average selling price across all transactions.

## Gold Table 6 - Sales Daily Summary

**Table:** `gold.sales_daily_summary`

**Grain:** One record per date.

**Recorded row count:** 364.

### Purpose
This table provides daily sales and order-fulfilment metrics.

### Documented columns
| Column | Type (Source 18) | Business meaning |
|---|---|---|
| `order_date` | date | Sales order date |
| `total_orders` | bigint | Total orders |
| `delivered_orders` | bigint | Delivered orders |
| `partially_delivered_orders` | bigint | Partially delivered orders |
| `cancelled_orders` | bigint | Cancelled orders |
| `quantity_ordered` | numeric | Total quantity ordered |
| `quantity_fulfilled` | numeric | Total quantity fulfilled |
| `total_discount` | numeric | Total discount |
| `total_revenue` | numeric | Total revenue |

### Business applications
- Analyse daily revenue.
- Compare order volumes.
- Analyse quantity ordered versus quantity fulfilled.
- Examine sales trends over time.

### Grain consideration
This table contains one row per date. It is suitable for daily trend analysis, but it does not provide individual order-level detail.

## Dimension tables (Source 11)
Source: the user-supplied "DairyChain - Power BI Data Model" document (Source 11, 2026-11-11, section 4). These dimension tables are Power BI dimensions, not PostgreSQL tables. Their documented use is in the Power BI model. Their table names are now from Source 22: all 5 appear in the DiagramLayout of the supplied `dairy_chain_project.pbix`, with the 6 Gold tables. Their columns and DAX definitions are now from Source 23 (pbixray): the dims are DAX calculated tables derived from the Gold tables, with exact formulas in [../04_Business_Analytics/kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md). Their relationships are also now shown: only one relationship exists in the model, and none of the 10 intended dimension relationships exists - see the Source 23 note under each dimension below.

### dim_date
Purpose: support date-based filtering and time-series analysis. The date dimension connects with sales daily summary, procurement quality summary, and production performance.

Relevant columns:

| Column | Purpose |
|---|---|
| Date | Calendar date |
| Year | Year-based filtering |
| Quarter | Quarterly analysis |
| Month | Month number |
| Month Name | Month display |
| Day | Day of month |

Source 23: the `dim_date` DAX is CALENDAR over `gold sales_daily_summary[order_date]` only, which produces a single Date column.

Date relationships:

| Dimension column | Reporting column |
|---|---|
| `dim_date[Date]` | `sales_daily_summary[order_date]` |
| `dim_date[Date]` | `procurement_quality_summary[procurement_date]` |
| `dim_date[Date]` | `production_performance[production_date]` |

The procurement and production date fields are DAX calculated columns in the model, derived from the relevant timestamps. Source 23 shown the exact formulas: `procurement_date` = DATE(YEAR(procurement_timestamp), MONTH(procurement_timestamp), DAY(procurement_timestamp)) and `production_date` = DATE(YEAR(production_start), MONTH(production_start), DAY(production_start)). They are NOT columns in PostgreSQL. Source 23 also shown that none of the three date relationships in the table above exists in the model, so `dim_date` does not filter any Gold table through a relationship. See the updated mismatch note below.

Shown date dimension DAX (Source 23, pbixray). This is NOT the Source 11 reference implementation above it in the earlier version of this file: the model does not use a UNION of three date columns, it uses only `gold sales_daily_summary[order_date]`.

```dax
dim_date =
CALENDAR(
    MIN('gold sales_daily_summary'[order_date]),
    MAX('gold sales_daily_summary'[order_date])
)
```

Source 23: the shown date range is 2025-11-02 to 2026-10-31, from `gold sales_daily_summary[order_date]` in the model data. The date slicer cannot filter the other Gold tables through relationships, because none of those relationships exists in the model.

### dim_product
Purpose: support product-based analysis. This dimension connects product information to `sales_product_performance` and `production_performance`.

Relationship keys: `dim_product[product_id]`, `gold production_performance[product_id]`, and `gold sales_product_performance[product_id]`.

Source 23: no relationship from `dim_product` exists in the model. The keys above are the intended design only.

It supports filtering by product, product name, and product category. The product dimension should contain one unique record per product identifier.

### dim_supplier
Purpose: support supplier-level filtering and procurement analysis. This dimension connects with `procurement_quality_summary` and `supplier_performance`.

Relationship keys: `dim_supplier[supplier_id]`, `gold procurement_quality_summary[supplier_id]`, and `gold supplier_performance[supplier_id]`.

Source 23: no relationship from `dim_supplier` exists in the model. The one relationship that does exist links `gold procurement_quality_summary[supplier_id]` directly to `gold supplier_performance[supplier_id]`, not through `dim_supplier`.

It supports analysis by supplier and, where included in the dimension, supplier district.

### dim_collection_centre
Purpose: support collection-centre analysis. This dimension connects with `procurement_quality_summary` and `collection_centre_performance`.

Relationship keys: `dim_collection_centre[collection_centre_id]`, `gold procurement_quality_summary[collection_centre_id]`, and `gold collection_centre_performance[collection_centre_id]`.

Source 23: no relationship from `dim_collection_centre` exists in the model. The keys above are the intended design only.

It supports collection-centre-level comparisons and procurement analysis.

### dim_unit
Purpose: support production analysis by measurement unit. This dimension was created to address the requirement to separate production output measured in litres and kilograms.

DAX implementation, from Source 11, section 4.5, and from Source 7, section 5. Source 23 shown this DAX as the model formula:

```dax
dim_unit =
DISTINCT(
    SELECTCOLUMNS(
        'gold production_performance',
        "Unit",
        TRIM(
            'gold production_performance'[unit_of_measure]
        )
    )
)
```

Relationship: `dim_unit[Unit]` to `gold production_performance[unit_of_measure]`.

Expected design: one unique value per unit in `dim_unit`, one-to-many relationship, and single-direction filtering from the dimension to production data. The expected design above is intended design only.

## Columns
Known: the Gold column names and business meanings above, documented in Source 10, with data types and nullability now from Source 18. The column counts are 23 for procurement_quality_summary, 10 for collection_centre_performance, 10 for supplier_performance, 12 for production_performance, 9 for sales_product_performance, and 9 for sales_daily_summary. Bronze columns (82) and Silver columns (83) are also from Source 18, with types, in the section above. Every Gold column name matches the Source 10 list exactly, in the same order, with zero mismatches.

Indexes are absent for every table by Source 21 (a `pg_index` query over bronze, silver, and gold returned 0 rows). Primary keys, foreign keys, unique constraints, and check constraints are now absent in Source 20: a `pg_constraint` query over bronze, silver, and gold returned 0 rows. Do not invent a key or a constraint from a column name alone. One shown difference is recorded, not assumed away: Silver `suppliers` has 7 columns while Bronze `suppliers` has 9; `status` and `contact_reference` are not in `silver.suppliers`.

## Known mismatch: dim_date mapping columns - explained as derived date fields
The Power BI relationship mapping in Source 10, section 12, uses two column names that do not appear in the Gold column lists in sections 5 and 8 of the same document:

- `procurement_date` is used in the mapping `dim_date` to `procurement_quality_summary`, but the documented procurement column is `procurement_timestamp`, not `procurement_date`.
- `production_date` is used in the mapping `dim_date` to `production_performance`, but the documented production columns are `production_start` and `production_end`, not `production_date`.

Source 11, section 4.1, explains this: `procurement_date` and `production_date` are date-level fields derived from the relevant timestamps. The exact formulas are DAX calculated columns in the model: `procurement_date` on `gold procurement_quality_summary` = DATE(YEAR(procurement_timestamp), MONTH(procurement_timestamp), DAY(procurement_timestamp)), and `production_date` on `gold production_performance` = DATE(YEAR(production_start), MONTH(production_start), DAY(production_start)). They are NOT columns in PostgreSQL - the Source 18 column dump (238 rows) has no `procurement_date` or `production_date` in any Gold table. This note is kept here, in [analytics_methodology.md](../04_Business_Analytics/analytics_methodology.md), and in the check record, as a resolved mismatch. See the full mapping table in [analytics_methodology.md](../04_Business_Analytics/analytics_methodology.md).

## How to use this file
Use this file as a column-name, type, grain, count, and business-purpose reference. Column names, types, and nullability are from Source 18. Constraints are absent in Source 20: do not claim a key or constraint exists. Indexes are absent in Source 21. Source 23 shown the Power BI model DAX, relationships, and model-data totals; see the dimension sections above and [kpi_definitions.md](../04_Business_Analytics/kpi_definitions.md).

## Next step / Related files
- [Database design](database_design.md)
- [KPI definitions](../04_Business_Analytics/kpi_definitions.md)
- [Analytics methodology](../04_Business_Analytics/analytics_methodology.md)
- [check file](../../VERIFICATION_AND_MISSING_INFO.md)
