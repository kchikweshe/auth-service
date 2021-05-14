from fastapi import APIRouter, Depends

import models
import oauth2
from database import get_db
import schemas
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['genre'], prefix='/genre')


@router.get('/', response_model=List[schemas.ShowGenre])
def get_genre(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    genre = db.query(models.Genre).all()
    return genre


@router.post('/')
def post_genre(request: schemas.Genre, db: Session = Depends(get_db),
               current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_genre = models.Genre(genre_name=request.genre_name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre



@router.put('/{id}')
def edit_genre(id, request: schemas.Genre, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == id)
    genre.update(request.dict())
    db.commit()
    return "updated"


@router.delete('/{id}')
def delete_genre(id, db: Session = Depends(get_db)):
    genre = db.query(models.Genre).filter(models.Genre.id == id)
    genre.delete(synchronize_session=False)
    db.commit()
    return {'deleted'}
