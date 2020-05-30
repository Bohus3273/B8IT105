# -*- coding: utf-8 -*-
"""
@author: DUDO3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# reading dataset, used dataset from purchase orders
dataset = pd.read_csv('Wholesale_Purchase.csv')
df = pd.DataFrame(data=dataset)

# setting option to display all columns from dataset 
pd.set_option('display.max_columns', None)

# examining data 
dataset.head() # dataset to display top rows from dataset
dataset.shape # returning size of the dataset - 440 rows x 9 columns

# using info() to return dataset columns with their datatypes, 
# this is also used to review for missing values in rows  
dataset.info() 
dataset.describe() # basic info on each column (no rows, mean, std, etc.)

dataset.columns  # columns index - display all column names 

# renaming value in Customer column
df['Customer_Type'].replace({'Hotel/Restaurant/Cafe':'HRC'}, inplace=True)

# checking counts of values in object variables
df['Customer_Type'].value_counts()
df['Region'].value_counts()

# filtering dataset by Customer_Type - creating 3 new dataframes for each type
is_retail = df['Customer_Type']=='Retail'
df_retail = df[is_retail]
print(df_retail)

# filtering using 2 conditions customer_type and region
customer = ['Retail']
region = ['Dublin']
df_ret2 = df[df.Customer_Type.isin(customer) & df.Region.isin(region)]
print(df_ret2)

# create series with specific columns (customer_type,region,fresh,milk)
ser1 = df.loc[:, ['Customer_Type', 'Region', 'Fresh', 'Milk']]
print(ser1)

# pivot table using ser1

table = pd.pivot_table(ser1, values=['Fresh', 'Milk'],
                       index=['Region', 'Customer_Type'],
                       aggfunc={'Fresh' : [min, max, np.sum],
                                'Milk' : [min, max, np.sum]})
table

# filtering table
table.query('Customer_Type == ["HRC"]')


# plotting stacked bar chart to display sum per region for each product
plotset = df.groupby('Region')[dataset.columns[3:]].sum()
print(plotset)

plotset.plot.bar()

plotset[dataset.columns[3:]].plot(kind="barh",
        stacked=True).legend(loc='upper right', ncol=2, title="Food Category")
plt.title('Food Sales')
plt.xlabel('Quantity')


