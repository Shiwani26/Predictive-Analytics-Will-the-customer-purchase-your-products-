import pandas as pd
from Load_Data import load_data

# Load the data using the reusable function
data = load_data()

# Now you can safely use data.head()
print(data.head())


# Checking if there is any missing values
data.isnull().sum()

# Other exploration code
print(data.shape)
print(data.info())
print(data.describe())

