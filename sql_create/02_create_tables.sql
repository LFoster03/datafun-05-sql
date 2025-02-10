-- 02_create_tables.sql

-- Create the authors table
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birth_date DATE
);

-- Create the books table with a foreign key referencing authors
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    publish_year INTEGER NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
);
