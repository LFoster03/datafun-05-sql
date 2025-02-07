import sqlite3
import os

# Define the database file (SQLite)
db_file = "mydatabase.sqlite3"

def create_database():
    """Create a database, define the schema, and insert records."""

    # If the database exists, remove it to restart
    if os.path.exists(db_file):
        os.remove(db_file)

    # Connect to the SQLite database (it will be created)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Step 1: Drop existing tables (to restart)
    with open('sql_create/01_drop_tables.sql', 'r') as file:
        cursor.executescript(file.read())

    # Step 2: Create the tables (schema)
    with open('sql_create/02_create_tables.sql', 'r') as file:
        cursor.executescript(file.read())

    # Step 3: Insert records into tables
    with open('sql_create/03_insert_records.sql', 'r') as file:
        cursor.executescript(file.read())

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Database and tables created, and records inserted successfully.")

if __name__ == "__main__":
    create_database()
