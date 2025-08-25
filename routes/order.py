from datetime import datetime, timezone
from decimal import Decimal
import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Order, OrderCreate, OrderUpdate, OrderItem, Product, Invoice
from db import get_session
from models.User import UserModel
from auth import get_current_user
from logger import logger

router = APIRouter(prefix="/order", tags=["Order"])

def generate_invoice_number():
    return f"INV-{datetime.now().year}-{uuid.uuid4().hex[:6].upper()}"


@router.post("/create")
def create_order(order_data: OrderCreate, session: Session = Depends(get_session), current_user: UserModel = Depends(get_current_user)):
    logger.info(f"User '{current_user.username}' is creating a new order")

    order = Order(
        customer_id=current_user.customer.customer_id,
        created_by=current_user.username,
        updated_by=current_user.username
    )
    session.add(order)
    session.flush()

    subtotal = Decimal("0.0")

    for item in order_data.items:
        product = session.get(Product, item.product_id)
        if not product:
            logger.warning(
                f"Product with ID {item.product_id} not found for order by user '{current_user.username}'"
            )
            raise HTTPException(status_code=400, detail=f"Product with ID {item.product_id} not found.")

        line_total = product.product_price * item.quantity
        subtotal += line_total

        logger.debug(f"Adding product {item.product_id} (Qty: {item.quantity}) to order {order.order_id}")
        order_item = OrderItem(
            order_id=order.order_id,
            product_id=item.product_id,
            quantity=item.quantity,
            product_price=product.product_price,
            created_by=current_user.username,
            updated_by=current_user.username
        )
        session.add(order_item)

    tax_amount = subtotal * Decimal("0.1")
    discount_amount = Decimal("0.0")
    total_amount = subtotal + tax_amount - discount_amount

    session.commit()
    session.refresh(order)

    logger.info(f"Order {order.order_id} successfully created by user '{current_user.username}'")

    invoice = Invoice(
        invoice_number=generate_invoice_number(),
        order_id=order.order_id,
        invoice_date=datetime.now(timezone.utc),
        subtotal=subtotal,
        tax_amount=tax_amount,
        discount_amount=discount_amount,
        total_amount=total_amount,
        created_by=current_user.username,
        updated_by=current_user.username
    )

    session.add(invoice)
    session.commit()
    session.refresh(invoice)

    logger.info(f"Invoice {invoice.invoice_number} created for order {order.order_id}")

    return {
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "invoice": {
            "invoice_id": invoice.invoice_id,
            "invoice_number": invoice.invoice_number,
            "total_amount": invoice.total_amount,
            "payment_status": invoice.payment_status,
        }
    }


@router.patch("/update/{id}")
def update_order(id: int, data: OrderUpdate, current_user: UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    logger.info(f"User '{current_user.username}' is updating order ID {id}")

    order = session.get(Order, id)
    if not order:
        logger.error(f"Update failed - Order {id} not found")
        raise HTTPException(status_code=404, detail="Order not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(order, key, value)

    order.updated_by = current_user.username
    session.add(order)
    session.commit()
    session.refresh(order)

    logger.info(f"Order {id} updated successfully by '{current_user.username}'")
    return order


@router.delete("/delete/{id}")
def delete_order(id: int, current_user: UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    logger.info(f"User '{current_user.username}' requested delete for order ID {id}")

    order = session.get(Order, id)

    if not order:
        logger.error(f"Delete failed - Order {id} not found")
        raise HTTPException(status_code=400, detail="Order not found")

    order.is_deleted = True
    order.updated_by = current_user.username

    order_items = order.order_items
    for item in order_items:
        item.is_deleted = True

    session.commit()
    session.refresh(order)

    logger.info(f"Order {id} marked as deleted by '{current_user.username}'")
    return {"message": "Order deleted"}


@router.get("/all")
def get_all_orders(session: Session = Depends(get_session)):
    logger.debug("Fetching all active orders")
    orders = session.exec(select(Order).where(Order.is_deleted == False)).all()
    logger.info(f"Fetched {len(orders)} active orders")
    return orders


@router.get("/{id}")
def get_single_order(id: int, session: Session = Depends(get_session)):
    logger.debug(f"Fetching order ID {id}")
    order = session.exec(select(Order).where((Order.order_id == id) & (Order.is_deleted == False))).first()
    
    if not order:
        logger.warning(f"Order {id} not found")
        raise HTTPException(status_code=404, detail="Order not found")
    
    logger.info(f"Order {id} fetched successfully")
    return order
