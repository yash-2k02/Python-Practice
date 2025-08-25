from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import CustomerCreate, Customer, CustomerUpdate, Order
from db import get_session
from models.User import UserModel
from auth import get_current_user
from logger import logger 

router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/create")
def create_customer(customer: CustomerCreate, session: Session = Depends(get_session), current_user: UserModel = Depends(get_current_user)):
    
    existing_customer = session.exec(
        select(Customer).where(Customer.user_id == current_user.user_id)
    ).first()

    if existing_customer:
        logger.warning(f"Customer profile already exists for user_id={current_user.user_id}, username={current_user.username}")
        raise HTTPException(status_code=400, detail="Customer profile already exists")
    
    db_customer = Customer(
        **customer.model_dump(), 
        user_id=current_user.user_id, 
        created_by=current_user.username, 
        updated_by=current_user.username
    )
    
    session.add(db_customer)
    session.commit()
    session.refresh(db_customer)
    
    logger.info(f"Customer created successfully: customer_id={db_customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return db_customer


@router.patch("/update")
def update_customer(data: CustomerUpdate, current_user: UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    
    customer = session.get(Customer, current_user.user_id)
    if not customer:
        logger.error(f"Customer not found for user_id={current_user.user_id}, username={current_user.username}")
        raise HTTPException(status_code=404, detail="Customer not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(customer, key, value)
    
    session.add(customer)
    session.commit()
    session.refresh(customer)
    
    logger.info(f"Customer updated successfully: customer_id={customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return customer


@router.delete("/delete")
def delete_customer(current_user:UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    
    customer = session.exec(
        select(Customer).where(Customer.user_id == current_user.user_id)
    ).first()
    
    if not customer:
        logger.error(f"Delete failed: Customer not found for user_id={current_user.user_id}, username={current_user.username}")
        raise HTTPException(status_code=404, detail="Customer not found")
    
    customer.is_deleted = 1
    customer.updated_by = current_user.username
    session.commit()
    session.refresh(customer)
    
    logger.info(f"Customer deleted: customer_id={customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return {"message": "Customer deleted"}


@router.get("/me")
def get_my_info(current_user: UserModel = Depends(get_current_user)):
    logger.info(f"Fetched current user info: user_id={current_user.user_id}, username={current_user.username}")
    return current_user
    

@router.get("/myorders")
def get_customer_orders(current_user:UserModel = Depends(get_current_user), session: Session = Depends(get_session)):
    
    orders = session.exec(
        select(Order).where(Order.customer_id == current_user.customer.customer_id)
    ).all()
    
    logger.info(f"Fetched orders for customer_id={current_user.customer.customer_id}, username={current_user.username}. Total orders={len(orders)}")
    
    return orders
