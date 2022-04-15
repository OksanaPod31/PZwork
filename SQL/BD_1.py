import sqlite3 as sq

with sq.connect('saper.db') as cor:
    cur = cor.cursor()
    cur.execute("DROP TABLE IF EXISTS users")

    cur.execute(""" CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, 
    sex INTEGER NOT NULL DEFAULT 1, old INTEGER, score INTEGER)""")

    cur.execute(" INSERT INTO users VALUES(1, 'Алексей', 1, 22, 1000 )")
    cur.execute(" INSERT INTO users VALUES(2, 'Миша', 1, 19, 800 )")
    cur.execute(" INSERT INTO users VALUES(3, 'Сергей', 1, 19, 900 )")
    cur.execute(" INSERT INTO users VALUES(4, 'Мария', 2, 18, 1500 )")
    cur.execute(" INSERT INTO users VALUES(5, 'Александр', 1, 20, 1100 )")

    cur.execute("SELECT name FROM users ")
    cur.execute("SELECT name FROM users WHERE sex = 2")
    cur.execute("SELECT name FROM users WHERE score < 2")
    cur.execute("SELECT name, score FROM users WHERE score = (SELECT MAX(score) FROM users)")
    cur.execute("SELECT name FROM users WHERE old BETWEEN 18 AND 20")

    cur.execute("UPDATE users SET old = 20 WHERE old = 19")
    cur.execute("UPDATE users SET score = score + 300 WHERE score < 1000")
    cur.execute("UPDATE users SET score = score + 100 WHERE old = 20")
    cur.execute("DELETE FROM users WHERE score < 1000")
