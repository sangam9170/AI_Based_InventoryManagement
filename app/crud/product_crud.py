from sqlalchemy.orm import Session
from app.models.product import Product

def get_products(db: Session):
    return db.query(Product).all()

def create_product(db: Session, product):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
