import enum
import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Enum, ForeignKey, Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .likes import likes
from backend.base import Base

class VideoStatus(enum.Enum):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    READY = "ready"
    ERROR = "error"

class Video(Base):
    __tablename__ = "videos"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    video_url = Column(String(500), nullable=False)
    thumb_url = Column(String(500), nullable=True)
    title = Column(String(500), nullable=False)
    status = Column(Enum(VideoStatus), name="video_status", default=VideoStatus.UPLOADING)
    likes_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author = relationship("User", back_populates="videos")
    comments = relationship("Comment", back_populates="video", cascade="all, delete-orphan")
    liked_by_users = relationship("User", secondary=likes, back_populates="liked_videos")

