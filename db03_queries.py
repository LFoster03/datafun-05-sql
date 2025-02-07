import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Define the database file (SQLite)
db_file = "mydatabase.sqlite3"

def run_sql_query(query):
    """Function to execute SQL query and return results as a pandas DataFrame."""
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def main():
    """Main function to execute SQL queries and summarize results."""
    
    # 1. Aggregation Query
    print("Running Aggregation Query (COUNT, AVG, SUM)...")
    with open('sql_queries/query_aggregation.sql', 'r') as file:
        aggregation_query = file.read()
    aggregation_result = run_sql_query(aggregation_query)
    print("Aggregation Result:\n", aggregation_result)

    # 2. Filter Query
    print("\nRunning Filter Query (WHERE)...")
    with open('sql_queries/query_filter.sql', 'r') as file:
        filter_query = file.read()
    filter_result = run_sql_query(filter_query)
    print("Filter Result:\n", filter_result)

    # 3. Sorting Query
    print("\nRunning Sorting Query (ORDER BY)...")
    with open('sql_queries/query_sorting.sql', 'r') as file:
        sorting_query = file.read()
    sorting_result = run_sql_query(sorting_query)
    print("Sorting Result:\n", sorting_result)

    # 4. Group By Query
    print("\nRunning Group By Query...")
    with open('sql_queries/query_group_by.sql', 'r') as file:
        group_by_query = file.read()
    group_by_result = run_sql_query(group_by_query)
    print("Group By Result:\n", group_by_result)

    # 5. Join Query
    print("\nRunning Join Query (INNER JOIN)...")
    with open('sql_queries/query_join.sql', 'r') as file:
        join_query = file.read()
    join_result = run_sql_query(join_query)
    print("Join Result:\n", join_result)

    # Example: Visualize Total Sales by Customer
    if not group_by_result.empty:
        print("\nVisualizing Total Sales by Customer...")
        group_by_result.plot(kind='bar', x='CustomerID', y='TotalSpent', title="Total Sales by Customer")
        plt.xlabel('CustomerID')
        plt.ylabel('Total Sales')
        plt.show()

if __name__ == "__main__":
    main()
