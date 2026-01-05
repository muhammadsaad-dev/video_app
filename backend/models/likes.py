from sqlalchemy import Table, Column, UUID, ForeignKey
from backend.base import Base


likes = Table(
    "likes",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
    Column("video_id", UUID(as_uuid=True), ForeignKey("videos.id"), primary_key=True),
)