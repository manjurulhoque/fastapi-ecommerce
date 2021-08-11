from typing import List, ForwardRef

from pydantic import BaseModel, EmailStr, Field

UserPost = ForwardRef('Post')


class CustomHTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }


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


class BaseCategory(BaseModel):
    name: str = Field(example="e.g. Programming")


class CategoryCreate(BaseCategory):
    class Config:
        orm_mode = True


class CategoryList(BaseCategory):
    id: int

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    title: str = Field(example="Example title")
    quantity: int
    description: str
    category_id: int

    class Config:
        orm_mode = True


class ProductList(BaseModel):
    id: int
    title: str = Field(example="Example title")
    quantity: int
    description: str
    image: str
    owner: UserGet
    category: CategoryList

    class Config:
        orm_mode = True
