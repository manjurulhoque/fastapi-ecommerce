from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app import crud
from app.schemas import CategoryList
from .base import get_db

router = APIRouter()


@router.get("/", response_model=List[CategoryList])
def list_categories(db: Session = Depends(get_db)):
    return crud.category_list(db)
