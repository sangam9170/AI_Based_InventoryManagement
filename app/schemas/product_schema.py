from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str = None
    current_stock: int = 0
    reorder_level: int = 10

class ProductOut(ProductCreate):
    id: int
    class Config:
        orm_mode = True
