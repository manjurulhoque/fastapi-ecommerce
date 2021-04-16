from sqlalchemy.orm import Session, joinedload

from app import schemas, models


def category_list(db: Session):
    return db.query(models.Category).all()
