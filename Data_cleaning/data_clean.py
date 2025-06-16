'''
Things to learn in this chapter
- Missing values
- Invalid types
- Incorrect values
- Outliers
- Duplicate rows
- Statistical sanitization
'''

import pandas as pd
import numpy as np

# loading the dirty dataset
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

df.columns = df.columns.str.strip().str.replace('"', '')
print(df.columns)


df.info()
df.head()
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Handlig missing values
# count nulls in each column
print(df.isnull().sum())

# drop rows with any missing value
df_cleaned = df.dropna()
print('After dropping rows with missing values: ')
print(df_cleaned)

# Or fill missing with a value
df['Weight(Pounds)'] = df['Weight(Pounds)'].fillna(df['Weight(Pounds)'].mean())
# replace missing values in your dataset with mean or median (don't drop)



# fixing invalid types
df['Weight(Pounds)'] = pd.to_numeric(df['Weight(Pounds)'], errors='coerce')
df['Height(Inches)'] = pd.to_numeric(df['Height(Inches)'], errors='coerce')

# Remove duplicates
df.duplicated().sum()
df = df.drop_duplicates()

# Remove outliers (using IQR)
Q1 = df['Weight(Pounds)'].quantile(0.25)
Q3 = df['Height(Inches)'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1-1.5*IQR
upper_bound = Q3+1.5*IQR

# filter out outliers
df = df[(df['Weight(Pounds)'] >= lower_bound) & (df['Weight(Pounds)'] <= upper_bound)]

# use IQR to remove outliers in both height and weight

# Bonus: logical sanitization
# example: weight should be >20 kg and <200 kg
df = df[(df['Weight(Pounds)'] > 20) & (df['Weight(Pounds)'] < 200)]


df.to_csv('cleaned_data.csv', index=False)
