from datetime import datetime

from sqlalchemy.orm import relationship

import database
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

Base = database.Base


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    movie_name = Column(String(20))
    actor_id = Column(Integer, ForeignKey("actors.id"))
    director_id = Column(Integer, ForeignKey("directors.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))
    rating = Column(Integer)
    release_date = Column(String(60))
    is_active = Column(Boolean, default=True)
    actor = relationship("Actor")
    director = relationship("Director")
    director = relationship("Genre")


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    actor_name = Column(String(20))
    is_active = Column(Boolean, default=True)


class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    genre_name = Column(String(20))
    is_active = Column(Boolean, default=True)


class Director(Base):
    __tablename__ = "directors"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    director_name = Column(String(20))
    is_active = Column(Boolean, default=True)



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String(20))
    password = Column(String(160))
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
