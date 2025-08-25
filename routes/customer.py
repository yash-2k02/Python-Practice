from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from models import CustomerCreate, Customer, CustomerUpdate, Order
from db import get_session
from models.User import UserModel
from auth import get_current_user
from logger import logger 

router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/create")
async def create_customer(customer: CustomerCreate, session: AsyncSession = Depends(get_session), current_user: UserModel = Depends(get_current_user)):
    
    result = await session.exec(
        select(Customer).where(Customer.user_id == current_user.user_id)
    )
    
    existing_customer = result.one_or_none()

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
    await session.commit()
    await session.refresh(db_customer)
    
    logger.info(f"Customer created successfully: customer_id={db_customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return db_customer


@router.patch("/update")
async def update_customer(data: CustomerUpdate, current_user: UserModel = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    
    customer = await session.get(Customer, current_user.user_id)
    if not customer:
        logger.error(f"Customer not found for user_id={current_user.user_id}, username={current_user.username}")
        raise HTTPException(status_code=404, detail="Customer not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(customer, key, value)
    
    await session.commit()
    await session.refresh(customer)
    
    logger.info(f"Customer updated successfully: customer_id={customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return customer


@router.delete("/delete")
async def delete_customer(current_user:UserModel = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    
    result = await session.exec(
        select(Customer).where(Customer.user_id == current_user.user_id)
    )
    
    customer = result.one_or_none()
    
    if not customer:
        logger.error(f"Delete failed: Customer not found for user_id={current_user.user_id}, username={current_user.username}")
        raise HTTPException(status_code=404, detail="Customer not found")
    
    customer.is_deleted = True
    customer.updated_by = current_user.username
    await session.commit()
    
    logger.info(f"Customer deleted: customer_id={customer.customer_id}, user_id={current_user.user_id}, username={current_user.username}")
    
    return {"message": "Customer deleted"}


@router.get("/me")
async def get_my_info(current_user: UserModel = Depends(get_current_user)):
    logger.info(f"Fetched current user info: user_id={current_user.user_id}, username={current_user.username}")
    return current_user
    

@router.get("/myorders")
async def get_customer_orders(current_user:UserModel = Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    
    results = await session.exec(
        select(Order).where(Order.customer_id == current_user.customer.customer_id)
    )
    
    orders = results.all()
    
    logger.info(f"Fetched orders for customer_id={current_user.customer.customer_id}, username={current_user.username}. Total orders={len(orders)}")
    
    return orders
