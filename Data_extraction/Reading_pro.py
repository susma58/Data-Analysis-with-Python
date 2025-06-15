# reading files project
# loading the files
import pandas as pd

data = pd.read_csv('hw.csv')

print(data.head()) # provide first five data

print(data.info()) # give details regarding dataset

print(data.shape) # provide rows and columns
print('Rows and columns:', data.shape)


print(data.describe()) # provide all statistical info


