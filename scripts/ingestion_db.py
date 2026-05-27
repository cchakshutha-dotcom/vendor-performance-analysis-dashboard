"""
ingestion_db.py
---------------
Ingests vendor_sales_summary.csv into a SQLite database (vendor_performance.db).
Run this script before running any analysis notebooks.
"""

import pandas as pd
import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'vendor_sales_summary.csv')
DB_PATH   = os.path.join(os.path.dirname(__file__), '..', 'data', 'vendor_performance.db')

def ingest_data():
    logger.info("Loading CSV: %s", DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

    logger.info("Shape: %s", df.shape)
    logger.info("Columns: %s", list(df.columns))

    # Connect / create DB
    conn = sqlite3.connect(DB_PATH)
    logger.info("Connected to SQLite DB: %s", DB_PATH)

    # Write tables
    df.to_sql('vendor_sales', conn, if_exists='replace', index=False)
    logger.info("Table 'vendor_sales' written (%d rows)", len(df))

    # Create summary view
    conn.execute("""
        CREATE VIEW IF NOT EXISTS vendor_summary AS
        SELECT
            VendorName,
            COUNT(*)                          AS total_records,
            ROUND(SUM(TotalSales), 2)         AS total_sales,
            ROUND(SUM(GrossProfit), 2)        AS total_profit,
            ROUND(AVG(CAST(GrossProfit AS FLOAT)/NULLIF(TotalSales,0)*100), 2) AS avg_profit_margin,
            SUM(QuantitySold)                 AS total_qty_sold,
            SUM(QuantityOnHand)               AS total_qty_on_hand
        FROM vendor_sales
        GROUP BY VendorName
        ORDER BY total_sales DESC
    """)
    conn.commit()
    logger.info("View 'vendor_summary' created.")

    # Quick validation
    result = pd.read_sql("SELECT * FROM vendor_summary", conn)
    logger.info("Vendor Summary:\n%s", result.to_string(index=False))

    conn.close()
    logger.info("Ingestion complete.")

if __name__ == '__main__':
    ingest_data()
