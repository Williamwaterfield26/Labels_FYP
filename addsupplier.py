import sqlite3
conn = sqlite3.connect('fypsuitagency.db')
c = conn.cursor()
c.execute("INSERT INTO suppliers(suppliername) VALUES ('Boris')")
conn.commit()