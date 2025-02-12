import sqlite3
import pathlib
import pandas as pd
import os

def combine_csv_to_db(csv_files, db_file):
    """
    Combine multiple CSV files into an SQLite database.

    :param csv_files: List of paths to the CSV files to be combined.
    :param db_file: Path to the SQLite database file.
    """
    try:
        # Connect to the SQLite database (this creates the file if it doesn't exist)
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            
            for csv_file in csv_files:
                if os.path.exists(csv_file):
                    print(f"Processing {csv_file}...")

                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(csv_file)

                    # Get the table name from the CSV filename (remove extension)
                    table_name = os.path.splitext(os.path.basename(csv_file))[0]

                    # Write the data to the SQLite database
                    df.to_sql(table_name, conn, if_exists='replace', index=False)

                    print(f"Data from {csv_file} inserted into table {table_name}.")
                else:
                    print(f"CSV file {csv_file} does not exist.")
    except sqlite3.Error as e:
        print(f"Error while processing CSV files: {e}")

# Example usage:
csv_files = ['/Users/lindsayfoster/Projects/datafun-05-sql/module5_create/data/authors.csv', '/Users/lindsayfoster/Projects/datafun-05-sql/module5_create/data/books.csv']  # List of CSV files
db_file = 'my_database.db'  # SQLite database file

combine_csv_to_db(csv_files, db_file)
