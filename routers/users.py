import models
import oauth2
import schemas
from hashing import Hash
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, APIRouter,Depends
from database import get_db
router = APIRouter(tags=['users'], prefix="/user")


@router.post('/', response_model=schemas.ShowUser)
def createuser(request: schemas.User, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/{id}', response_model=schemas.ShowUser)
def getUser(id, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} doesnt exist")
    return users
