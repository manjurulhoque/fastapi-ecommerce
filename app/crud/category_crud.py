from sqlalchemy.orm import Session, joinedload

from app import schemas, models


def category_list(db: Session):
    return db.query(models.Category).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    new_category = models.Category(name=category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
