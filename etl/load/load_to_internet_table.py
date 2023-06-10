import pandas as pd
import psycopg2
import json

path_file = "data/processed/internet_processed_2.csv"

# Convert JSON data to a DataFrame
df = pd.read_csv(path_file)

# Print the DataFrame
print(df.columns)

df = df[[
          'index'
        , 'entity'
        , 'code'
        , 'year'
        , 'cellulars'
        , 'percent_users'
        , 'users'
        , 'broadband'
        ]]

# rename columns
df = df.rename(columns={'index': 'index_num',
                        'year' : 'date_year'})

# Change type of columns
data_types={
          'index_num' : int
        , 'entity' : str
        , 'code' : str
        , 'date_year' : int
        , 'cellulars': int
        , 'percent_users' : float
        , 'users' : int
        , 'broadband' : int 
            }

# change the type
df = df.astype(data_types)

with open('config/config.json') as f:
    config = json.load(f)

# Access the configuration values
database_config = config['database']

# PostgreSQL connection details
conn = psycopg2.connect(
      database = database_config['database'],
      user = database_config['user'],
      password = database_config['password'],
      host = database_config['host'],
      port= database_config['port']
)

# schema name
schema_name= "public"
# table to insert the data into
table_name = "f_internet"

# Iterate over DataFrame rows and insert into the database
with conn.cursor() as cursor:
    for index, row in df.iterrows():
        values = [row['index_num'], row['entity'], row['code'], row['date_year'], row['cellulars'], row['percent_users'], row['users'], row['broadband']]
        insert_query = f"INSERT INTO {table_name} (index_num, entity, code, date_year, cellulars, percent_users, users, broadband) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, values)

    conn.commit()

# Close the database connection
conn.close()