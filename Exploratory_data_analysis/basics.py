'''
Things to learn in here:
Summary Stats: describe your data numerically
Data distributions: understand shapes of variables
Correlation: measure relationships between variables
Visualization: spot trends, patterns, outliers
Hypothesis testing: validate claims using statistics
Reporting: present insights clearly
'''

# libraries used
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
from scipy import stats

# Summary statistics
df.describe()
df.info()
df['Column'].value_counts()

# Data Distributions
# histogram
sns.histplot(df['Height'], kde=True)
plt.title("Height Distribution")
plt.show()

# boxplot (detect outliers)
sns.boxplot(x=df['Weight'])
plt.title("Weight Distribution")
plt.show()

# Correlation Matrix
correlation = df.corr(numeric_only = True)
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Use .corr() to check strength of relationships from -1 to +1
# Closer to +1 = Strong correlation


# Hypothesis Testing (t-test)
# Are male and female heights significantly different?
male = df[df['Gender'] == 'Male']['Height']
female = df[df['Gender'] == 'Female']['Height']

t_stat, p_val = stats.ttest_ind(male, female, equal_var=False)

print(f'T-statistic: {t_stat:.3F}')
print(f'P-value: {p_val:.4f}')

# if p-value<0.05, the difference is statistically significant

# Correlation vs causation
'''
Correlation show patterns, not reason
To test cause, use:
- experiments
- randomized studies
- advanced modeling 

'''


# More visualizations
# Pairplot (relationships between all variables)
sns.pairplot(df)

# countplot for categorical data
sns.countplot(data=df, x='Gender')

# scatterplot
sns.scatterplot(data=df, x='Height', y='Weight', hue='Gender')



"""
Reporting insights
use clear visuals
mention key findings (e.g. Male students are on average 5 cm taller.)
Use stats + plots together
Be honest if you didn't find a significant pattern



Practice task
Use your cleaned dataset from wrangling
describe all numerical features
Plot: histogram, boxplot, pairplot
calculate correlation matrix
use t-test between two groups
generate a short "data report" with key findings, insights and potential next steps

"""