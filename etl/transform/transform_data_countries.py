import numpy as np
import pandas as pd

# Connect with csv file
df = pd.read_csv('C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/processed/countries_processed.csv')

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
print(df.iloc[1])

# chose the columns
df = df[[   
         'Country'
        , 'Region'
        , 'Population'
        , 'Pop. Density (per sq. mi.)'
        , 'Infant mortality (per 1000 births)'
        , 'GDP ($ per capita)'
        , 'Literacy (%)'
        , 'Climate'
        , 'Birthrate'
        , 'Deathrate'
        , ]]

# # rename columns
df = df.rename(columns={  
          'Country':'country'
        , 'Region':'region'
        , 'Population':'population'
        , 'Pop. Density (per sq. mi.)': 'pop_density'
        , 'Infant mortality (per 1000 births)':'infant_mortality'
        , 'GDP ($ per capita)':'GDP_p_capita'
        , 'Literacy (%)': 'literacy'
        , 'Climate':'climate'
        , 'Birthrate':'birthrate'
        , 'Deathrate':'deathrate'})

print(df.columns)

print('Types')
print(df.dtypes)

# Cleaning and manipularion
# remove the non-numeric characters and convert the string to a numeric type. 
df['pop_density'] = df['pop_density'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
df['literacy'] = df['literacy'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
df['birthrate'] = df['birthrate'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
df['deathrate'] = df['deathrate'].str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# # Types again
print('NewTypes')
print(df.dtypes)

# # Specify the new folder path
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/processed/'

# # Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'countries_processed_2.csv', index=False)

print("File saved successfully!")
