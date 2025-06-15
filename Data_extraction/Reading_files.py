"""
Load and inspect data from various formats
Understand structure of data
Basic inspection tools (.head, info, describe())
"""

import pandas as pd
# csv files
df_csv = pd.read_csv('data.csv')
print(df_csv.head())

# json files
df_json = pd.read_json('data.json')
print(df_json.head())

# excel files
df_excel = pd.read_excel('data.xlsx')
print(df_excel.head())

# xml files
import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)