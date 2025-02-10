import sqlite3
import os

# Path to the database file
db_file = 'library.features.db'

# Function to run a SQL file
def run_sql_file(cursor, filename):
    with open(filename, 'r') as f:
        sql = f.read()
        cursor.executescript(sql)

# Function to demonstrate SQL features like updating, deleting records
def demonstrate_sql_features():
    # Create or connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # Run update operation (update publish year for '1984')
        print("Updating records...")
        run_sql_file(cursor, 'sql_features/update_records.sql')
        
        # Run delete operation (delete 'Animal Farm' from books)
        print("Deleting records...")
        run_sql_file(cursor, 'sql_features/delete_records.sql')

        # Commit changes and check the records after updates and deletes
        conn.commit()

        # Query to display the updated books
        print("Books after update and delete operations:")
        cursor.execute("SELECT title, publish_year FROM books ORDER BY publish_year DESC")
        books = cursor.fetchall()
        for book in books:
            print(book)

        # Add a new column to the 'books' table (e.g., genre)
        print("Adding a new column 'genre' to the books table...")
        cursor.execute("ALTER TABLE books ADD COLUMN genre TEXT")

        # Update the genre for some books
        cursor.execute("UPDATE books SET genre = 'Dystopian' WHERE title = '1984'")
        cursor.execute("UPDATE books SET genre = 'Fantasy' WHERE title = 'The Hobbit'")

        # Query to check the books with their genres
        print("Books with their genres:")
        cursor.execute("SELECT title, genre FROM books")
        books = cursor.fetchall()
        for book in books:
            print(book)

        # Commit changes
        conn.commit()

        print("Database operations completed successfully.")
    
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        conn.rollback()
    
    finally:
        conn.close()

# Run the feature demonstration
if __name__ == '__main__':
    demonstrate_sql_features()
