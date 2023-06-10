

  # Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_user",
    password="your_password"
    )


try:
  
    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # SQL query to create the table
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INTEGER,
            salary NUMERIC(10, 2)
        )
    '''

    # Execute the SQL query to create the table
    cur.execute(create_table_query)

    # Commit the transaction
    conn.commit()

    print("Table created successfully!")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL or creating the table:", error)

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()