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

# Added CSV files books.csv and authors.csv to a data file.
