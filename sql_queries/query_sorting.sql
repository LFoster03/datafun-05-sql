-- query_sorting.sql

-- Get books sorted by publish year (ascending)
SELECT title, publish_year FROM books
ORDER BY publish_year ASC;

-- Get books sorted by title (descending)
SELECT title FROM books
ORDER BY title DESC;
