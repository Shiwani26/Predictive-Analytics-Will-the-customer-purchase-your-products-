

# Will the Customer Purchase Your Product?  A Predictive Analytics Approach

## Overview

As a business owner, one of the key priorities is understanding whether customers will purchase your product again, maintain loyalty, and avoid churn. Ultimately, everything revolves around the customer, as they determine the long-term sustainability of the business.

This project applies predictive analytics to assess customer behavior, identify purchasing trends, and calculate key performance metrics like churn rate, retention rate, and Net Promoter Score (NPS) using a comprehensive e-commerce dataset sourced from Kaggle.

##  Objectives

* Analyze customer purchasing behavior by age, gender, and value.
* Calculate customer churn rate and NPS.
* Build a predictive model to determine likelihood of repeat purchases.
* Provide data-driven recommendations to improve customer engagement and retention.

##  Dataset

The dataset (`shopping_trends.csv`) includes the following key features:

* Customer ID
* Age
* Gender
* Purchase Amount (USD)
* Review Rating
* Frequency of Purchases
* Promo Code Used
* Discount Applied
* Product Category

## Data Exploration

Basic checks and statistics were performed to understand the dataset:

```python
import pandas as pd

def load_data():
    return pd.read_csv("data/shopping_trends.csv")

data = load_data()
print(data.head())
print(data.info())
print(data.describe())
```

## Key Insights:

* Age: Average is 44 years (range: 18–70).
* Purchase Amount: Mean of \$59.76 (range: \$20–\$100).
* Review Rating: Average is 3.75/5.
* Previous Purchases: Average of 25, indicating repeat buying behavior.

### Age-Based Analysis
```
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

# Average review rating by age group
Age_review = df.groupby('AgeGroup', observed=True)['Review Rating'].mean().reset_index()
print(Age_review)
```

Customers aged 18–29 are the top spenders, contributing \~\$52,905. Spending is stable from **30–69**, then drops sharply beyond age 70.

###  Gender-Based Analysis
```
import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()

## gender based spending

gender_based = data.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based


##How much did each gender spend in each category
gender_based = data.groupby(['Gender', 'Category'])['Purchase Amount (USD)'].sum().reset_index(name='Total_Sales')
gender_based

## checking Male purchasing behavior

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
```

* Male customers spent \$157,890 vs \$75,191 by females.
* Both genders prefer Clothing and Accessories.
* Outerwear is the least purchased across both groups.

###  Value-Based Analysis
```
import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()

## Total spending per customer.
spending_per_customer = data.groupby('Customer ID')['Purchase Amount (USD)'].sum().reset_index()
spending_per_customer.head(10)

## identify high-value vs low-value customer

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


##Frequency of purchases (number of  customers purchases per month).


# Filter for Monthly purchasers
monthly_df = data[data['Frequency of Purchases'] == 'Weekly']

# Count number of 'Previous Purchases' records in that monthly group
num_of_purchase_per_month = monthly_df['Previous Purchases'].count()

print("Number of customers who purchase monthly:", num_of_purchase_per_month)
```
Customers were categorized as:
* **High-Value**: Above median total spending.
* **Low-Value**: Below median spending.
* **weekly purchases** : 539 Cutomers, showing strong recurring engagement

## Net Promoter Score (NPS)
NPS is a metric used to gauge customer loyalty and satisfaction by asking customers how likely they are to recommend a company’s product or service to others on a scale of 0 to 10. Respondents are classified into three categories:

# Promoters (9–10) : Loyal enthusiasts who promote your brand.
# Passives (7–8) : Satisfied but unenthusiastic.
# Detractors (0–6) : Unhappy customers who may harm your brand through negative word-of-mouth.
The NPS is calculated by subtracting the percentage of Detractors from the percentage of Promoters. A higher NPS indicates more customer loyalty and positive word-of-mouth, which are critical for business growth. To calculate the NPS, we will use review ratings as a proxy for overall satisfaction. Here’s how to calculate NPS:

NPS was calculated based on review ratings:

```python
data['NPS_Category'] = pd.cut(data['Review Rating'], bins=[2.5, 3.33, 4.17, 5],
                              labels=['Detractors', 'Passives', 'Promoters'], right=False)

nps_counts = data['NPS_Category'].value_counts(normalize=True) * 100
nps_score = nps_counts.get('Promoters', 0) - nps_counts.get('Detractors', 0)
```

### NPS Results:

* **Detractors**: 33.5%
* **Passives**: 32.7%
* **Promoters**: 31%
* **NPS Score**: **-1.59**

➡️ **Conclusion**: Customer loyalty is low, and experience improvement is necessary to convert detractors into promoters.

---

## 🤖 Predictive Analytics

We used a **Random Forest Classifier** to predict if a customer is likely to purchase next month:

### Feature Engineering:

* **Used\_Promo**, **Used\_Discount**
* **Previous Purchases**
* **Purchase Amount**

```python
X = data[['Previous Purchases', 'Purchase Amount (USD)', 'Used_Discount', 'Used_Promo']]
y = data['Likely_To_Purchase_Next_Month']
```

### Model Results:

* **Overall Accuracy**: 62%
* **Precision (Non-buyers)**: 0.71
* **Recall (Non-buyers)**: 0.77
* **Precision (Buyers)**: 0.27
* **Recall (Buyers)**: 0.22

➡️ The model is good at detecting **non-buyers**, but **struggles with buyers**, limiting its use for targeting repeat purchasers.

---

## 🔁 Churn Analysis

```python
churned = data['Likely_To_Purchase_Next_Month'] == 0
churn_rate = churned.mean() * 100
```

* **Churn Rate**: **72%**
* Indicates that most customers are **not expected to return** next month.

---

## 📌 Conclusion

The findings indicate that:

* **Customer churn is high (72%)**.
* **NPS score is negative (-1.59)**, showing dissatisfaction.
* **The predictive model struggles to identify loyal customers**, but can identify churned ones.

While segments like **young adults (18–29)** and **male shoppers** show potential, broader loyalty and satisfaction improvements are needed.

---

## 💡 Recommendations

### 1. Enhance Customer Experience

* Improve **delivery times**, **product quality**, and **website usability**.
* Collect direct feedback to identify pain points.

### 2. Targeted Promotions

* Offer **personalized discounts** to at-risk customers.
* Retarget **low-value** segments to reignite engagement.

### 3. Loyalty Programs

* Reward **frequent** and **high-spending** customers.
* Gamify shopping behavior with **tiered incentives**.

### 4. Segmented Marketing

* Personalize campaigns by **age**, **gender**, and **purchase category**.
* Focus on high-performing categories like **Clothing** and **Accessories**.

### 5. Improve Category Performance

* Reevaluate underperforming areas like **Outerwear**.
* Promote with **seasonal offers**, **bundle deals**, or **marketing push**.

---
