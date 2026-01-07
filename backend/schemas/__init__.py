from .user import User, UserCreate, UserUpdate
from .video import Video, VideoCreate, VideoUpdate
from .comment import Comment, CommentCreate, CommentWithAuthor

# This makes them available when you 'import schemas'
__all__ = [
    "User", "UserCreate", "UserUpdate",
    "Video", "VideoCreate", "VideoUpdate",
    "Comment", "CommentCreate", "CommentWithAuthor"
]