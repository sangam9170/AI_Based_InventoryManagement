from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.crud import sales_crud
from app.schemas.sales_schema import SaleCreate, SaleOut

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SaleOut)
def add_sale(sale: SaleCreate, db: Session = Depends(get_db)):
    return sales_crud.create_sale(db, sale)
