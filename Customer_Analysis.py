import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()

# Total spending per customer.
spending_per_customer = data.groupby('Customer ID')['Purchase Amount (USD)'].sum().reset_index()
spending_per_customer.head(10)

# identify high-value vs low-value customer

#  Calculate total spending per customer
data['Total_Spent'] = data['Purchase Amount (USD)']  
customer_spending = data.groupby('Customer ID')['Total_Spent'].sum().reset_index()

#  Define a threshold to split high vs low value
threshold = customer_spending['Total_Spent'].median()  

#  Label customers
customer_spending['Customer_Value'] = customer_spending['Total_Spent'].apply(
    lambda x: 'High-Value' if x >= threshold else 'Low-Value'
)

print(customer_spending.head(10))


# Average purchase amount per category.

Average_purchase = data.groupby('Category')['Purchase Amount (USD)'].mean().reset_index()
Average_purchase

#Frequency of purchases (number of  customers purchases per month).


# Filter for Monthly purchasers
monthly_df = data[data['Frequency of Purchases'] == 'Weekly']

# Count number of 'Previous Purchases' records in that monthly group
num_of_purchase_per_month = monthly_df['Previous Purchases'].count()

print("Number of customers who purchase monthly:", num_of_purchase_per_month)

