import numpy as np
import pandas as pd

# Connect with csv file
df = pd.read_csv('C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/processed/internet_processed.csv')

# Overview of DataFrame
print('shape')
print(df.shape)

# Overview of DataFrame
print('columns')
print(df.columns)

# Overview of DataFrame
print('Types')
print(df.dtypes)

# summary statistics of numeral columns
print('Describe')
print(df.describe())

# Missing values
print('missing values')
print(df.isnull().sum())

# Head of DataFrame
print('head 5')
print(df.head())

# Cleaning and manipularion
# remove the non-numeric characters and convert the string to a numeric type. 
df['Cellular Subscription'] = df['Cellular Subscription'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float).astype(int)
df['No. of Internet Users'] = df['No. of Internet Users'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float).astype(int)
df['Broadband Subscription'] = df['Broadband Subscription'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float).astype(int)
df['Internet Users(%)'] = df['Internet Users(%)'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Types again
print('Types')
print(df.dtypes)

# rename columns
df = df.rename(columns={  'Cellular Subscription': 'cellulars'
                   , 'No. of Internet Users': 'users'
                   , 'Broadband Subscription': 'broadband'
                   , 'Internet Users(%)': 'percent_users'
                   , 'Code': 'code'
                   , 'Entity': 'entity'
                   , 'Year': 'year' })


print(df.columns)

# Specify the new folder path
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/processed/'

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'internet_processed_2.csv', index=False)

print("File saved successfully!")
