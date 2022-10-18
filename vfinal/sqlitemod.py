import sqlite3
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

cursor.execute("Drop TABLE betoch_rent")

print("rent detail table")


conn.commit()
conn.close()