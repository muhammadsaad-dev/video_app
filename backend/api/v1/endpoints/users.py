from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any

import crud
import schemas
from api.deps import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def register_user(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate
) -> Any:
    """
    Create a new user.
    """
    # Check if user already exists
    user = crud.user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    return crud.user.create_user(db, user_in=user_in)

@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: str, # UUIDs are passed as strings in URLs
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific user by ID.
    """
    user = crud.user.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user