# Feature column: Year_Diff
df['Year_Diff'] = df['Year_First_Transaction'] - df['Year_Last_Transaction']

# Nama-nama feature columns
feature_columns = ['Average_Transaction_Amount', 'Count_Transaction', 'Year_Diff']

# Features variable
X = df[feature_columns] 

# Target variable
y = df['is_churn'] 
