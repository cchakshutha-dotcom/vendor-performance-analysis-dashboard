"""
get_vendor_summary.py
---------------------
Reads vendor_sales_summary.csv, computes per-vendor KPIs, and
saves the result to data/vendor_performance_summary.csv.
"""

import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'vendor_sales_summary.csv')
OUT_PATH  = os.path.join(os.path.dirname(__file__), '..', 'data', 'vendor_performance_summary.csv')


def get_vendor_summary():
    logger.info("Reading data from: %s", DATA_PATH)
    df = pd.read_csv(DATA_PATH)
    df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
    df['ProfitMargin'] = ((df['GrossProfit'] / df['TotalSales']) * 100).round(2)

    summary = df.groupby('VendorName').agg(
        TotalSales=('TotalSales', 'sum'),
        TotalPurchaseCost=('TotalPurchaseCost', 'sum'),
        TotalGrossProfit=('GrossProfit', 'sum'),
        AvgProfitMargin=('ProfitMargin', 'mean'),
        TotalQtySold=('QuantitySold', 'sum'),
        TotalQtyOnHand=('QuantityOnHand', 'sum'),
        NumberOfTransactions=('VendorName', 'count'),
    ).reset_index()

    summary['TotalSales']        = summary['TotalSales'].round(2)
    summary['TotalPurchaseCost'] = summary['TotalPurchaseCost'].round(2)
    summary['TotalGrossProfit']  = summary['TotalGrossProfit'].round(2)
    summary['AvgProfitMargin']   = summary['AvgProfitMargin'].round(2)
    summary.sort_values('TotalSales', ascending=False, inplace=True)
    summary.reset_index(drop=True, inplace=True)

    logger.info("Vendor Summary:\n%s", summary.to_string(index=False))
    summary.to_csv(OUT_PATH, index=False)
    logger.info("Saved to: %s", OUT_PATH)
    return summary


if __name__ == '__main__':
    get_vendor_summary()
