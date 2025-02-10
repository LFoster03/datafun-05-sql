-- 03_insert_records.sql

-- Insert authors
INSERT INTO authors (first_name, last_name, birth_date) VALUES
('George', 'Orwell', '1903-06-25'),
('J.K.', 'Rowling', '1965-07-31'),
('J.R.R.', 'Tolkien', '1892-01-03'),
('Agatha', 'Christie', '1890-09-15'),
('Mark', 'Twain', '1835-11-30'),
('F. Scott', 'Fitzgerald', '1896-09-24'),
('Jane', 'Austen', '1775-12-16'),
('Charles', 'Dickens', '1812-02-07'),
('Harper', 'Lee', '1926-04-28'),
('Herman', 'Melville', '1819-08-01');

-- Insert books
INSERT INTO books (title, publish_year, author_id) VALUES
('1984', 1949, 1),
('Animal Farm', 1945, 1),
('Harry Potter and the Sorcerer\'s Stone', 1997, 2),
('Harry Potter and the Chamber of Secrets', 1998, 2),
('The Hobbit', 1937, 3),
('The Lord of the Rings', 1954, 3),
('Murder on the Orient Express', 1934, 4),
('The Murder of Roger Ackroyd', 1926, 4),
('The Adventures of Tom Sawyer', 1876, 5),
('The Great Gatsby', 1925, 6);
