-- query_aggregation.sql

-- Count the number of books in the database
SELECT COUNT(*) AS total_books FROM books;

-- Average publish year of all books
SELECT AVG(publish_year) AS avg_publish_year FROM books;

-- Sum of publish years (just for demonstration)
SELECT SUM(publish_year) AS sum_publish_year FROM books;
