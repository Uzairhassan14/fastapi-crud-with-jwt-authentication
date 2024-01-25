from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, models, oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.showBlog],
)
def all(
    db: Session = Depends(get_db),
    current_user: schemas.BlogUser = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create(
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.BlogUser = Depends(oauth2.get_current_user),
):
    return blog.create(request, db)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def destroy(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.BlogUser = Depends(oauth2.get_current_user),
):
    return blog.destroy(id, db)


@router.put(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
)
async def update_blog(
    id,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.BlogUser = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.showBlog,
)
def show(
    id,
    db: Session = Depends(get_db),
    current_user: schemas.BlogUser = Depends(oauth2.get_current_user),
):
    return blog.show(id, db)
