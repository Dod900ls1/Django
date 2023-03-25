DROP TABLE IF EXISTS directors;
CREATE TABLE directors (
    directorID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

DROP TABLE IF EXISTS movies;
CREATE TABLE movies (
    movieID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    rating REAL,
    year INTEGER
);

DROP TABLE IF EXISTS genres;
CREATE TABLE genres (
    genreID INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT
);

DROP TABLE IF EXISTS movie_genres;
CREATE TABLE movie_genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movieID INTEGER,
    genreID INTEGER
);

DROP TABLE IF EXISTS director_movies ;
CREATE TABLE director_movies  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movieID INTEGER,
    directorID INTEGER
);

INSERT INTO directors (name) VALUES
    ('Frank Darabont'),
    ('Francis Ford Coppola'),
    ('Christopher Nolan'),
    ('Peter Jackson'),
    ('Quentin Tarantino');

INSERT INTO movies (title, directorID, rating, year) VALUES
    ('The Shawshank Redemption', 1, 9.3, 1994),
    ('The Godfather', 2, 9.2, 1972),
    ('The Dark Knight', 3, 9.0, 2008),
    ('The Lord of the Rings: The Fellowship of the Ring', 4, 8.8, 2001),
    ('Pulp Fiction', 5, 8.9, 1994);
    ('The Godfather: Part II', 2, 9.0, 1974),
    ('The Dark Knight Rises', 3, 8.4, 2012),
    ('The Lord of the Rings: The Two Towers', 4, 8.7, 2002),
    ('Inception', 3, 8.8, 2010),
    ('Goodfellas', 1, 8.7, 1990),
    ('The Matrix', NULL, 8.7, 1999);

INSERT INTO genres (genre) VALUES
    ('Drama'),
    ('Crime'),
    ('Action'),
    ('Adventure'),
    ('Thriller');

INSERT INTO movie_genres (movieID, genreID) VALUES
    (1, 1),
    (1, 5),
    (2, 1),
    (2, 2),
    (3, 3),
    (3, 5),
    (4, 3),
    (4, 4),
    (5, 1),
    (5, 2),
    (5, 5);
