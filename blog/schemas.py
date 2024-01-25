from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class BlogUser(BaseModel):
    name: str
    email: str
    password: str


class ShowBlogUser(BaseModel):
    name: str
    email: str
    blogs01: List[Blog] = []

    class Config:
        orm_mode = True


class showBlog(BaseModel):
    title: str
    body: str
    creator: ShowBlogUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
