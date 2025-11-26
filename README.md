Supermarket Sales Insights Analysis

A data analysis project exploring supermarket sales data to uncover patterns, customer behavior, and revenue insights using Python, SQL, and data visualization.

📊 Key Features

> Data cleaning and preprocessing with Python (Pandas)

> Exploratory Data Analysis (EDA) with Matplotlib and Seaborn

> Example SQL queries for data exploration

> Business insights for sales optimization

> Visualizations saved for reporting

🛠 Tech Stack

> Python (Pandas, NumPy, Matplotlib, Seaborn)

> Jupyter Notebook

> SQL (SQLite / MySQL / PostgreSQL – example queries)

> Git & GitHub

📁 Project Structure

supermarket-sales-analysis/
│
├── data/
│     └── supermarket_sales_cleaned.csv
│
├── notebooks/
│     └── sales_analysis.ipynb
│
├── scripts/
│     ├── data_cleaning.py
│     ├── eda_analysis.py
│     └── sql_queries.sql
│
├── visuals/
│     ├── revenue_by_category.png
│     ├── sales_trend.png
│     ├── discount_pie.png
│     ├── quantity_by_category.png
│     └── heatmap_sales.png
│
├── README.md
└── requirements.txt


🚀 How to Run

1. Clone the repo
   
git clone https://github.com/mann-0/supermarket-sales-analysis.git

cd supermarket-sales-analysis

3. Setup virtual environment
   
python -m venv venv

# Activate venv (Windows)

venv\Scripts\activate

# Activate venv (Mac/Linux)

source venv/bin/activate

3. Install dependencies
   
pip install -r requirements.txt

5. Run scripts
   
python scripts/data_cleaning.py       # Combine & clean CSV files

python scripts/eda_analysis.py        # Generate visualizations

7. Open Jupyter Notebook (optional)
   
jupyter notebook notebooks/sales_analysis.ipynb

🧠 Business Insights (Examples)

Top-selling categories: Certain product categories dominate revenue

Daily sales trends: Peak sales occur on specific dates

Discount impact: Discounts increase sales volume

Quantity sold: Food/vegetable categories have the highest quantity sold

Revenue heatmaps: Show patterns over time and by category

📌 SQL Queries (Examples)

The scripts/sql_queries.sql file contains example queries such as:

Top 10 selling products by revenue

Daily average revenue

Revenue by category

Discount impact analysis

Top items by quantity sold

📌 Author

Mann Kumar

GitHub: https://github.com/mann-0

LinkedIn: https://www.linkedin.com/in/mann-kumar-70396839a/
