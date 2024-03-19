import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Read JSON data into pandas DataFrame
json_file_path = "/home/jigs/Documents/dashboard/myproject/jsondata.json"
df = pd.read_json(json_file_path)

# Establish connection to PostgreSQL database
engine = create_engine('postgres://postgres:IIT@cse1@localhost:5432/jdatabase')

# Replace 'username', 'password', 'localhost', '5432', and 'database_name' with your actual database credentials

# Insert data into PostgreSQL table
df.to_sql('insights', engine, if_exists='append', index=False)
