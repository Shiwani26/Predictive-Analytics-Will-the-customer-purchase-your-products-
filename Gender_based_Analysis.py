import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()

# gender based spending

gender_based = data.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based


#How much did each gender spend in each category
gender_based = data.groupby(['Gender', 'Category'])['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based

# checking Male purchasing behavior

# Filter for males
male_df = data[data['Gender'] == 'Male']

# Group by category and sum purchase amounts
male_category_spending = (
    male_df.groupby('Category')['Purchase Amount (USD)'] .sum().reset_index().sort_values(by='Purchase Amount (USD)', ascending=False)
)

print(male_category_spending)


# for female spending
# Filter for female
female_df = data[data['Gender'] == 'Female']

# Group by category and sum purchase amounts
female_category_spending = (
    female_df.groupby('Category')['Purchase Amount (USD)'] .sum().reset_index().sort_values(by='Purchase Amount (USD)', ascending=False)
)

print(female_category_spending)
