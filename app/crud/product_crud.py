from sqlalchemy.orm import Session, joinedload

from app import schemas, models


def list_products(db: Session):
    return db.query(models.Product).options(joinedload(models.Product.owner)).all()


def create_product(db: Session, product: schemas.ProductCreate, image: str, owner_id: int):
    new_product = models.Product(
        title=product.title,
        description=product.description,
        quantity=product.quantity,
        image=image,
        owner_id=owner_id,
        category_id=product.category_id,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
