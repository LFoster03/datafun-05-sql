-- query_join.sql

-- Get books with their authors' first and last names
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Get all books with authors, including authors without books (using LEFT JOIN)
SELECT books.title, authors.first_name, authors.last_name
FROM books
LEFT JOIN authors ON books.author_id = authors.author_id;
