from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import user
from ..hashing import Hash


def craete_user(request: schemas.BlogUser, db: Session):
    new_user = models.BlogUser(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.BlogUser).filter(models.BlogUser.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} is not found",
        )
    return user
