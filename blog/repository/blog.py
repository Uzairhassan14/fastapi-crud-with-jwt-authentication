from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blogs).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blogs(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id, db: Session):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id: int, request: schemas.Blog, db: Session):
    db_blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    if db_blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found",
        )
    for key, value in request.dict().items():
        setattr(db_blog, key, value)
    db.commit()
    return "updated"


def show(id: int, db: Session):
    blog = db.query(models.Blogs).filter(models.Blogs.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} is not found",
        )
    return blog
