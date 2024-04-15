from icecream import ic
import sqlite3
import time


conn = sqlite3.connect('example.db')  # Create an in-memory database
cursor = conn.cursor()

queries = {
    "INNER JOIN":"SELECT * FROM customers INNER JOIN orders ON customers.id = orders.customer_id",
    "LEFT JOIN":"SELECT * FROM customers LEFT JOIN orders ON customers.id = orders.customer_id",
    "RIGHT JOIN":"SELECT * FROM customers RIGHT JOIN orders ON customers.id = orders.customer_id",
    "FULL OUTER JOIN":"SELECT * FROM customers FULL OUTER JOIN orders ON customers.id = orders.customer_id"
}

# Measure Execution Time
for key, query in queries.items():
    start_time = time.time()
    cursor.execute(query)
    ic(f"Query: {key}\nExecution Time: {time.time() - start_time} seconds\n")