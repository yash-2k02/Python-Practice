from typing import Optional
from pydantic import EmailStr
from sqlmodel import Relationship, SQLModel, Field
from models import Customer


class UserCreate(SQLModel):
    username: str = Field(..., min_length=6, max_length=15, description="Username must be 6-15 chars")
    password: str = Field(..., min_length=6, max_length=15, description="Password must be 6-15 chars")
    email: EmailStr
    
class UserLogin(SQLModel):
    username: str
    password: str


class UserModel(SQLModel, table=True):
    __tablename__ = "users"
    user_id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str
    email: str = Field(unique=True)
    is_active: bool = Field(default=True)
    created_by: str = Field(default="Admin")
    updated_by: str = Field(default="Admin")
    customer: "Customer" = Relationship(back_populates="user")
