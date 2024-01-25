from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Blogs(Base):
    __tablename__ = "blogs01"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("blog_user.id"))

    creator = relationship("BlogUser", back_populates="blogs01")


class BlogUser(Base):
    __tablename__ = "blog_user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs01 = relationship("Blogs", back_populates="creator")
