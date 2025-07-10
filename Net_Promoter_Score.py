import pandas as pd
from  Load_Data import load_data

# Load the data using the reusable function
data = load_data()


data['NPS_Category'] = pd.cut(
    data['Review Rating'], 
    bins=[2.5, 3.33, 4.17, 5],  
    labels=['Detractors', 'Passives', 'Promoters'],
    right=False


)

nps_counts = data['NPS_Category'].value_counts(normalize=True) * 100
nps_score = nps_counts.get('Promoters', 0) - nps_counts.get('Detractors', 0)

print(nps_counts)
print("NPS Score:", nps_score)

