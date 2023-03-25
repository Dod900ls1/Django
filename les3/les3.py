from sqlalchemy import create_engine, Integer, String, REAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship, Session

engine = create_engine("sqlite+pysqlite:///db1.sqlite3", echo=False)


class Base(DeclarativeBase):
    pass


class Director(Base):
    __tablename__ = 'directors'
    directorID = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(256), nullable=False, unique=False)
    movies = relationship('Movie', back_populates='director')

    def __repr__(self):
        return f'Director (name={self.name}), movie (movies={self.movies})'


class Movie(Base):
    __tablename__ = 'movies'
    movieID = mapped_column(Integer, primary_key=True)
    directorID = mapped_column(ForeignKey('directors.directorID'), nullable=False)
    title = mapped_column(String(256), nullable=False, unique=True)
    rating = mapped_column(REAL, nullable=True)
    year = mapped_column(Integer, nullable=False)
    director = relationship('Director', back_populates='movies')

    def __repr__(self):
        return f'Movie (title={self.title}), (rating={self.rating}), (year={self.year})'


if __name__ == "__main__":
    session = Session(engine)
    Base.metadata.create_all(bind=engine)

    directors = [
        Director(name='Christopher Nolan'),
        Director(name='Steven Spielberg'),
        Director(name='Martin Scorsese'),
        Director(name='Quentin Tarantino'),
        Director(name='Stanley Kubrick')
    ]
    session.add_all(directors)

    # Add 20 movies for those directors
    movies = [
        Movie(title='Inception', rating=8.8, year=2010, director=directors[0]),
        Movie(title='The Dark Knight', rating=9.0, year=2008, director=directors[0]),
        Movie(title='Interstellar', rating=8.6, year=2014, director=directors[0]),
        Movie(title='Dunkirk', rating=7.8, year=2017, director=directors[0]),
        Movie(title='Jurassic Park', rating=8.1, year=1993, director=directors[1]),
        Movie(title='Saving Private Ryan', rating=8.6, year=1998, director=directors[1]),
        Movie(title=r'Schindler\'s List', rating=8.9, year=1993, director=directors[1]),
        Movie(title='Indiana Jones and the Raiders of the Lost Ark', rating=8.4, year=1981, director=directors[1]),
        Movie(title='Goodfellas', rating=8.7, year=1990, director=directors[2]),
        Movie(title='The Departed', rating=8.5, year=2006, director=directors[2]),
        Movie(title='Taxi Driver', rating=8.3, year=1976, director=directors[2]),
        Movie(title='Gangs of New York', rating=7.5, year=2002, director=directors[2]),
        Movie(title='Pulp Fiction', rating=8.9, year=1994, director=directors[3]),
        Movie(title='Kill Bill: Vol. 1', rating=8.1, year=2003, director=directors[3]),
        Movie(title='Kill Bill: Vol. 2', rating=8.0, year=2004, director=directors[3]),
        Movie(title='Inglourious Basterds', rating=8.3, year=2009, director=directors[3]),
        Movie(title='Shutter Island', rating=8.2, year=2010, director=directors[3]),
        Movie(title='The Aviator', rating=7.5, year=2004, director=directors[3]),
        Movie(title='Gone Girl', rating=8.1, year=2014, director=directors[4]),
        Movie(title='The Curious Case of Benjamin Button', rating=7.8, year=2008, director=directors[4]),
        Movie(title='Memento', rating=8.4, year=2000, director=directors[0]),
        Movie(title='The Prestige', rating=8.5, year=2006, director=directors[0]),
        Movie(title='Reservoir Dogs', rating=8.3, year=1992, director=directors[1]),
        Movie(title='Once Upon a Time in America', rating=8.4, year=1984, director=directors[3])]

    session.add_all(movies)
    try:
        session.commit()
    except Exception as e:
        print(e)
