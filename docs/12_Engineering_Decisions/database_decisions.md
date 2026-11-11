# Database Decisions

> Status: PARTIALLY VERIFIED

## Purpose
This file answers why PostgreSQL was chosen for DairyChain and what that choice does and does not prove. It is for a reader who needs the database reason, not only its name.

## In this file
- The choice
- Why PostgreSQL fits
- What it does not prove
- Status

## The choice
PostgreSQL 18 is the relational database for DairyChain. It stores Bronze, Silver and Gold, and it runs the SQL that cleans, transforms and analyses the data.

## Why PostgreSQL fits
PostgreSQL fits structured business data: suppliers, batches, products, orders and days, with keys between them. It supports joins, aggregations, CTEs, window functions and transactions, which are the tools this project needs. It also supports the reconciliation checks that prove a Gold total matches its Silver source.

## What it does not prove
Choosing PostgreSQL does not prove the database was created, connected or loaded successfully. The brief reported an earlier authentication error during database creation. Status: RESOLVED by Source 17, which verifies a successful connection (localhost, port 5432, user postgres, database dairychain, server PostgreSQL 18.6). A successful load still needs a run log, which was not supplied.

## Status
The choice is VERIFIED as a README statement. The successful use of the database is PENDING EVIDENCE.

## Next step / Related files
- Architecture decisions](architecture_decisions.md)
- System architecture](../02_System_Architecture/system_architecture.md)
- Verification file](../../VERIFICATION_AND_MISSING_INFO.md)
