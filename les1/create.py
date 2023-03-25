import sqlite3

DB = 'create.sqlite3'

script1 = """
DROP TABLE if EXISTS favMovies;

CREATE TABLE favMovies (
    title TEXT,
    year INTEGER,
    rating REAL,
    director TEXT
);
"""

query1 = """
INSERT INTO favMovies
VALUES (?, ?, ?, ?);
"""

data1 = [
    ('The Last of Us', 2023, 9.1, 'Neil Druckmann'),
    ('The Whale', 2022, 7.8, 'Darren Aronofsky'),
    ('Poker Face', 2023, 8.0, 'Damien Chazelle '),
    ('Babylon', 2022, 7.3, 'Natasha Lyonne'),
    ('All Quiet on the Western Front', 2022, 7.8, 'Edward Berger'),
    ('Avatar: The Way of Water', 2022, 7.8, 'James Cameron '),
    ('Glass Onion: A Knives Out Mystery', 2022, 7.2, 'Rian Johnson'),
]

script2 = """
DROP TABLE if EXISTS directors;

CREATE TABLE directors (
    name TEXT,
    yearsOld INTEGER,
    filmsDirected TEXT,
    avgRating REAL
);
"""

query2 = """
INSERT INTO directors
VALUES (?, ?, ?, ?)
"""

data2 = [
    ('Neil Druckmann',
     44,
     'Pedro Pascal and Bella Ramsey in The Last of Us (2023). The Last of Us · Uncharted: Legacy of Thieves Collection (2022)',
     7.5),
    ('Darren Aronofsky', 54, 'Pi, Requiem for a Dream, The Fountain', 5.4),
    ('Yehor Boiar', 16, 'Very beautiful star, Triganomery', 10.0),
]



with sqlite3.connect(DB) as connection:
    cursor = connection.cursor()
    cursor.executescript(script1)
    cursor.executescript(script2)
    for row in data1:
        cursor.execute(query1, row)
    for row in data2:
        cursor.execute(query2, row)

    connection.commit()
