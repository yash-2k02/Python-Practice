from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from models.base import AuditBase, register_audit_listeners
from models import Order

# class InvoiceCreate(SQLModel):
#     order_id: int
#     due_date: Optional[datetime] = None
#     subtotal: float
#     tax_amount: float = 0.0
#     discount_amount: float = 0.0
#     total_amount: float


class InvoiceUpdate(SQLModel):
    due_date: Optional[datetime] = None
    tax_amount: Optional[float] = None
    discount_amount: Optional[float] = None
    total_amount: Optional[float] = None
    payment_status: Optional[str] = None
    payment_method: Optional[str] = None
    payment_date: Optional[datetime] = None
    updated_by: Optional[str] = None


class Invoice(AuditBase, table=True):
    __tablename__ = "invoices"
    invoice_id: Optional[int] = Field(default=None, primary_key=True)
    invoice_number: str = Field(index=True, unique=True, nullable=False)
    order_id: int = Field(foreign_key="orders.order_id")

    invoice_date: datetime = Field(default_factory=datetime.now(timezone.utc))
    due_date: Optional[datetime] = None

    subtotal: float
    tax_amount: float = 0.0
    discount_amount: float = 0.0
    total_amount: float

    payment_status: str = Field(default="PENDING")
    payment_method: Optional[str] = None
    payment_date: Optional[datetime] = None

    order: "Order" = Relationship(back_populates="invoice")


register_audit_listeners(Invoice)
