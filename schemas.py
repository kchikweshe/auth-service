from datetime import datetime
from typing import Optional

from fastapi import Body
from pydantic import BaseModel


class Actor(BaseModel):
    actor_name: str


class ShowActor(Actor):
    id: int
    is_active:bool

    class Config():
        orm_mode = True


class Genre(BaseModel):
    genre_name: str


class ShowGenre(Genre):
    id: int

    class Config():
        orm_mode = True


class Director(BaseModel):
    director_name: str


class ShowDirector(Director):
    id: int

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class Movie(BaseModel):
    movie_name: str
    actor_id: int
    director_id: int
    genre_id: int
    rating: int
    release_date: Optional[datetime] = Body(None)


class ShowMovies(Movie):
    id:int
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
