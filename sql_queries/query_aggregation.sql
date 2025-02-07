-- query_aggregation.sql

-- Aggregating data to get total, average, and count of orders
SELECT 
    COUNT(OrderID) AS TotalOrders,
    AVG(OrderTotal) AS AverageOrderAmount,
    SUM(OrderTotal) AS TotalSales
FROM Orders;
