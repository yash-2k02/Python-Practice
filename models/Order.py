from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional, List
from enum import Enum as PyEnum
from sqlalchemy import Enum as SQLAlchemyEnum
from models.base import AuditBase, register_audit_listeners
from models.OrderItem import OrderItemCreate

class OrderStatus(str, PyEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"   
    CANCELLED = "cancelled"
    RETURN_REQUESTED = "return_requested"
    RETURNED = "returned"
    FAILED = "failed"
    REFUNDED = "refunded"                

if TYPE_CHECKING:
    from Customer import Customer
    from OrderItem import OrderItem
    from Invoice import Invoice


class OrderCreate(SQLModel):
    items: List[OrderItemCreate]
    
class OrderUpdate(SQLModel):
    customer_id: Optional[int] = Field(None, ge=1, description="ID should be greater or equal to 1")
    order_status: Optional[OrderStatus] = None
    


class Order(AuditBase, table=True):
    __tablename__ = "orders"
    order_id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customers.customer_id")
    order_status: OrderStatus = Field(sa_column=SQLAlchemyEnum(OrderStatus), default=OrderStatus.PENDING)
    customer: "Customer" = Relationship(back_populates="orders")
    order_items: List["OrderItem"] = Relationship(back_populates="order")
    invoice: "Invoice" = Relationship(back_populates="order")


register_audit_listeners(Order)
    
