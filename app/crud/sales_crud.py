from sqlalchemy.orm import Session
from app.models.sales import Sale
from app.models.product import Product

def create_sale(db: Session, sale):
    db_sale = Sale(**sale.dict())
    db.add(db_sale)
    
    # Update product stock
    product = db.query(Product).filter(Product.id==sale.product_id).first()
    if product:
        product.current_stock -= sale.quantity_sold
    db.commit()
    db.refresh(db_sale)
    return db_sale
