from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    
class Customer(BaseModel):
    id: int
    name: str
    email: EmailStr
    
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None