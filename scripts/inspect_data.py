import pandas as pd
import os

# Path to data folder
data_folder = "data"

# List all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
print("Found CSV files:", csv_files)

# Read and inspect each CSV
for file in csv_files:
    print("\n--- Inspecting:", file, "---")
    df = pd.read_csv(os.path.join(data_folder, file))
    
    # Print basic info
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("First 5 rows:")
    print(df.head())

