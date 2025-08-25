from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Product, ProductCreate, ProductUpdate
from db import get_session
from models.User import UserModel
from auth import get_current_user
from logger import logger 

router = APIRouter(prefix="/product", tags=["Product"])


@router.post("/create")
def create_product(product: ProductCreate, session: Session = Depends(get_session), current_user: UserModel = Depends(get_current_user)):
    
    logger.info(f"User '{current_user.username}' is attempting to create product '{product.product_name}'")

    existing_product = session.exec(
        select(Product).where(Product.product_name == product.product_name)
    ).first()

    if existing_product:
        logger.warning(f"Product creation failed. Product '{product.product_name}' already exists")
        raise HTTPException(status_code=400, detail="Product already exists")
    
    db_product = Product(**product.model_dump(), created_by=current_user.username, updated_by=current_user.username)
    
    try:
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        logger.info(f"Product created successfully: {db_product.product_name} (id={db_product.product_id})")
        
        return db_product
    
    except Exception as e:
        session.rollback()
        logger.error(f"Error creating product '{product.product_name}': {e}")
        
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/update/{id}")
def update_product(id: int, data: ProductUpdate, current_user: UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    logger.info(f"User '{current_user.username}' is attempting to update product id={id}")

    product = session.get(Product, id)
    if not product:
        logger.warning(f"Product update failed. Product id={id} not found")
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    
    product.updated_by = current_user.username

    try:
        session.add(product)
        session.commit()
        session.refresh(product)
        logger.info(f"Product updated successfully: id={product.product_id}, name={product.product_name}")
        
        return product
    
    except Exception as e:
        session.rollback()
        logger.error(f"Error updating product id={id}: {e}")
        
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/delete/{id}")
def delete_product(id:int, current_user:UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    logger.info(f"User '{current_user.username}' is attempting to delete product id={id}")

    product = session.get(Product, id)
    if not product:
        logger.warning(f"Product deletion failed. Product id={id} not found")
        raise HTTPException(status_code=400, detail="Product not found")

    product.is_deleted = 1
    product.updated_by = current_user.username

    try:
        session.commit()
        session.refresh(product)
        logger.info(f"Product deleted successfully: id={id}, name={product.product_name}")
        
        return {"message": "Product deleted"}
    
    except Exception as e:
        session.rollback()
        logger.error(f"Error deleting product id={id}: {e}")
        
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/all")
def get_all_products(session:Session = Depends(get_session)):
    logger.info("Fetching all active products")

    products = session.exec(select(Product).where(Product.is_deleted == 0)).all()
    logger.info(f"Fetched {len(products)} products")
    return products


@router.get("/{id}")
def get_single_product(id:int, session:Session = Depends(get_session)):
    logger.info(f"Fetching product by id={id}")

    product = session.exec(
        select(Product).where((Product.product_id == id) & (Product.is_deleted == False))
    ).first()
    
    if not product:
        logger.warning(f"Product not found: id={id}")
        raise HTTPException(status_code=404, detail="Product not found")
    
    logger.info(f"Fetched product successfully: id={product.product_id}, name={product.product_name}")
    return product
