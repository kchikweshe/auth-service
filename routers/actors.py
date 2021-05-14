from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import models
import oauth2
from database import get_db

import schemas

router = APIRouter(tags=['actors'], prefix="/actors")


@router.get('/', response_model=List[schemas.ShowActor])
def getallactors(db: Session = Depends(get_db)):
    actors = db.query(models.Actor).all()
    return actors


@router.get('/{id}', response_model=schemas.ShowActor)
def getactorbyid(id: int, db: Session = Depends(get_db)):
    actors = db.query(models.Actor).filter(models.Actor.id == id).first()
    return actors


@router.post('/')
def post_actors(request: schemas.Actor, db: Session = Depends(get_db)):
    new_actor = models.Actor(actor_name=request.actor_name)
    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    return new_actor


@router.put('/{id}')
def edit_actor(id, request: schemas.Actor, db: Session = Depends(get_db)):
    actor = db.query(models.Actor).filter(models.Actor.id == id)
    actor.update(request.dict())
    print(request)
    db.commit()
    return "updated"


@router.delete('/{id}')
def delete_actor(id, db: Session = Depends(get_db)):
    # item:schemas.ShowActor = db.query(models.Actor).filter(models.Actor.id == id).first()
    # print(item.is_active)
    # if item.is_active:
    #     item.is_active = False
    # else:
    #     item.is_active = True
    # actor = db.query(models.Actor).filter(models.Actor.id == id)
    # actor.update(item)
    # db.commit()
    actor = db.query(models.Actor).filter(models.Actor.id == id)
    actor.delete(synchronize_session=False)
    db.commit()
    return {'deleted'}
