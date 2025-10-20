from sqlalchemy import Column, Integer, ForeignKey, Date
from app.config import Base
from sqlalchemy.orm import relationship
import datetime

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity_sold = Column(Integer)
    sale_date = Column(Date, default=datetime.date.today)
    
    product = relationship("Product")
