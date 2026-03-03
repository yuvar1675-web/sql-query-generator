import sqlite3

def create_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        purchase_amount INTEGER
    )
    """)

    # Sample data insert
    cursor.execute("INSERT INTO customers (name, city, purchase_amount) VALUES ('Arun', 'Chennai', 6000)")
    cursor.execute("INSERT INTO customers (name, city, purchase_amount) VALUES ('Priya', 'Madurai', 3000)")
    cursor.execute("INSERT INTO customers (name, city, purchase_amount) VALUES ('Kumar', 'Chennai', 8000)")

    conn.commit()
    conn.close()

def run_query(query):
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results