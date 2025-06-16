'''
Key concepts you'll master
- Reshaping: change rows - columns (wide vs long)
- Merging: combine datasets by key
- Categorical data: encode text into numbers
- Hierarchial indexing: multi-index for grouped data
- Indexing: smart row/column selection
'''

import pandas as pd
import numpy as np
# RESHAPING
# Reshaping with .melt() and .pivot()
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Math': [85, 90],
    'Science': [80, 95]
})

df_long = pd.melt(df, id_vars='Name', var_name='Subject', value_name='Score')
print(df_long)

# Long wide format
df_wide = df_long.pivot(index='Name', columns='Subject', values='Score').reset_index()
print(df_wide)


# COMBINING DATAFRAMES
# Merging with .merge()
students = pd.DataFrame({
    'ID': [1,2,3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

grades = pd.DataFrame({
    'ID': [1,2],
    'Grade': ['A', 'B']
})

merged = pd.merge(students, grades, on = 'ID', how='left')
print(merged)


"""
inner: only matching rows
left: all from left + matches
outer: union of all
right: all from right + matches
"""

# Concatenation stacking
df1 = pd.DataFrame({'A': [1,2]})
df2 = pd.DataFrame({'A': [3,4]})


pd.concat([df1, df2], ignore_index=True)



# HANDLING
# Handling categorical data
df = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Green']})

# convert to category
df['Color'] = df['Color'].astype('category')

# encoding to numbers
df['Color_Code'] = df['Color'].cat.codes


# HIERARCHIAL INDEXING (Multiindex)
data = pd.DataFrame({
    'City': ['Kathmandu', 'Kathmandu', 'Pokhara', 'Pokhara'],
    'Year': [2020, 2021, 2022, 2021],
    'Population': [1000000, 1100000, 2000000, 2100000]
})

data = data.set_index(['City', 'Year'])
print(data)



# SMART INDEXING AND SELECTION
# .loc for labels, iloc for positions
df.loc[df['Subject'] == 'Math']     # by condition
df.iloc[0:3]                        # first 3 rows
df.set_index('Name').loc['Alice']   # specific index



"""
Exercise Task:
Create two dataframes: students and scores
Merge them with .merge(), using left join
Reshape them to long format using .melt()
Encode subjects as categories'
Use .pivot() to retun to wide format
Set multi-index using Name and Subject
Filter scores for a specific student using .loc[]
"""