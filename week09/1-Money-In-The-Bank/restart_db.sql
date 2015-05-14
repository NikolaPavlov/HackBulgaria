# should load manualy, like a bloody noob
# omg i'm so lame

DROP TABLE IF EXISTS clients;

CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    balance REAL DEFAULT 0,
    message TEXT,
    email TEXT,
    fail_login_attemps REAL DEFAULT 0);


