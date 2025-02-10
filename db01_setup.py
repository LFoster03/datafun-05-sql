import sqlite3
import os

# Path to the database file
db_file = 'library.setup.db'

# Function to run a SQL file
def run_sql_file(cursor, filename):
    with open(filename, 'r') as f:
        sql = f.read()
        cursor.executescript(sql)

# Main function to set up the database
def setup_database():
    # Check if the database exists, and delete it if so
    if os.path.exists(db_file):
        os.remove(db_file)

    # Create a new SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # Run the SQL scripts to create tables and insert records
        run_sql_file(cursor, 'sql_create/01_drop_tables.sql')  # Drop tables if they exist
        run_sql_file(cursor, 'sql_create/02_create_tables.sql')  # Create tables
        run_sql_file(cursor, 'sql_create/03_insert_records.sql')  # Insert records

        # Commit changes and close the connection
        conn.commit()
        print("Database created and records inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

# Run the setup function
if __name__ == '__main__':
    setup_database()
