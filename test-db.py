import psycopg2
from psycopg2 import OperationalError

def create_connection(dsn):
    connection = None
    try:
        connection = psycopg2.connect(dsn)
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

# Replace with your actual DSN
dsn = "postgresql://kratos:secret@localhost:5434/kratos"

# Test the connection
conn = create_connection(dsn)
if conn:
    print("Connection successful")
    # create a table in the PostgreSQL database
    