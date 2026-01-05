from backend.base import Base
from sqlalchemy import Column, UUID, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func
import uuid

class Comment(Base):
    __tablename__ = "comments"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    video_id = Column(UUID(as_uuid=True), ForeignKey("videos.id"), nullable=False, index=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    video = relationship("Video", back_populates="comments")
    author = relationship("User", back_populates="comments")