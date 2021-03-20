from sqlalchemy.orm import Session

from app import schemas, models


def create_product(db: Session, product: schemas.ProductCreate, image: str, owner_id: int):
    new_product = models.Product(
        title=product.title,
        description=product.description,
        quantity=product.quantity,
        image=image,
        owner_id=owner_id,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
