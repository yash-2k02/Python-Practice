from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlmodel import Session
from db import get_session
from models.User import UserModel, UserCreate 
from auth import pwd_context
from logger import logger


router = APIRouter(prefix="/user", tags=["User"])


def get_password_hash(password: str):
    return pwd_context.hash(password)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, session: Session = Depends(get_session)):

    logger.info(f"Attempting to create user: {user.username}")

    existing_user = session.exec(
        select(UserModel).where(
            UserModel.username == user.username
        )
    ).first()

    if existing_user:
        logger.warning(f"User creation failed. Username already exists: {user.username}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    db_user = UserModel(
        username=user.username,
        hashed_password=get_password_hash(user.password),
        email=user.email
    )

    try:
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        logger.info(f"User created successfully: {db_user.username} (id={db_user.user_id})")
        
        return {"id": db_user.user_id, "username": db_user.username}
    
    except Exception as e:
        session.rollback()
        logger.error(f"Error creating user {user.username}: {e}")
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
