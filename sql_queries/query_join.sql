-- query_join.sql

-- INNER JOIN: Join Orders and Customers based on CustomerID
SELECT 
    Orders.OrderID, 
    Orders.OrderDate, 
    Customers.CustomerName, 
    Orders.OrderTotal
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- LEFT JOIN: Include customers without orders
SELECT 
    Customers.CustomerName, 
    Orders.OrderID, 
    Orders.OrderTotal
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;
