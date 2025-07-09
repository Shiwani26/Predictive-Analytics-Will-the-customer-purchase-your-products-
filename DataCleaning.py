import pandas as pd
import os

print("Current working directory:", os.getcwd())

try:
    data = pd.read_csv("C:/Users/ankit/Documents/AAAAA SHIWANI/New Project/Python + Power BI/shopping_trends.csv")
    print("✅ CSV Loaded Successfully!\n")
    print(data.head())
except FileNotFoundError:
    print("❌ Error: CSV file not found. Please check the file path.")
except Exception as e:
    print("❌ An unexpected error occurred:", e)
