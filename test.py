import sqlite3

try:
    conn = sqlite3.connect('yourdatabase.db')
    print("Database connected successfully!")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")

import sqlite3

def run_query():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('yourdatabase.db')
        cursor = conn.cursor()
        
        print("Connected to the database!")
        
        # Run a simple query
        cursor.execute("SELECT * FROM books LIMIT 5;")
        
        # Fetch and print the results
        results = cursor.fetchall()
        if results:
            print("Query Results:")
            for row in results:
                print(row)
        else:
            print("No results found.")
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run_query()

