import sqlite3
conn = sqlite3.connect('fypsuitagency.db')
c = conn.cursor()
c.execute("SELECT * FROM suppliers")
conn.commit()
print(c.fetchall())

