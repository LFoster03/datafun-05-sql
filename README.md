# datafun-05-sql
Module 5 - learning SQL
# Database Schema Design

# Library Database Schema

This project defines a simple database schema for a library system with two related tables: `authors` and `books`.

## Schema Design

1. **authors** table:
   - `author_id`: Primary key, integer, autoincrement.
   - `first_name`: Text, the first name of the author.
   - `last_name`: Text, the last name of the author.
   - `birth_date`: Date, the birth date of the author.

2. **books** table:
   - `book_id`: Primary key, integer, autoincrement.
   - `title`: Text, the title of the book.
   - `publish_year`: Integer, the year the book was published.
   - `author_id`: Foreign key, integer, references the `author_id` in the `authors` table.

## SQL Files

1. **01_drop_tables.sql**: Drops the `authors` and `books` tables if they already exist.
2. **02_create_tables.sql**: Creates the `authors` and `books` tables with a foreign key constraint.
3. **03_insert_records.sql**: Inserts 10 records into the `authors` and `books` tables.

## Python Script

- **db01_setup.py**: A Python script that automates the creation of the database, schema, and insertion of records. Run this script to set up the database.

## Instructions

1. Install Python and SQLite3 on your machine.
2. Place the `db01_setup.py` script and the `sql_create` folder (with the SQL files) in the same directory.
3. Run the Python script by executing `python db01_setup.py` to create the database and insert records.
4. The database will be created as `library.db` in the same directory.

# Library Database Features

This project extends the functionality of the library database to perform various operations such as updating records, deleting records, adding new columns, and querying data.

## SQL Features

### 1. **update_records.sql**
This SQL file updates records in the database. For example, the `publish_year` for the book "1984" is updated.

sql
UPDATE books
SET publish_year = 2023
WHERE title = '1984';

# Library Database Queries

This project demonstrates various SQL queries for aggregations, filtering, sorting, grouping, and joining data in an SQLite database. Additionally, Python is used to execute the SQL queries and visualize the results.

# Library Database Queries

This project demonstrates various SQL queries for aggregations, filtering, sorting, grouping, and joining data in an SQLite database. Additionally, Python is used to execute the SQL queries and visualize the results.

## SQL Queries

### 1. **query_aggregation.sql**
Performs aggregation functions:
- `COUNT()`: Counts the number of books in the database.
- `AVG()`: Computes the average publish year of books.
- `SUM()`: Sums the publish years (for demonstration).

### 2. **query_filter.sql**
Filters records using the `WHERE` clause:
- Books published after 1950.
- Books written by a specific author (e.g., 'J.K. Rowling').

### 3. **query_sorting.sql**
Sorts records using the `ORDER BY` clause:
- Books sorted by publish year in ascending order.
- Books sorted by title in descending order.

### 4. **query_group_by.sql**
Groups records by author and performs aggregation:
- Counts the number of books per author.
- Computes the average publish year of books per author.

### 5. **query_join.sql**
Joins the `books` and `authors` tables:
- Retrieves books along with their authors' names using `INNER JOIN`.
- Retrieves all books along with authors, including authors without books (using `LEFT JOIN`).

## Python Script

### db03_queries.py
This Python script executes the SQL queries and visualizes the data using `matplotlib`.

- It runs aggregation queries, filter queries, sorting queries, grouping queries, and join queries.
- It visualizes the number of books per author with a bar chart.

## Instructions

1. Place the SQL queries (`query_aggregation.sql`, `query_filter.sql`, `query_sorting.sql`, `query_group_by.sql`, `query_join.sql`) and the Python script (`db03_queries.py`) in the appropriate folders.
2. Install required Python libraries: `sqlite3` (for interacting with the database) and `matplotlib` (for visualizations).

## Added CSV files books.csv and authors.csv to a data file.

## Created a new database called project.sqlite3 using the books.csv and the authors.csv
Created a function to create the database. Used one input - the Path to the database file to create. 

## Created some tables for the database. Using the SQL CREATE TABLE statements. Also added some code to DROP TABLE IF EXISTS before creating (or recreating) the tables.

## Inserted the data from my csv files into my project.sqlite3 file to populate tables. 

### Instructions
Loop Through Both Files:
The script loops through each CSV file and its corresponding table name using zip(csv_files, table_names). This pairs each CSV file with its table name.

Processing Each CSV:
For each CSV file, the script reads the data into a pandas DataFrame (df = pd.read_csv(csv_file)).
It checks if the CSV file is empty, and if it is, it skips processing that file.
The data is then inserted into the corresponding table in the SQLite database using df.to_sql(table_name, conn, if_exists='replace', index=False).

Database Insertions:
The if_exists='replace' argument means that the table will be dropped and recreated if it already exists. If you want to append the data to the existing table instead, use if_exists='append'.
Error Handling:
The script includes try-except blocks to handle potential errors like missing files or SQLite connection issues.
Example Code: 
```import sqlite3
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
```

## Git Commit


