from typing import List, ForwardRef

from pydantic import BaseModel, EmailStr, Field

UserPost = ForwardRef('Post')


class UserBase(BaseModel):
    email: EmailStr = Field(None, example="user@example.com", title="User email")


class User(UserBase):
    name: str
    password: str

    class Config:
        orm_mode = True


class UserNameEmail(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserGet(UserBase):
    name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    name: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class ProductCreate(BaseModel):
    title: str
    quantity: int
    description: str

    class Config:
        orm_mode = True
