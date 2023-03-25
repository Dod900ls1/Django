from les3 import engine, Base, Movie, Director, Session

if __name__ == '__main__':
    session = Session(engine)
    # Films directed by Tarantino
    Tarantino = session.query(Movie).join(Director).filter(Director.name == 'Quentin Tarantino').all()
    for i in Tarantino:
        print(i)
    print(f'{["-" for i in range(20)]}')
    # Films with rating bigger than 8.5
    good_movies = session.query(Movie).filter(Movie.rating > 8.5).all()
    for i in good_movies:
        print(i)
    print(f'{["-" for i in range(20)]}')
    # Director of film "Inception"
    Inception = session.query(Director).join(Movie).filter(Movie.title == 'Inception').one()
    print(Inception)