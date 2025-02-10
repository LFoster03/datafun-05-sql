-- update_records.sql

-- Update the publish year for a specific book
UPDATE books
SET publish_year = 2023
WHERE title = '1984';
