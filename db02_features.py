import sqlite3
import os

# Define the database file (SQLite)
db_file = "mydatabase.sqlite3"

def run_sql_script(script_path):
    """Function to run SQL script on the SQLite database."""
    with open(script_path, 'r') as file:
        sql_script = file.read()

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        print(f"Successfully executed {script_path}")
    except sqlite3.Error as e:
        print(f"Error executing {script_path}: {e}")
    finally:
        conn.close()

def query_database(query):
    """Function to run a simple query and print results."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query Results:")
        for row in result:
            print(row)
    except sqlite3.Error as e:
        print(f"Error querying the database: {e}")
    finally:
        conn.close()

def main():
    """Main function to run SQL operations."""
    
    # Step 1: Execute the update records SQL script
    run_sql_script('sql_features/update_records.sql')

    # Step 2: Execute the delete records SQL script
    run_sql_script('sql_features/delete_records.sql')
    
    # Step 3: Query the Customers table to verify changes (showing the first 5 customers)
    query_database("SELECT * FROM Customers LIMIT 5;")

    # Step 4: Query the Orders table to verify updates and deletions
    query_database("SELECT * FROM Orders;")

if __name__ == "__main__":
    main()
