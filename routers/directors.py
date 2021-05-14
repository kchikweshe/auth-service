from fastapi import APIRouter, Depends

import models
import oauth2
from database import get_db
import schemas
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(tags=['director'], prefix='/director')


@router.get('/', response_model=List[schemas.ShowDirector])
def get_director(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    director = db.query(models.Director).all()
    return director


@router.post('/')
def post_director(request: schemas.Director, db: Session = Depends(get_db),
               current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_director = models.Director(director_name=request.director_name)
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director


@router.put('/{id}')
def edit_director(id, request: schemas.Director, db: Session = Depends(get_db)):
    director = db.query(models.Director).filter(models.Director.id == id)
    director.update(request.dict())
    db.commit()
    return "updated"


@router.delete('/{id}')
def delete_director(id, db: Session = Depends(get_db)):
    director = db.query(models.Director).filter(models.Director.id == id)
    director.delete(synchronize_session=False)
    db.commit()
    return {'deleted'}
