from sklearn.preprocessing import StandardScaler
import pandas as pd

'''
Doing two things in here: 
scaling numeric data using standardscaler
encoding categorical data like gender into numbers
'''

df = pd.DataFrame({
    'Hours_studied': [2,3,4,5,6],
    'Sleep_hours': [8, 7,6,5,4],
    'Gender': ['Female', 'Male', 'Female', 'Male', 'Female'],
    'Passed': [0,0,1,1,1]
})
print(df)

# convert gender into numerical codes
df['Gender_Code'] = df['Gender'].astype('category').cat.codes
print(df[['Gender', 'Gender_Code']])

# Feature scaling
x = df[['Hours_studied', 'Sleep_hours', 'Gender_Code']]

# create scaler object
scaler = StandardScaler()

# fit and transform the features
x_scaled = scaler.fit_transform(x)

# optional: view as a dataframe
x_scaled_df = pd.DataFrame(x_scaled, columns=x.columns)
print(x_scaled_df)

y = df['Passed']