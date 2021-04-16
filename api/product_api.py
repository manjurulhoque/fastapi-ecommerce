import os
from datetime import timedelta
from typing import List
import shutil

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Body
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from app import schemas, crud, models
from app.schemas import ProductCreate, ProductList, CustomHTTPError
from .base import get_db
from .user_api import get_current_user

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

media_path = os.path.join(os.path.abspath(os.path.join(BASE_DIR, os.pardir)), "media/")
router = APIRouter()


# @router.get("/", responses={
#     200: {"model": List[ProductList]},
#     409: {
#         "model": CustomHTTPError,
#         "description": "Custom error",
#     },
# })
@router.get("/", response_model=List[ProductList])
def list_products(db: Session = Depends(get_db)):
    return crud.list_products(db)


@router.post("/create/", responses={
    200: {"model": ProductCreate},
    403: {
        "model": CustomHTTPError,
        "description": "Custom error",
    },
})
def create_product(file: UploadFile = File(...), title: str = Body(...), description: str = Body(...), quantity: int = Body(..., gt=0), db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    filename = media_path + file.filename
    if "image/" not in file.content_type:
        raise HTTPException(403, detail='Only image is acceptable')

    with open(filename, "wb") as image:
        shutil.copyfileobj(file.file, image)

    product = schemas.ProductCreate(title=title, description=description, quantity=quantity)
    return crud.create_product(db=db, product=product, image=filename, owner_id=current_user.id)
