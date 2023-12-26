from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    owner_id : int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(PostBase):
    Post: Post
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)