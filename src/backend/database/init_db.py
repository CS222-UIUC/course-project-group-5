"""Initialize database"""
import sqlite3

connection = sqlite3.connect("database.db")
with open("schema.sql", "r", encoding="utf-8") as f:
    connection.executescript(f.read())
cur = connection.cursor()
# test insertion
cur.execute(
    "INSERT INTO Users (username, password, email, phone, apt_id) VALUES (?, ?, ?, ?, ?)",
    ("XXXXX", "XXXXXXXXX", "XXXX@XXX.XXX", "(XXX)XXX-XXX", 1),
)
# test selection
res = connection.execute("SELECT * FROM Users").fetchall()
print(res)
connection.commit()
connection.close()
