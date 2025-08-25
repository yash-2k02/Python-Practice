from fastapi import APIRouter, HTTPException
from models import CustomerCreate, Customer, CustomerUpdate
from db import get_connection
from typing import List

router = APIRouter()

@router.post("/create")
def create_customer(customer:CustomerCreate, created_by: str):
    db = get_connection()
    cur = db.cursor()
    cur.execute("insert into customers(name, email, created_by, updated_by) values (%s, %s, %s)", (customer.name, customer.email, created_by, created_by))
    db.commit()
    customer_id = cur.lastrowid
    cur.close()
    db.close()
    return {"id": customer_id, **customer.model_dump()}


@router.get("/id/{cust_id}", response_model = Customer)
def get_customer_by_id(cust_id: int):
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("select id,name,email from customers where id = %s and is_deleted = 0", (cust_id,))
    cust = cur.fetchone()
    cur.close()
    db.close()
    if not cust:
        raise HTTPException(status_code=404, detail="Customer not found")
    return cust


@router.get("/all", response_model = List[Customer])
def get_all_customers():
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("select id,name,email from customers where is_deleted = 0")
    cust = cur.fetchall()
    cur.close()
    db.close()
    if not cust:
        raise HTTPException(status_code=404, detail="Customers not found")
    return cust


@router.put("/update/{cust_id}")
def update_customer(cust_id:int, customer: CustomerUpdate, updated_by: str):
    db = get_connection()
    cur = db.cursor()
    cur.execute("""
        update customers
        set 
            name = coalesce(%s, name),
            email = coalesce(%s, email),
            updated_by = %s
        where id = %s
    """, (
        customer.name,
        customer.email,
        updated_by,
        cust_id
    ))
    db.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    cur.close()
    db.close()
    return {"message": "Customer details updated"}


@router.delete("/delete/{cust_id}")
def delete_customer(cust_id:int):
    db = get_connection()
    cur = db.cursor()
    cur.execute("update customers set is_deleted = %s where id = %s", (1, cust_id))
    db.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Customer not found")
    cur.close()
    db.close()
    return {"message": "Customer deleted"}