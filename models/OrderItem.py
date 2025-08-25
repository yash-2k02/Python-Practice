from decimal import Decimal
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Column, Numeric
from sqlmodel import Field, Relationship, SQLModel
from models.base import AuditBase, register_audit_listeners

if TYPE_CHECKING:
    from Product import Product
    from Order import Order

class OrderItemCreate(SQLModel):
    product_id: int = Field(..., ge=0, description="ID cannot be negative")
    quantity: int = Field(..., ge=1, description="Quantity cannot be zero or negative")


class OrderItem(AuditBase, table=True):
    __tablename__ = "order_items"
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="orders.order_id")
    product_id: int = Field(foreign_key="products.product_id")
    quantity: int
    product_price: Decimal  = Field(
        sa_column=Column(Numeric(10, 2))
    )
    product: "Product" = Relationship(back_populates="order_items")
    order: "Order" = Relationship(back_populates="order_items")
    
    
register_audit_listeners(OrderItem)