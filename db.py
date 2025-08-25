from fastapi import HTTPException
from sqlmodel import create_engine, SQLModel, Session
from config import settings
from sqlalchemy.exc import SQLAlchemyError
from models import Customer, Category, Invoice, Order, OrderItem, Product, UserModel


DATABASE_URL = settings.database_url

# engine = create_engine(DATABASE_URL)


# def init_db():
#     SQLModel.metadata.create_all(engine)


# def get_session():
#     try:
#         with Session(engine) as session:
#             yield session
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
 
 
        

from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

engine = create_async_engine(DATABASE_URL)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    try:
        async with AsyncSession(engine) as session:
            yield session
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")