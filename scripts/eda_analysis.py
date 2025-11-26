import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Path to cleaned data and visuals folder
data_path = "data/supermarket_sales_cleaned.csv"
visuals_folder = "visuals"

# Create visuals folder if it doesn't exist
os.makedirs(visuals_folder, exist_ok=True)

# 2. Load cleaned dataset
df = pd.read_csv(data_path)
df['date'] = pd.to_datetime(df['date'])  # ensure date is datetime

print("Data loaded. Shape:", df.shape)
print(df.head())

# -----------------------
# 3. Revenue by Category
# -----------------------
category_revenue = df.groupby("category_name")["total"].sum().sort_values(ascending=True)

plt.figure(figsize=(10,6))
category_revenue.plot(kind="barh", color="skyblue")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue (RMB)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "revenue_by_category.png"))
plt.close()
print("Saved revenue_by_category.png")

# -----------------------
# 4. Daily Sales Trend
# -----------------------
daily_sales = df.groupby("date")["total"].sum()

plt.figure(figsize=(12,6))
daily_sales.plot(color="orange")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (RMB)")
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "sales_trend.png"))
plt.close()
print("Saved sales_trend.png")

# -----------------------
# 5. Discount Analysis
# -----------------------
discount_counts = df["discount_yes/no"].value_counts()

plt.figure(figsize=(6,6))
discount_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["lightgreen", "salmon"])
plt.title("Discount vs No Discount")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "discount_pie.png"))
plt.close()
print("Saved discount_pie.png")

# -----------------------
# 6. Quantity Sold by Category
# -----------------------
category_quantity = df.groupby("category_name")["quantity_sold_kilo"].sum().sort_values(ascending=True)

plt.figure(figsize=(10,6))
category_quantity.plot(kind="barh", color="lightcoral")
plt.title("Total Quantity Sold by Category (kilo)")
plt.xlabel("Quantity Sold (kg)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "quantity_by_category.png"))
plt.close()
print("Saved quantity_by_category.png")

# -----------------------
# 7. Optional: Heatmap (Date vs Category)
# -----------------------
heat_data = df.pivot_table(values="total", index="category_name", columns="date", aggfunc="sum")

plt.figure(figsize=(15,8))
sns.heatmap(heat_data, cmap="Blues")
plt.title("Revenue Heatmap: Category vs Date")
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "heatmap_sales.png"))
plt.close()
print("Saved heatmap_sales.png")

print("EDA complete. All visuals saved in the 'visuals' folder.")
