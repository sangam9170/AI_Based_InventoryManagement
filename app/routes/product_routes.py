from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.crud import product_crud
from app.schemas.product_schema import ProductCreate, ProductOut

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ProductOut])
def list_products(db: Session = Depends(get_db)):
    return product_crud.get_products(db)

@router.post("/", response_model=ProductOut)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)
