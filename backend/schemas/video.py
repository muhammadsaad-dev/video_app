from pydantic import BaseModel, HttpUrl, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from ..models.video import VideoStatus # Import the Enum you created earlier

# Shared attributes for Videos
class VideoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=500)
    # We use str for URLs here since they might be placeholders initially
    video_url: str 
    thumb_url: Optional[str] = None

# Schema for Video Upload/Creation
class VideoCreate(VideoBase):
    author_id: UUID

# Schema for Updating Video metadata (e.g., changing title)
class VideoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=500)
    status: Optional[VideoStatus] = None
    thumb_url: Optional[str] = None

# Schema for API Responses
class Video(VideoBase):
    id: UUID
    author_id: UUID
    status: VideoStatus
    likes_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)