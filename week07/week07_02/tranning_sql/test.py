import sqlite3


conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

create_query = '''
    CREATE TABLE IF NOT EXISTS
    users(first_name text, second_name text, salary int)
'''
cursor.execute(create_query)

add_user_query = """
    INSERT INTO users VALUES('pepino' , 'mihaelov' , 222)
    """
select_query = """
    SELECT first_name, second_name FROM users
    """


# cursor.execute(add_user_query)
obj = cursor.execute(select_query)
for row in obj:
    print('first_name: ' + row[0])
    print('last name:' + row[1])
conn.commit()
conn.close()
print('conn close successfuly')
