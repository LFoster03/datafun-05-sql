-- query_filter.sql

-- Get books published after 1950
SELECT title, publish_year FROM books
WHERE publish_year > 1950;

-- Get books written by a specific author (example: 'J.K. Rowling')
SELECT title FROM books
JOIN authors ON books.author_id = authors.author_id
WHERE authors.first_name = 'J.K.' AND authors.last_name = 'Rowling';
