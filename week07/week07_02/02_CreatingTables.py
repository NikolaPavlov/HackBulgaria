import sqlite3
database_name = 'polyglot.db'
create_table_query = """
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                   phone TEXT, email TEXT unique, password TEXT)
"""

db_connection = sqlite3.connect(database_name)
cursor = db_connection.cursor()
cursor.execute(create_table_query)
