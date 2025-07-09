import pandas as pd

def load_data():
    return pd.read_csv("C:/Users/ankit/Documents/AAAAA SHIWANI/New Project/Python + Power BI/shopping_trends.csv")

# Call the function directly
data = load_data()

print(data.head())