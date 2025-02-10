import sqlite3
import os
import matplotlib.pyplot as plt

# Path to the database file
db_file = 'library.queries.db'

# Function to run SQL queries and fetch the results
def run_sql_query(query):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Function to execute aggregation query and display results
def aggregation_queries():
    print("Running Aggregation Queries...")
    
    # COUNT, AVG, SUM queries
    count_query = 'SELECT COUNT(*) AS total_books FROM books'
    avg_query = 'SELECT AVG(publish_year) AS avg_publish_year FROM books'
    sum_query = 'SELECT SUM(publish_year) AS sum_publish_year FROM books'
    
    total_books = run_sql_query(count_query)[0][0]
    avg_publish_year = run_sql_query(avg_query)[0][0]
    sum_publish_year = run_sql_query(sum_query)[0][0]
    
    print(f"Total Books: {total_books}")
    print(f"Average Publish Year: {avg_publish_year}")
    print(f"Sum of Publish Years: {sum_publish_year}")
    
# Function to execute filter query and display results
def filter_queries():
    print("\nRunning Filter Queries...")
    
    # Books published after 1950
    filter_query = 'SELECT title, publish_year FROM books WHERE publish_year > 1950'
    books_after_1950 = run_sql_query(filter_query)
    
    print("Books Published After 1950:")
    for book in books_after_1950:
        print(f"{book[0]} ({book[1]})")

# Function to execute sorting query and display results
def sorting_queries():
    print("\nRunning Sorting Queries...")
    
    # Books sorted by publish year
    sort_query = 'SELECT title, publish_year FROM books ORDER BY publish_year ASC'
    sorted_books = run_sql_query(sort_query)
    
    print("Books Sorted by Publish Year (Ascending):")
    for book in sorted_books:
        print(f"{book[0]} ({book[1]})")

# Function to execute GROUP BY query and display results
def group_by_queries():
    print("\nRunning Group By Queries...")
    
    # Number of books per author
    group_by_query = '''SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS num_books
                        FROM authors JOIN books ON authors.author_id = books.author_id
                        GROUP BY authors.author_id'''
    books_per_author = run_sql_query(group_by_query)
    
    print("Number of Books Per Author:")
    for author in books_per_author:
        print(f"{author[0]} {author[1]}: {author[2]} books")

# Function to execute JOIN query and display results
def join_queries():
    print("\nRunning Join Queries...")
    
    # Get books with their authors
    join_query = '''SELECT books.title, authors.first_name, authors.last_name
                    FROM books INNER JOIN authors ON books.author_id = authors.author_id'''
    books_with_authors = run_sql_query(join_query)
    
    print("Books with Authors:")
    for book in books_with_authors:
        print(f"{book[0]} by {book[1]} {book[2]}")

# Function to visualize data (e.g., number of books per author)
def visualize_books_per_author():
    group_by_query = '''SELECT authors.first_name, authors.last_name, COUNT(books.book_id) AS num_books
                        FROM authors JOIN books ON authors.author_id = books.author_id
                        GROUP BY authors.author_id'''
    books_per_author = run_sql_query(group_by_query)
    
    authors = [f"{author[0]} {author[1]}" for author in books_per_author]
    num_books = [author[2] for author in books_per_author]

    # Bar chart
    plt.bar(authors, num_books)
    plt.xlabel('Author')
    plt.ylabel('Number of Books')
    plt.title('Number of Books Per Author')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Main function to execute queries and visualize results
def main():
    aggregation_queries()
    filter_queries()
    sorting_queries()
    group_by_queries()
    join_queries()
    visualize_books_per_author()

if __name__ == '__main__':
    main()
