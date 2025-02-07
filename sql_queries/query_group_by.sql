-- query_group_by.sql

-- Group orders by CustomerID and calculate the total order amount for each customer
SELECT 
    CustomerID,
    COUNT(OrderID) AS NumberOfOrders,
    SUM(OrderTotal) AS TotalSpent
FROM Orders
GROUP BY CustomerID;
