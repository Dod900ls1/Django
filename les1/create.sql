DROP TABLE if EXISTS favMovies, directors;

CREATE TABLE favMovies (
    title TEXT,
    year INTEGER,
    rating REAL,
    director TEXT
);

CREATE TABLE directors (
    name TEXT,
    yearsOld INTEGER,
    filmsDirected TEXT,
    avgRating REAL
);


INSERT INTO favMovies
VALUES('The Last of Us', 2023, 9.1, 'Neil Druckmann'),
    ('The Whale', 2022, 7.8, 'Darren Aronofsky'),
    ('Poker Face', 2023, 8.0, 'Damien Chazelle '),
    ('Babylon', 2022, 7.3, 'Natasha Lyonne'),
    ('All Quiet on the Western Front', 2022, 7.8, 'Edward Berger'),
    ('Avatar: The Way of Water', 2022, 7.8, 'James Cameron '),
    ('Glass Onion: A Knives Out Mystery', 2022, 7.2, 'Rian Johnson');

INSERT INTO directors
VALUES ('Neil Druckmann', 'Pedro Pascal and Bella Ramsey in The Last of Us (2023). The Last of Us · Uncharted: Legacy of Thieves Collection (2022)' ,44, 7.5)
    ('Darren Aronofsky', 'Pi, Requiem for a Dream, The Fountain', 54, 5.4)
