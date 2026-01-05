from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from .user import User  # Import the User schema for nesting

# Shared attributes
class CommentBase(BaseModel):
    body: str = Field(..., min_length=1, max_length=1000)

# Input for creating a comment
class CommentCreate(CommentBase):
    video_id: UUID

# Input for editing a comment
class CommentUpdate(BaseModel):
    body: str = Field(..., min_length=1, max_length=1000)

# Output for the API
class Comment(CommentBase):
    id: UUID
    author_id: UUID
    video_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Specialized Output Schema for the UI (Nested)
class CommentWithAuthor(Comment):
    author: User