import sqlite3
import pathlib
import pandas as pd
import os

def csv_to_sqlite(csv_files, db_file, table_names):
    """
    Inserts data from multiple CSV files into an SQLite3 database.

    :param csv_files: List of paths to the CSV files
    :param db_file: Path to the SQLite3 database file
    :param table_names: List of table names corresponding to the CSV files
    """
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        with sqlite3.connect(db_file) as conn:
            for csv_file, table_name in zip(csv_files, table_names):
                if os.path.exists(csv_file):
                    print(f"Processing {csv_file}...")

                    # Read the CSV into a pandas DataFrame
                    df = pd.read_csv(csv_file)

                    # Check if the DataFrame is empty
                    if df.empty:
                        print(f"Warning: {csv_file} is empty.")
                        continue

                    print(f"Data from {csv_file}:")
                    print(df.head())  # Show first few rows for debugging

                    # Insert data into the SQLite database (create table if it doesn't exist)
                    df.to_sql(table_name, conn, if_exists='replace', index=False)

                    print(f"Data from {csv_file} inserted into the '{table_name}' table in {db_file}.")
                else:
                    print(f"CSV file {csv_file} does not exist.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
csv_files = ['/Users/lindsayfoster/Projects/datafun-05-sql/module5_create/data/authors.csv', '/Users/lindsayfoster/Projects/datafun-05-sql/module5_create/data/books.csv']  # List of CSV files
db_file = '/Users/lindsayfoster/Projects/datafun-05-sql/project.sqlite3'  # SQLite database file
table_names = ['authors', 'books']  # Corresponding table names for the CSV files

csv_to_sqlite(csv_files, db_file, table_names)
