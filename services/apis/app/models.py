from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from typing import Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pydantic import BaseModel

from .database import Base


class Products(Base):
    __tablename__ = "products"

    sku = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    quantity = Column(Integer)
    quantityFormat = Column(Integer)
    ingredientId = Column(Integer)
    brand = Column(String(75))
    category = Column(String(75))
    categoryUrl = Column(String(75))

    # instances      = relationship("Listing", back_populates="id")


class Listing(Base):
    __tablename__ = "listing"

    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String(75))
    price = Column(Float, index=True)
    lastUpdate = Column(Integer)
    skuReference = Column(Integer, ForeignKey("products.sku"))

    # linkedProduct = relationship("Products", back_populates="sku")


PydanticProducts = sqlalchemy_to_pydantic(Products)
PydanticListing = sqlalchemy_to_pydantic(Listing)

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None
    quantityFormat: Optional[int] = None
    ingredientId: Optional[int] = None
    brand: Optional[str] = None
    category: Optional[str] = None
    categoryUrl: Optional[str] = None
