import sqlite3

db_path = "bluestock_mf.db"
schema_path = "sql/schema.sql"

conn = sqlite3.connect(db_path)

with open(schema_path, "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Database created successfully")