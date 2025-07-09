import pandas as pd

# Load the CSV file into the 'data' variable
data = pd.read_csv("C:/Users/ankit/Documents/AAAAA SHIWANI/New Project/Python + Power BI/shopping_trends.csv")

# Now you can safely use data.head()
print(data.head())

# Other exploration code
print(data.shape)
print(data.info())
print(data.describe())

