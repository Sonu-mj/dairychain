# DairyChain synthetic dataset

This folder contains 10 related CSV datasets for a synthetic Indian dairy factory covering 2025-11-01 through 2026-10-31.

## Structure

- `data/raw/master/`: suppliers, collection centres, products
- `data/raw/procurement/`: milk procurement and quality tests
- `data/raw/production/`: production batches, inputs and outputs
- `data/raw/sales/`: sales orders and order lines

## Important modeling assumptions

- Every completed production batch consumes 650 L of accepted raw milk in FIFO order.
- For this starter model, each finished product is modeled as a simplified direct raw-milk conversion. Yield factors are illustrative synthetic assumptions, not engineering specifications.
- The second production output is a combined coproduct/residual amount to make the simplified input/output quantity balance explicit.
- Orders are processed chronologically and fulfilled quantities are capped by finished goods available by the order timestamp.
- Customer codes are external references; no customer master table is included in this 10-table starter scope.
- Five intentional data-quality scenarios are documented in the data dictionary.

## Start here

Load the CSVs into PostgreSQL Bronze as raw landing tables. Preserve source values, including the five intentional DQ scenarios.
