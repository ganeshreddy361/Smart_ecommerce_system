from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    image: Optional[str] = None
    category: Optional[str] = None

class ProductResponse(ProductCreate):
    id: int
    popularity: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class CartRequest(BaseModel):
    product_id: int
    quantity: int = 1

class CartResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    model_config = ConfigDict(from_attributes=True)

class OrderResponse(BaseModel):
    id: int
    total: float
    payment_status: str
    order_status: str
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)

class NotificationResponse(BaseModel):
    id: int
    type: str
    message: str
    read: bool
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)
