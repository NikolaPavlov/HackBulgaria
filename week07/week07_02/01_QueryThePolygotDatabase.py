import sqlite3

query_base = 'polyglot.db'
query = 'SELECT * FROM languages'

conn = sqlite3.connect(query_base)
cursor = conn.cursor()
result = cursor.execute(query)

for row in result:
    print(row)
