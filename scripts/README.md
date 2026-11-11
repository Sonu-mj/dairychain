# Scripts

`dairychain.ipynb` is the Python implementation. It was developed in Google Colab, not as local scripts. It has 148 code cells and uses pandas only: it unzips the dataset, reads the 10 CSV files, cleans timestamps, calculates purchase costs and cost mismatches, applies the rejection rules (SNF below 8.2, fat below 3.2, acidity above 0.17, temperature above 8.5C), and validates the data. It has no SQL, no database connection, and no Bronze load.

No `scripts/load_bronze.py` file has been supplied. The whiteboard diagram in `docs/assets/architecture-whiteboard.png` names that file, SQLAlchemy, and psycopg, but none of those are verified. They are labelled unconfirmed in the docs. If the ingestion script is added, put it here.
