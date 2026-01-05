from sqlalchemy.orm import Session
from uuid import UUID
from passlib.context import CryptContext
from models.user import User
from schemas.user import UserCreate, UserUpdate

# Setup password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Hashes a plain-text password."""
    return pwd_context.hash(password)

def get_user(db: Session, user_id: UUID):
    """Fetch a single user by their UUID."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    """Check if an email is already registered."""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in: UserCreate):
    """Hashes password and saves a new user to the DB."""
    hashed_password = get_password_hash(user_in.password)
    
    db_user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hashed_password,
        bio=user_in.bio
        # avatar_url uses the model default
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: User, user_in: UserUpdate):
    """Updates user profile fields dynamically."""
    update_data = user_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user