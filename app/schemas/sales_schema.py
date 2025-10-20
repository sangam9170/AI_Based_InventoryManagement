from pydantic import BaseModel
from datetime import date

class SaleCreate(BaseModel):
    product_id: int
    quantity_sold: int

class SaleOut(SaleCreate):
    id: int
    sale_date: date
    class Config:
        orm_mode = True
