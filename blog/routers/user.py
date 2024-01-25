from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..hashing import Hash
from ..repository import user

router = APIRouter(prefix="/user", tags=["Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowBlogUser,
)
def create_user(request: schemas.BlogUser, db: Session = Depends(get_db)):
    return user.craete_user(request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ShowBlogUser,
)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
