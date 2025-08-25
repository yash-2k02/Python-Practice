from decimal import Decimal
from sqlalchemy import Column, Numeric
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING, List, Optional
from models.base import AuditBase, register_audit_listeners

if TYPE_CHECKING:
    from Category import Category
    from OrderItem import OrderItem

class ProductCreate(SQLModel):
    product_name: str = Field(..., min_length=8, max_length=80, description="Product name should be between 8-80 chars")
    product_description: str = Field(..., min_length=10, max_length=255, description="Product description should be between 10-255 chars")
    product_price: Decimal = Field(...,gt=0, description="Price must be greater than 0")
    category_id: int = Field(..., ge=0, description="ID cannot be negative")
    
class ProductUpdate(SQLModel):
    product_name: Optional[str] = Field(None, min_length=8, max_length=80, description="Product name should be between 8-80 chars")
    product_description: Optional[str] = Field(None, min_length=10, max_length=255, description="Product description should be between 10-255 chars")
    product_price: Optional[Decimal] = Field(None,gt=0, description="Price must be greater than 0")
    category_id: Optional[int] = Field(None, ge=1, description="ID cannot be negative")


class Product(AuditBase, table=True):
    __tablename__ = "products"
    product_id: Optional[int] = Field(default=None, primary_key=True)
    product_name: str = Field(unique=True)
    product_description: Optional[str]
    product_price: Decimal  = Field(
        sa_column=Column(Numeric(10, 2))
    )
    category_id: int = Field(foreign_key="categories.category_id")
    category: "Category" = Relationship(back_populates="products")
    order_items: List["OrderItem"] = Relationship(back_populates="product")
   
 
register_audit_listeners(Product)