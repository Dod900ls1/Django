import sqlite3

DB = "create.sqlite3"

with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    script = open('create1.sql').read()
    cursor.executescript(script)