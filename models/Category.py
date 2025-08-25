from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, List, Optional
from models.base import AuditBase, register_audit_listeners

if TYPE_CHECKING:
    from Product import Product

class CategoryCreate(SQLModel):
    category_name: str = Field(..., min_length=5, max_length=60, description="Category name should be between 5-60 chars")
    category_description: Optional[str] = Field(None, min_length=15, max_length=200, description="Description should be between 15-200 chars")


class CategoryUpdate(SQLModel):
    category_name: Optional[str] = Field(..., min_length=5, max_length=60, description="Category name should be between 5-60 chars")
    category_description: Optional[str] = Field(None, min_length=15, max_length=200, description="Description should be between 15-200 chars")


class Category(AuditBase, table=True):
    __tablename__ = "categories"
    category_id: Optional[int] = Field(default=None, primary_key=True)
    category_name: str = Field(max_length=50, unique=True)
    category_description: Optional[str]
    products: List["Product"] = Relationship(back_populates="category")
    

register_audit_listeners(Category)