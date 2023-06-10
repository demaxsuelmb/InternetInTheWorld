import pandas as pd
import psycopg2

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


# # rename columns
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
print(df.head())


# # PostgreSQL connection details
# conn = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="12345678",
#     host="localhost",
#     port="5432"
# )

# # schema name
# schema_name= "public"
# # table to insert the data into
# table_name = "f_internet"



# # Iterate over DataFrame rows and insert into the database
# with conn.cursor() as cursor:
#     for index, row in df.iterrows():
#         values = [row['lead_id'], row['lead_nome'], row['dt_cadastro'], row['updateDate'], row['mktLink'], row['publicLink'], row['stage'], row['city'], row['state'], row['country'], row['industry_id'], row['industry'], row['source_id'], row['source_name'], row['subSource_id'], row['subsource']]
#         insert_query = f"INSERT INTO {table_name} (lead_id, lead_nome, dt_cadastro, updateDate, mktLink, publicLink, stage, city, state, country, industry_id, industry, source_id, source_name, subSource_id, subsource) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#         cursor.execute(insert_query, values)

#     conn.commit()

# # Close the database connection
# conn.close()