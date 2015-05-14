import sqlite3
import re
import hashlib
from Client import Client
from settings import *

conn = sqlite3.connect(DB)
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def hash_pass(password):
    return hashlib.sha1(password.encode()).hexdigest()


def change_pass(new_pass, logged_user):
    hashed_pass = hash_pass(new_pass)
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (hashed_pass, logged_user.get_id()))
    conn.commit()


def check_pass(username, password):
    long_en = len(password) >= PASS_MIN_LEN
    not_cont_usern = username not in password
    has_let_cap_let = re.search(r'[a-z]', password) and re.search(r'[A-Z]', password)
    has_digit = re.search(r'\d', password)
    if long_en and not_cont_usern and has_let_cap_let and has_digit:
        if not re.match(r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", password):
            return True
    return False


def register(username, password):
    hashed_pass = hash_pass(password)
    if check_pass(username, password):
        insert_sql = "INSERT INTO clients (username, password) values (?, ?)"
        cursor.execute(insert_sql, (username, hashed_pass))
        conn.commit()
        return succ_log_in
    else:
        return strong_pass_msg


def login(username, password):
    hashed_pass = hash_pass(password)
    select_query = "SELECT id , username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, hashed_pass))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
