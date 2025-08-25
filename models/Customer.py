from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List
from models.base import AuditBase, register_audit_listeners
from models.User import UserModel

if TYPE_CHECKING:
    from Order import Order
    from Invoice import Invoice

class CustomerCreate(SQLModel):
    customer_name: str = Field(..., min_length=5, max_length=60, description="Customer name should be between 5-60 chars")
    customer_address: str = Field(..., min_length=15, max_length=200, description="Address should be between 15-200 chars")
    
class CustomerUpdate(SQLModel):
    customer_name: Optional[str] = Field(None, min_length=5, max_length=60, description="Name should be between 5-60 chars")
    customer_address: Optional[str] = Field(None, min_length=15, max_length=200, description="Address should be between 15-200 chars")


class Customer(AuditBase, table=True):
    __tablename__ =  "customers"
    customer_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.user_id", nullable=False)
    customer_name: str = Field(max_length=30)
    customer_address: str = Field(max_length=100)
    user: "UserModel" = Relationship(back_populates="customer")
    orders: List["Order"] = Relationship(back_populates="customer")
    # invoices: List["Invoice"] = Relationship(back_populates="customer")


register_audit_listeners(Customer)
