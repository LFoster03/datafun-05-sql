-- Create the Customers table
CREATE TABLE IF NOT EXISTS Customers (
    ID INTEGER PRIMARY KEY,     -- Unique ID for each customer
    Name TEXT NOT NULL,         -- Name of the customer
    Email TEXT NOT NULL UNIQUE  -- Email address of the customer
);

-- Create the Orders table
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,    -- Unique ID for each order
    OrderDate TEXT NOT NULL,        -- The date the order was made
    CustomerID INTEGER,             -- Foreign Key: ID of the customer
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID) -- Relationship between Orders and Customers
);
