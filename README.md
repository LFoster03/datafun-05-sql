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
