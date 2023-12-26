import pandas as pd

# Connect with csv file
df = pd.read_csv('data/raw/internet.csv', delimiter=';')

# transform in a DataFrame
df = pd.DataFrame(df)


# Convert selected columns to float using a loop
columns_to_convert = [
                    'Cellular Subscription'
                    ,'Internet Users(%)'
                    ,'No. of Internet Users'
                    ,'Broadband Subscription'
                    ]


# Convert selected columns to int using a loop
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')


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


# Save in the csv file
# Specify the new folder path
output_folder = 'data/processed/'
# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'internet_processed.csv', index=False)

print("\nFile saved successfully!")