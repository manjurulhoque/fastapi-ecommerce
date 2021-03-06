import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(os.path.abspath(os.path.join(BASE_DIR, os.pardir)), ".env"))

from api import user_api, product_api, category_api

# models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users",
    }
]

app = FastAPI(
    title="E-commerce API",
    description="FastAPI based ***e-commerce***",
    version="0.1.0",
    redocs_url=None,
    docs_url="/",
    openapi_tags=tags_metadata,
    debug=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(user_api.router, tags=['users'])
app.include_router(product_api.router, prefix='/products', tags=['products'])
app.include_router(category_api.router, prefix='/categories', tags=['categories'])
