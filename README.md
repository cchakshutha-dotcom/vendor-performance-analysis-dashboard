# 🏢 Vendor Performance Data Analytics — End-to-End Project

> **Based on:** YouTube Tutorial — *Vendor Performance Data Analytics End-To-End Project | SQL + Python + Power BI + Reporting*
> **Video:** https://youtu.be/nmCfNHjfgEY

---

## 📌 Project Overview

This project analyzes **vendor sales performance** across 10 vendors and 7 product categories for the year 2023. It covers the full data analytics pipeline:

- Data Ingestion → SQLite database
- Data Cleaning & Feature Engineering
- Exploratory Data Analysis (EDA)
- 12 Business Visualizations
- Vendor KPI Summary Report
- SQL-based Analysis

---

## 📂 Project Structure

```
Vendor_Performance_Analysis/
├── data/
│   ├── vendor_sales_summary.csv          ← Raw dataset (2,000 records)
│   ├── vendor_sales_cleaned.csv          ← Cleaned + engineered dataset
│   ├── vendor_performance_summary.csv    ← KPI summary per vendor
│   └── vendor_performance.db            ← SQLite database
│
├── notebooks/
│   └── Vendor_Performance_Analysis.ipynb ← Main Jupyter Notebook (fully executed)
│
├── scripts/
│   ├── ingestion_db.py                   ← Load CSV → SQLite DB
│   ├── get_vendor_summary.py             ← Generate vendor KPI summary
│   └── generate_charts.py               ← Standalone chart generation
│
├── output_graphs/
│   ├── 01_total_sales_by_vendor.png
│   ├── 02_gross_profit_by_vendor.png
│   ├── 03_profit_margin_by_vendor.png
│   ├── 04_sales_by_category.png
│   ├── 05_monthly_sales_trend.png
│   ├── 06_quarterly_sales_by_vendor.png
│   ├── 07_quantity_sold_by_vendor.png
│   ├── 08_correlation_heatmap.png
│   ├── 09_sales_vs_profit_scatter.png
│   ├── 10_profit_margin_distribution.png
│   ├── 11_sales_distribution_pie.png
│   └── 12_inventory_on_hand.png
│
└── README.md
```

---

## 🛠️ Software Required

- Python 3.8+
- Jupyter Notebook / VS Code

---

## 📦 Installation

```bash
pip install pandas numpy matplotlib seaborn openpyxl
```

---

## 🚀 How to Run

**Step 1:** Extract the ZIP file

**Step 2:** Open the project folder in VS Code or Terminal

**Step 3:** (Optional) Run ingestion script to set up SQLite DB:
```bash
python scripts/ingestion_db.py
```

**Step 4:** Launch Jupyter Notebook:
```bash
jupyter notebook
```

**Step 5:** Open `notebooks/Vendor_Performance_Analysis.ipynb`

**Step 6:** Click **Kernel → Restart & Run All**

---

## 📊 Dataset Columns

| Column | Description |
|--------|-------------|
| VendorName | Name of the vendor |
| Brand | Associated brand |
| Category | Product category |
| PurchasePrice | Cost price per unit |
| ActualPrice | Selling price per unit |
| QuantitySold | Units sold |
| QuantityOnHand | Current inventory |
| TotalSales | Revenue (ActualPrice × Qty) |
| TotalPurchaseCost | Cost (PurchasePrice × Qty) |
| GrossProfit | TotalSales − TotalPurchaseCost |
| PurchaseDate | Transaction date |

---

## 📈 Output Charts (12 Visualizations)

1. Total Sales by Vendor
2. Total Gross Profit by Vendor
3. Average Profit Margin by Vendor
4. Total Sales by Category (Horizontal Bar)
5. Monthly Sales Trend (Line Chart)
6. Quarterly Sales by Vendor (Grouped Bar)
7. Total Quantity Sold by Vendor
8. Correlation Heatmap of Numeric Features
9. Total Sales vs Gross Profit (Scatter Plot)
10. Profit Margin Distribution by Vendor (Box Plot)
11. Sales Distribution by Category (Pie Chart)
12. Inventory on Hand by Vendor

---

## 💡 Key Business Insights

1. **Apex Supplies** is the top vendor — $10.6M in sales (2023)
2. **Icon Wholesale** has the highest profit margin at **42.96%**
3. All vendors maintain margins between **40–43%** — stable pricing policy
4. **Apex Supplies** carries the most inventory risk (55,135 units on hand)
5. Monthly sales are consistent — no extreme seasonal fluctuations
6. All 7 product categories contribute roughly equally to total revenue

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computation |
| Matplotlib | Chart creation |
| Seaborn | Statistical visualizations |
| SQLite3 | Database storage & SQL queries |
| Jupyter Notebook | Interactive analysis environment |
