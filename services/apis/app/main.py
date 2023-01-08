from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models, crud
# from . import models, schemas, crud

from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS Acess

origins = [
    "http://0.0.0.0",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables

models.Base.metadata.create_all(bind=engine)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def ping():
    return {"ping": "pong"}


@app.post("/products/", response_model=models.PydanticProducts)
def create_product(product: models.PydanticProducts, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@app.get("/products/", response_model=List[models.PydanticProducts])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return [models.PydanticProducts.from_orm(product) for product in products]


@app.get("/products/{sku}", response_model=models.PydanticProducts)
def read_product(sku: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, sku=sku)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return models.PydanticProducts.from_orm(db_product)


@app.patch("/products/{sku}", response_model=models.PydanticProducts)
def update_products(sku: int, productUpdate: models.ProductUpdate,  db: Session = Depends(get_db)):
    db_product = crud.get_product(db, sku=sku)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return crud.update_product(db, db_product, productUpdate)


@app.delete("/products/{sku}")
def update_products(sku: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, sku=sku)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return crud.delete_product(db, db_product)
