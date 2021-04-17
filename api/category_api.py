from typing import List

from fastapi import Depends, APIRouter, Body
from sqlalchemy.orm import Session

from app import crud
from app.schemas import CategoryList, CategoryCreate
from .base import get_db

router = APIRouter()


@router.get("/", response_model=List[CategoryList])
def list_categories(db: Session = Depends(get_db)):
    return crud.category_list(db)


@router.post("/create", response_model=CategoryCreate)
def create_category(name: str = Body(...), db: Session = Depends(get_db)):
    category = CategoryCreate(name=name)
    return crud.create_category(db, category)
