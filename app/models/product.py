from sqlalchemy import Column, Integer, String
from app.config import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=True)
    current_stock = Column(Integer, default=0)
    reorder_level = Column(Integer, default=10)
