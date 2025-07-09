import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()

# create age group
bins = [18, 30, 40, 50, 60, 70, 80, 90, 101]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Sorting the age group
df = data.sort_values(by='AgeGroup', ascending=True)
df.head()

# Spending as per age group

total_spending_by_age = df.groupby('AgeGroup', observed=True)['Purchase Amount (USD)'].sum().reset_index()
total_spending_by_age.columns = ['AgeGroup', 'Total_Spending']
total_spending_by_age

