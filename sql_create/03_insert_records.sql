-- Insert 10 customers
INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'Alice Johnson', 'alice.johnson@example.com'),
(2, 'Bob Smith', 'bob.smith@example.com'),
(3, 'Charlie Brown', 'charlie.brown@example.com'),
(4, 'Diana Prince', 'diana.prince@example.com'),
(5, 'Edward Harris', 'edward.harris@example.com'),
(6, 'Fiona Lee', 'fiona.lee@example.com'),
(7, 'George King', 'george.king@example.com'),
(8, 'Hannah Green', 'hannah.green@example.com'),
(9, 'Ian White', 'ian.white@example.com'),
(10, 'Jane Doe', 'jane.doe@example.com');

-- Insert 10 orders (each associated with a customer)
INSERT INTO Orders (OrderID, OrderDate, CustomerID) VALUES
(1, '2025-02-01', 1),
(2, '2025-02-02', 2),
(3, '2025-02-03', 3),
(4, '2025-02-04', 4),
(5, '2025-02-05', 5),
(6, '2025-02-06', 6),
(7, '2025-02-07', 7),
(8, '2025-02-08', 8),
(9, '2025-02-09', 9),
(10, '2025-02-10', 10);
