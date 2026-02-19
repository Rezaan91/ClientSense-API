from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

# Pydantic models for API
class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    # Add more fields as needed for churn prediction

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# SQLAlchemy models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    tenure = Column(Integer)
    monthly_charges = Column(Float)
    total_charges = Column(Float)
    # Add more fields