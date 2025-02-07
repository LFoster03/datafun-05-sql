# datafun-05-sql
Module 5 - learning SQL
# Database Schema Design

This database contains two tables: `Customers` and `Orders`.

### Customers Table:
- `ID` (INTEGER, Primary Key) - The unique identifier for each customer.
- `Name` (TEXT) - The name of the customer.
- `Email` (TEXT) - The customer's email address (unique).

### Orders Table:
- `OrderID` (INTEGER, Primary Key) - The unique identifier for each order.
- `OrderDate` (TEXT) - The date when the order was placed.
- `CustomerID` (INTEGER, Foreign Key) - The reference to the `ID` from the `Customers` table. This establishes a one-to-many relationship between `Customers` and `Orders`.

### Relationship:
- Each **customer** can have multiple **orders**, but each **order** belongs to only one **customer**.
- The `Orders` table has a foreign key (`CustomerID`) that links to the `Customers` table's `ID`.

### How to Use:
1. Clone or download the repository.
2. Run the `db01_setup.py` script to set up the database and insert records.
3. The database will be created with the `Customers` and `Orders` tables, populated with sample data.

1. SQL Scripts
The project includes the following SQL scripts, which are used to perform database operations:

update_records.sql: This script is used to update one or more records in a table.

Example: Updating the OrderDate of a specific OrderID in the Orders table.
delete_records.sql: This script is used to delete one or more records from a table.

Example: Deleting all records in the Orders table for a specific CustomerID.
2. Python Script
db02_features.py: This Python script demonstrates how to execute the SQL scripts (update_records.sql and delete_records.sql) to perform updates and deletions. It also includes functions to query the database to verify changes after performing these operations.

# Database Queries and Analysis Project

This project demonstrates how to use SQL queries to perform various operations on a SQLite database, including aggregation, filtering, sorting, grouping, and joining. Additionally, the project utilizes Python to execute the SQL queries, summarize the results, and visualize the data.

## Project Structure

1. Query aggregation

## SQL Query Files

### 1. `query_aggregation.sql`
This SQL file demonstrates how to use aggregation functions such as `COUNT`, `AVG`, and `SUM` to summarize data. It helps analyze datasets by counting records, averaging values, and calculating totals.

Example query:

```sql
-- query_aggregation.sql
SELECT 
    COUNT(OrderID) AS TotalOrders,
    AVG(OrderTotal) AS AverageOrderAmount,
    SUM(OrderTotal) AS TotalSales
FROM Orders;

2. Query Filter
This SQL file demonstrates filtering data using the WHERE clause. It allows you to query data based on specific conditions.
-- query_filter.sql
SELECT * FROM Orders
WHERE OrderTotal > 100;

3. Query Sorting
This SQL file demonstrates sorting data using the ORDER BY clause. You can sort data in ascending or descending order based on one or more columns.
-- query_sorting.sql
SELECT * FROM Orders
ORDER BY OrderDate DESC;

4. Query Group By
This SQL file demonstrates grouping data using the GROUP BY clause, often with aggregation functions like COUNT or SUM, to summarize data at a group level (e.g., by customer or category).
-- query_group_by.sql
SELECT 
    CustomerID,
    COUNT(OrderID) AS NumberOfOrders,
    SUM(OrderTotal) AS TotalSpent
FROM Orders
GROUP BY CustomerID;

5. Query Join
This SQL file demonstrates joining tables using the INNER JOIN and LEFT JOIN clauses. It allows you to combine data from multiple tables based on a related column.
-- query_join.sql
SELECT 
    Orders.OrderID, 
    Orders.OrderDate, 
    Customers.CustomerName, 
    Orders.OrderTotal
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

6. Python Script (db03_queries.py)
This Python script demonstrates how to run the SQL queries defined above, execute them on a SQLite database, and summarize or visualize the results.