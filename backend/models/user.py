import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID # Best for Postgres
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .likes import likes
from backend.base import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    avatar_url = Column(
        String(500), 
        nullable=False, 
        default="PLACEHOLDER_S3_URL_DEFAULT_AVATAR" 
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    videos = relationship("Video", back_populates="author", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")
    liked_videos = relationship("Video", secondary=likes, back_populates="liked_by_users")
    # Inside class User(Base):
    followers = relationship("Follow", foreign_keys="Follow.following_id", back_populates="followed_user")
    following = relationship("Follow", foreign_keys="Follow.follower_id", back_populates="follower")

