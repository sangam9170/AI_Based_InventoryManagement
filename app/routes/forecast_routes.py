from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.models.sales import Sale
from app.models.product import Product
from app.ml.forecast_model import DemandForecaster
import pandas as pd

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{product_id}")
def forecast_demand(product_id: int, db: Session = Depends(get_db)):
    sales = db.query(Sale).filter(Sale.product_id==product_id).all()
    if not sales:
        return {"message": "No sales data"}
    
    df = pd.DataFrame([{"week_number": i+1, "quantity_sold": s.quantity_sold} for i,s in enumerate(sales)])
    forecaster = DemandForecaster()
    forecaster.train(df)
    
    product = db.query(Product).filter(Product.id==product_id).first()
    predicted = forecaster.predict(len(df))
    
    return {
        "product_id": product_id,
        "predicted_demand": predicted,
        "current_stock": product.current_stock,
        "stock_gap": max(0, predicted - product.current_stock)
    }
