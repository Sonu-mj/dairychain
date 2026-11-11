# DairyChain data dictionary

All data is synthetic. IDs are stable business keys within this generated dataset. The simulation period is **2025-11-01 through 2026-10-31**.

## Master data

### `suppliers.csv` - 200 rows
| Column | Meaning |
|---|---|
| `supplier_id` | Supplier primary key (`SUP-####`). |
| `supplier_name` | Synthetic farmer, cooperative or farm name. |
| `village`, `district`, `state` | Supplier location. |
| `supplier_type` | Supplier classification. |
| `registration_date` | Supplier registration date. |
| `status` | Supplier status; one deliberately lowercase value is included. |
| `contact_reference` | Synthetic non-contact reference token. |

### `collection_centres.csv` - 20 rows
| Column | Meaning |
|---|---|
| `collection_centre_id` | Collection-centre primary key (`CC-###`). |
| `centre_name`, `village`, `district`, `state` | Centre identity and location. |
| `operating_capacity_litres` | Nominal daily collection capacity. |
| `opening_time`, `closing_time` | Local operating hours. |
| `status` | Centre operating status. |

### `products.csv` - 12 rows
| Column | Meaning |
|---|---|
| `product_id` | Product primary key (`PRD-###`). |
| `product_name`, `category` | Product description and category. |
| `unit_of_measure` | Finished product unit (`Litre` or `Kilogram`). |
| `standard_pack_size` | Nominal retail pack configuration. |
| `shelf_life_days` | Synthetic shelf-life assumption. |
| `selling_price` | Synthetic unit selling price in INR. |
| `active_status` | Product status. |

## Procurement and quality

### `milk_procurement.csv` - 18,000 rows
| Column | Meaning |
|---|---|
| `procurement_id` | Procurement primary key (`PRC-######`). |
| `batch_id` | Raw milk batch key (`MBT-######`); links to `quality_tests.batch_id` and `production_inputs.source_batch_id`. |
| `supplier_id`, `collection_centre_id` | Foreign keys to supplier and collection-centre masters. |
| `procurement_timestamp` | Milk receipt timestamp. One intentional non-ISO timestamp is included. |
| `shift` | Morning or Evening collection shift. |
| `quantity_litres` | Received raw milk volume. |
| `purchase_rate_per_litre` | Synthetic purchase rate in INR/L. |
| `total_purchase_cost` | Extended purchase cost in INR; one intentional 25% mismatch is included. |
| `acceptance_status` | Accepted or Rejected based on quality thresholds. |

### `quality_tests.csv` - 18,000 rows
| Column | Meaning |
|---|---|
| `test_id` | Quality-test primary key (`QCT-######`). |
| `batch_id` | Raw milk batch reference to `milk_procurement.batch_id`. |
| `test_timestamp` | Quality test timestamp. |
| `fat_percentage`, `snf_percentage` | Fat and solids-not-fat readings. |
| `temperature_c` | Milk temperature in Celsius; one intentional NULL is included. |
| `acidity` | Acidity reading. |
| `quality_status`, `rejection_reason` | Acceptance result and primary rejection reason. |
| `laboratory_id` | Synthetic laboratory identifier. |

## Production

### `production_batches.csv` - 4,000 rows
| Column | Meaning |
|---|---|
| `production_id` | Production batch primary key (`PRD-B-#####`). |
| `product_id` | Foreign key to `products.product_id`. |
| `production_start`, `production_end` | Production window. |
| `shift` | Shift derived from start time. |
| `production_status` | Batch status; all generated runs are Completed. |
| `supervisor_id` | Synthetic supervisor identifier. |

### `production_inputs.csv` - generated row count
| Column | Meaning |
|---|---|
| `production_input_id` | Production-input primary key (`PIN-######`). |
| `production_id` | Foreign key to `production_batches.production_id`. |
| `source_batch_id` | Foreign key to accepted `milk_procurement.batch_id`. |
| `input_material_type` | Input material; currently `Raw Milk`. |
| `input_quantity`, `unit_of_measure` | Consumed quantity and unit. Each completed batch consumes 650 L in total. |
| `input_timestamp` | Timestamp at which the material is consumed; source receipt is at or before this time. |

### `production_outputs.csv` - 8,000 rows
| Column | Meaning |
|---|---|
| `output_id` | Production-output primary key (`POU-######`). |
| `production_id` | Foreign key to `production_batches.production_id`. |
| `product_id` | Foreign key to `products.product_id`. |
| `output_type` | Primary product or combined coproduct/residual description. |
| `output_quantity`, `unit_of_measure` | Output quantity and product unit. |
| `output_classification` | `Primary product` or `By-product / residual`. |

## Sales

### `sales_orders.csv` - 14,000 rows
| Column | Meaning |
|---|---|
| `order_id` | Sales-order primary key (`ORD-######`). |
| `customer_code` | Synthetic external customer reference; no customer master is included. |
| `order_timestamp` | Chronologically sorted order timestamp. |
| `order_status` | Delivered, Partially Delivered or Cancelled. |
| `expected_delivery_date`, `actual_delivery_date` | Expected and simulated actual delivery dates. |
| `payment_status` | Paid, Pending, Partially Paid or Void. |

### `sales_order_lines.csv` - 28,000 rows
| Column | Meaning |
|---|---|
| `order_line_id` | Sales-order-line primary key (`ORL-######`). |
| `order_id` | Foreign key to `sales_orders.order_id`. |
| `product_id` | Foreign key to `products.product_id`. |
| `quantity_ordered`, `quantity_fulfilled` | Requested and fulfilled quantities in product units. |
| `unit_selling_price` | Selling price in INR per product unit. |
| `discount_amount`, `line_total` | Discount and net line value in INR. |

## Intentional data-quality scenarios

1. `SUP-0015`: lowercase supplier status (`active`).
2. `SUP-0042`: leading/trailing whitespace in supplier village.
3. `PRC-000500`: procurement timestamp formatted as `DD/MM/YYYY HH:MM` rather than ISO.
4. `PRC-001000`: total purchase cost is inflated by 25% relative to quantity × rate.
5. `QCT-000250`: `temperature_c` is NULL.

## Modeling caveat

This is a **starter synthetic dataset**, not an engineering-grade dairy process simulator. Every finished product is modeled as a simplified direct conversion from raw milk, with illustrative yield factors. The second output is a combined coproduct/residual quantity, not a detailed material lineage model. Do not treat the yield factors or simulated prices as real-world operating benchmarks.
