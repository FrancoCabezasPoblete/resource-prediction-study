from icecream import ic
from faker import Faker
import sqlite3
import random
import sys

if len(sys.argv) < 4:
    ic("Usage: python main.py <n_customers:int> <n_orders:int> <path_db:string>")
    sys.exit(1)

n_customers = int(float(sys.argv[1]))
n_orders = int(float(sys.argv[2]))
fake = Faker()
# Connect to SQLite database
conn = sqlite3.connect(sys.argv[3])
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    email TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATE,
    amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers (id)
)''')

# Insert fake data into customers
customer_query = "INSERT INTO customers (name, address, email) VALUES (?, ?, ?)"

for _ in range(n_customers):
    cursor.execute(
        customer_query, 
        (fake.name(), fake.address(), fake.email())
    )

# Insert fake data into orders
order_query = "INSERT INTO orders (customer_id, order_date, amount) VALUES (?, ?, ?)"

for _ in range(n_orders):
    # Randomly assign orders to customers
    customer_id = random.randint(1, n_customers)
    cursor.execute(
        order_query, 
        (customer_id, fake.date_between(start_date='-1y', end_date='today'), round(random.uniform(20.0, 500.0), 2))
    )

# Commit and close
conn.commit()
conn.close()