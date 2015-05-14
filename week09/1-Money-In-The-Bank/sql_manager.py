import sqlite3
import re
import hashlib
import smtplib
import random
import string
from Client import Client
from settings import *

conn = sqlite3.connect(DB)
cursor = conn.cursor()


def create_clients_table():
    reset_query = "DROP TABLE IF EXISTS clients"
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT,
                fail_login_attemps REAL DEFAULT 0)'''
    add_test_user = "INSERT INTO clients (username, password, email) VALUES (?, ?, ?)"

    cursor.execute(reset_query)
    cursor.execute(create_query)
    cursor.execute(add_test_user, ('gogo', 'Password1!', 'rastamandito@mail.bg'))
    conn.commit()


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


def check_email(email):
    if re.match(EMAIL_REGEX, email):
        return False
    else:
        return True


def register(username, password, email):
    hashed_pass = hash_pass(password)
    if check_email(email):
        return email_fail_msg
    if check_pass(username, password):
        insert_sql = "INSERT INTO clients (username, password, email) VALUES (?, ?, ?)"
        cursor.execute(insert_sql, (username, hashed_pass, email))
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


def generate_random_string():
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_str


def update_reseted_pass(password, username):
    update_sql = "UPDATE clients SET password = ? WHERE username = ?"
    cursor.execute(update_sql, (password, username))
    conn.commit()


def send_reset_email(username, email):
    random_string = generate_random_string()
    new_pass = hash_pass(random_string)
    update_reseted_pass(new_pass, username)
    gmail_user = GMAIL_USER
    gmail_pass = GMAIL_PASS
    FROM = GMAIL_USER
    TO = email
    SUBJECT = 'reseting the password for the bank $$$ money comming!!!'
    TEXT = 'Your new pass is: {}'.format(random_string)
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.sendmail(FROM, TO, message)
        server.quit()
        print('successfully send the mail')
    except:
        print('failed to send the mail')

