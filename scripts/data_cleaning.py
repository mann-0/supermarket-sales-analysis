import pandas as pd
import os

# 1. Path to data folder
data_folder = "data"

# 2. Read CSVs
annex1 = pd.read_csv(os.path.join(data_folder, "annex1.csv"))  # item info
annex2 = pd.read_csv(os.path.join(data_folder, "annex2.csv"))  # sales
annex3 = pd.read_csv(os.path.join(data_folder, "annex3.csv"))  # wholesale price
annex4 = pd.read_csv(os.path.join(data_folder, "annex4.csv"))  # loss rate

print("CSV files loaded successfully.")

# 3. Merge annex1 & annex4 into sales (annex2)
# Merge item info
df = annex2.merge(annex1[['Item Code', 'Item Name', 'Category Name']], on='Item Code', how='left')

# Merge loss rate
df = df.merge(annex4[['Item Code', 'Loss Rate (%)']], on='Item Code', how='left')

# Merge wholesale price on Item Code + Date
df = df.merge(annex3[['Date', 'Item Code', 'Wholesale Price (RMB/kg)']],
              on=['Date', 'Item Code'], how='left')

print("All merges complete. Shape:", df.shape)

# 4. Clean column names
df.columns = df.columns.str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

# 5. Convert date column
df['date'] = pd.to_datetime(df['date'])

# 6. Compute total revenue per transaction
df['total'] = df['quantity_sold_kilo'] * df['unit_selling_price_rmb/kg']

# 7. Drop rows missing essential columns
essential_columns = ['date', 'item_code', 'quantity_sold_kilo', 'unit_selling_price_rmb/kg']
df = df.dropna(subset=essential_columns)

print("After cleaning, shape:", df.shape)

# 8. Save cleaned CSV
cleaned_path = os.path.join(data_folder, "supermarket_sales_cleaned.csv")
df.to_csv(cleaned_path, index=False)

print(f"Cleaned data saved as '{cleaned_path}'")
