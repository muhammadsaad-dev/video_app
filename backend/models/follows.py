import uuid
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.base import Base

class Follow(Base):
    __tablename__ = "follows"
    
    # follower_id: the person who clicks "Follow"
    follower_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    # following_id: the person being followed
    following_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Optional: help SQLAlchemy navigate the self-referential relationship
    follower = relationship("User", foreign_keys=[follower_id], back_populates="following")
    followed_user = relationship("User", foreign_keys=[following_id], back_populates="followers")