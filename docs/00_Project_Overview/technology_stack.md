# Technology Stack


## Purpose
This file answers which tools DairyChain uses and what each tool is for. It is for a reader who needs to reproduce the setup or check a tool claim against the dependency files.

## In this file
- Tools and purpose
- Database
- Versions

## Tools and purpose
| Technology | Purpose |
|---|---|
| Python | Data ingestion and processing |
| Pandas | Data manipulation and transformation |
| PostgreSQL 18.6 | Relational database and data storage |
| SQL | Data cleaning, transformation and analytical queries |
| Power BI | Business intelligence and interactive reporting |
| DAX | Measures and analytical calculations |
| Git and GitHub | Version control and project documentation |

## Database
The project database is named `dairychain`. It contains three main schemas: `bronze`, `silver`, and `gold`. PostgreSQL version 18.6 is confirmed by the user-supplied System Architecture document (Source 8, 2026-11-11).

## Versions
Exact versions and packages must be checked against the Colab notebook imports, where it can be checked. Do not invent package versions and do not create an assumed requirements.txt (Source 14, 2026-11-11).

## Previously reported environment, not confirmed current
The brief reported an earlier environment: Windows, PowerShell, VS Code, Python 3.13.6, pip 25.2, and a project virtual environment named `.venv`. A database creation attempt in that environment had met an authentication error. Do not present those values as the current environment. PostgreSQL 18.6 is shown by Source 8, and Source 17 shows the server version 18.6 from a successful connection (localhost, port 5432, user postgres, database dairychain). The earlier authentication error is resolved as the current state.

## Related tools in the brief
The brief also named NumPy, PyArrow, CSV and Parquet as part of the project context. The Python implementation is in Google Colab notebooks (.ipynb), not separate local scripts (Source 14, 2026-11-11).

## Next step / Related files
- [System architecture](../02_System_Architecture/system_architecture.md)
- [Data ingestion](../03_Data_Engineering/data_ingestion.md)
- [check file](../../VERIFICATION_AND_MISSING_INFO.md)
