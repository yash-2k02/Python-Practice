from fastapi import APIRouter, HTTPException
from models import ProductCreate, Product, ProductUpdate
from db import get_connection
from typing import List

router = APIRouter()

@router.post("/create")
def create_product(product:ProductCreate, created_by: str):
    db = get_connection()
    cur = db.cursor()
    cur.execute("insert into products(name, price, created_by) values (%s, %s, %s)", (product.name, product.price, created_by))
    db.commit()
    product_id = cur.lastrowid
    cur.close()
    db.close()
    return {"id": product_id, **product.model_dump()}


@router.get("/id/{prod_id}", response_model = Product)
def get_product_by_id(prod_id: int):
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("select id,name,price from products where id = %s", (prod_id,))
    prod = cur.fetchone()
    cur.close()
    db.close()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod


@router.get("/all", response_model = List[Product])
def get_all_products():
    db = get_connection()
    cur = db.cursor(dictionary=True)
    cur.execute("select id,name,price from products where is_deleted = 0")
    cust = cur.fetchall()
    cur.close()
    db.close()
    if not cust:
        raise HTTPException(status_code=404, detail="Product not found")
    return cust


@router.put("/update/{prod_id}")
def update_product(prod_id:int, product: ProductUpdate, updated_by: str):
    db = get_connection()
    cur = db.cursor()
    cur.execute("""
        update products
        set 
            name = coalesce(%s, name),
            price = coalesce(%s, price),
            updated_by = %s
        where id = %s
    """, (
        product.name,
        product.price,
        updated_by,
        prod_id
    ))
    db.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    cur.close()
    db.close()
    return {"message": "Product details updated"}


@router.delete("/delete/{prod_id}")
def delete_product(prod_id:int):
    db = get_connection()
    cur = db.cursor()
    cur.execute("update products set is_deleted = 0 where id = %s", (prod_id,))
    db.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    cur.close()
    db.close()
    return {"message": "Product deleted"}

