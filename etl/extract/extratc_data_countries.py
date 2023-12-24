# Extract Data of Countries

# import libraries
import pandas as pd
import matplotlib as plt 

# Connect with csv file
df = pd.read_csv('data/raw/countries.csv', delimiter=';')

# transform in a DataFrame
df = pd.DataFrame(df)

# changing comma to dot
df = df.replace({',': '.'}, regex=True)

# Basic informations
# headers - the first few rows of the DataFrame
print("\nhead")
print(df.head(5))
# info - data types and missing values
print("\ninfo")
print(df.info())
# describe - statistics for numerical columns
print("\ndescribe")
print(df.describe())
# Count of unique values in each column
print("\nnunique")
print(df.nunique())

# Specify the new folder path
output_folder = 'data/processed/'
# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'countries_processed.csv', index=False)

print("\nFile saved successfully!")