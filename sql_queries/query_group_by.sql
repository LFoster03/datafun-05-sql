-- query_group_by.sql

-- Count the number of books per author
SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS num_books
FROM authors
JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id;

-- Get the average publish year of books per author
SELECT authors.first_name, authors.last_name, AVG(books.publish_year) AS avg_publish_year
FROM authors
JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id;
