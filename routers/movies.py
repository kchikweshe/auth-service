from fastapi import APIRouter, Depends

import models
import oauth2
from database import get_db
import schemas
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['movie'], prefix='/movie')


@router.get('/', response_model=List[schemas.ShowMovies])
def get_movie(db: Session = Depends(get_db)):
    movie = db.query(models.Movies).all()
    return movie


@router.post('/')
def post_movie(request: schemas.Movie, db: Session = Depends(get_db)):
    new_movie = models.Movies(movie_name=request.movie_name,actor_id=request.actor_id,director_id=request.director_id,genre_id=request.genre_id,rating=request.rating,release_date=request.release_date)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie



# @router.put('/{id}')
# def edit_genre(id, request: schemas.Genre, db: Session = Depends(get_db)):
#     genre = db.query(models.Genre).filter(models.Genre.id == id)
#     genre.update(request.dict())
#     db.commit()
#     return "updated"

#
# @router.delete('/{id}')
# def delete_genre(id, db: Session = Depends(get_db)):
#     genre = db.query(models.Genre).filter(models.Genre.id == id)
#     genre.delete(synchronize_session=False)
#     db.commit()
#     return {'deleted'}
