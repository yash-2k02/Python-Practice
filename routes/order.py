from fastapi import APIRouter, HTTPException
from models import OrderItem, OrderCreate, Order
from db import get_connection
from typing import List

router = APIRouter()


@router.post("/create")
def create_order(order: OrderCreate, created_by: str):
    
    db = get_connection()
    cur = db.cursor()

    try:
        cur.execute("SELECT id FROM customers WHERE id = %s AND is_deleted = 0", (order.customer_id,))
        if not cur.fetchone():
            raise HTTPException(status_code=404, detail=f"Customer id: {order.customer_id} not found")

        cur.execute(
            "INSERT INTO orders (customer_id, created_by, updated_by) VALUES (%s, %s, %s)",
            (order.customer_id, created_by, created_by)
        )
        order_id = cur.lastrowid

        for item in order.items:
            cur.execute("SELECT price FROM products WHERE id = %s AND is_deleted = 0", (item.product_id,))
            product = cur.fetchone()
            if not product:
                raise HTTPException(status_code=404, detail=f"Product id: {item.product_id} not found")

            price_at_purchase = product[0]
            cur.execute(
                """INSERT INTO order_items(order_id, product_id, quantity, price_at_purchase, created_by, updated_by)
                   VALUES(%s, %s, %s, %s, %s, %s)""",
                (order_id, item.product_id, item.quantity, price_at_purchase, created_by, created_by)
            )

        db.commit()
        return {"order_id": order_id, "message": "Order created successfully"}

    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()


@router.get("/id/{order_id}", response_model=Order)
def get_order_by_id(order_id: int):
    
    db = get_connection()
    cur = db.cursor(dictionary=True)

    cur.execute("SELECT * FROM orders WHERE id = %s AND is_deleted = 0", (order_id,))
    order = cur.fetchone()
    if not order:
        cur.close()
        db.close()
        raise HTTPException(status_code=404, detail="Order not found")

    cur.execute("SELECT * FROM order_items WHERE order_id = %s AND is_deleted = 0", (order_id,))
    items = cur.fetchall()

    cur.close()
    db.close()

    order_items = [OrderItem(**item) for item in items]

    return Order(
        id=order["id"],
        customer_id=order["customer_id"],
        order_date=order["order_date"],
        items=order_items
    )


@router.get("/all", response_model=List[Order])
def get_all_orders():
    
    db = get_connection()
    cur = db.cursor(dictionary=True)

    cur.execute("SELECT * FROM orders WHERE is_deleted = 0")
    orders = cur.fetchall()
    if not orders:
        cur.close()
        db.close()
        raise HTTPException(status_code=404, detail="No orders found")

    order_list = []
    for order in orders:
        cur.execute("SELECT * FROM order_items WHERE order_id = %s AND is_deleted = 0", (order["id"],))
        items = cur.fetchall()
        order_items = [OrderItem(**item) for item in items]

        order_list.append(
            Order(
                id=order["id"],
                customer_id=order["customer_id"],
                order_date=order["order_date"],
                items=order_items
            )
        )

    cur.close()
    db.close()
    return order_list


@router.delete("/delete/{order_id}")
def delete_order(order_id: int, updated_by: str):
    
    db = get_connection()
    cur = db.cursor()

    try:
        cur.execute(
            "UPDATE orders SET is_deleted = 1, updated_by = %s WHERE id = %s",
            (updated_by, order_id)
        )
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Order not found")

        cur.execute(
            "UPDATE order_items SET is_deleted = 1, updated_by = %s WHERE order_id = %s",
            (updated_by, order_id)
        )

        db.commit()
        return {"message": "Order deleted successfully"}

    except Exception as e:
        db.rollback()
        raise e
    finally:
        cur.close()
        db.close()