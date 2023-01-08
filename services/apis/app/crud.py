from typing import Union
from sqlalchemy.orm import Session

from . import models


def create_product(db: Session, product: models.PydanticProducts):
    db_product = models.Products(
        sku=product.sku,
        name=product.name,
        quantity=product.quantity,
        quantityFormat=product.quantityFormat,
        ingredientId=product.ingredientId,
        brand=product.brand,
        category=product.category,
        categoryUrl=product.categoryUrl,
    )
    db.add(db_product)
    db.commit()

    return product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Products).offset(skip).limit(limit).all()


def get_product(db: Session, sku: int) -> Union[models.Products, None]:
    return db.query(models.Products).filter(models.Products.sku == sku).first()

def update_product(db: Session, product: models.Products, productUpdate: models.ProductUpdate):
    updateDict = productUpdate.dict(exclude_none=True)
    for key, value in updateDict.items():
        product.__setattr__(key, value)

    db.add(product)
    db.commit()

    return models.PydanticProducts.from_orm(product)

def delete_product(db: Session, product: models.Products) -> dict:
    db.delete(product)
    db.commit()
    return {"ok": True}
