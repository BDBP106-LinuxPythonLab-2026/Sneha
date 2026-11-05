# (5) Reading and Processing diabetes.csv Using Pandas

import pandas as pd

# Load the dataset
df = pd.read_csv('diabetes.csv')

# (i) Print all the column names
print("Column Names:")
print(df.columns.tolist())
print("-" * 40)

# (ii) Print the first 10 rows
print("First 10 Rows:")
print(df.head(10))
print("-" * 40)

# (iii) Print the mean of the BloodPressure column values
print("Mean of BloodPressure:")
print(df['BloodPressure'].mean())
print("-" * 40)

# (iv) Print the first 4 rows of columns 3, 4, 5 (Note: 0-indexed integer columns 3, 4, 5)
print("First 4 rows of columns 3, 4, 5:")
print(df.iloc[:4, 3:6])
print("-" * 40)

# (v) Add another column ’NormalizedBP’ using (max-min) normalization
bp_min = df['BloodPressure'].min()
bp_max = df['BloodPressure'].max()
df['NormalizedBP'] = (df['BloodPressure'] - bp_min) / (bp_max - bp_min)
print("NormalizedBP (first 5 rows):")
print(df[['BloodPressure', 'NormalizedBP']].head())
print("-" * 40)


# (vi) Write a function categorize_age(age) and create 'age_category' column
def categorize_age(age):
  if 1 <= age <= 18:
    return 'Youth'
  elif 19 <= age <= 50:
    return 'Adult'
  elif age > 50:
    return 'Senior'
  else:
    return 'Unknown'


# Assuming there is an 'Age' column in the dataframe
df['age_category'] = df['Age'].apply(categorize_age)
print("Age category (first 5 rows):")
print(df[['Age', 'age_category']].head())
