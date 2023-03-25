import sqlite3

DB = 'create.sqlite3'

query = """
SELECT *
FROM directors
WHERE avgRating >= 6
"""

query1 = """
SELECT *
FROM favMovies LEFT JOIN directors
ON directors.name = favMovies.director
"""

with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    print('Query1:')
    for item in cursor.execute(query):
        print(item)
    print('Query2:')
    for item in cursor.execute(query1):
        print(item)
