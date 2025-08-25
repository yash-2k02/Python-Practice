from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    
class Product(BaseModel):
    id: int
    name: str
    price: float
    
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None