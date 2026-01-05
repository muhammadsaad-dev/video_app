from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

# Shared attributes across all User schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_]+$")
    email: EmailStr
    bio: Optional[str] = Field(None, max_length=500)

# Schema for User Registration (Input)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100)

# Schema for Profile Updates (Optional fields)
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    bio: Optional[str] = Field(None, max_length=500)
    avatar_url: Optional[str] = None

# Schema for API Responses (Output)
class User(UserBase):
    id: UUID
    avatar_url: str
    created_at: datetime

    # This replaces 'orm_mode = True' in Pydantic v2
    model_config = ConfigDict(from_attributes=True)