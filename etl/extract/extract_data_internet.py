import pandas as pd

# Connect with csv file
df = pd.read_csv('C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/raw/internet.csv', delimiter=';')

# Specify the new folder path
output_folder = 'C:/Users/demaxsuel.batista/Documents/Python Scripts/03 - analises e port/01 - project DE - Internet/data/processed/'

# transform in a DataFrame
df = pd.DataFrame(df)
# print a sample of data
print(df.head())

# Save the DataFrame as a new CSV file in the output folder
df.to_csv(output_folder + 'internet_processed.csv', index=False)

print("File saved successfully!")