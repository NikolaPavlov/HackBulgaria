import sqlite3
import re
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    # update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, logged_user.get_id())
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    # update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def check_pass(username, password):
    long_en = len(password) >= 8
    not_cont_usern = username not in password
    has_let_cap_let = re.search(r'[a-z]', password) and re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    if long_en and not_cont_usern and has_let_cap_let and has_digit:
        if not re.match(r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", password):
            return True
    return False


def register(username, password):
    if check_pass(username, password):
        # insert_sql = "insert into clients (username, password) values ('%s', '%s')" % (username, password)
        insert_sql = "INSERT INTO clients (username, password) values (?, ?)"
        cursor.execute(insert_sql, (username, password))
        conn.commit()
        return 'Succesffuly registered!'
    else:
        return '''
            Please choose strong pass or JohnTheRiper will come for you!
            aka. More than 8 symbols, capital letters, special symbol, digit!
            '''


def login(username, password):
    # select_query = "SELECT id, username, balance, message FROM clients WHERE username = '%s' AND password = '%s' LIMIT 1" % (username, password)
    select_query = "SELECT id , username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
