from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import Product, ProductCreate
from app.database.mock_db import products_db
from uuid import uuid4

router = APIRouter()

@router.get("/", response_model=list[Product])
def get_products():
    return products_db

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str):
    product = next((p for p in products_db if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    new_product = product.dict()
    new_product["id"] = str(uuid4())
    products_db.append(new_product)
    return new_product
