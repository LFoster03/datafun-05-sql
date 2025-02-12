import sqlite3
import pathlib

# Define the path to the SQLite database file
db_file = 'my_database.db'  # SQLite database file in your project root

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")  # Path to the SQL file
            with open(sql_file, "r") as file:
                sql_script = file.read()  # Read the SQL commands from the file
            conn.executescript(sql_script)  # Execute the SQL commands
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

