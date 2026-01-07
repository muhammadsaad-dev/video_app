from .user import create_user, get_user, get_user_by_email, authenticate
from .video import create_video, get_video, get_all_videos
from .comment import create_comment, get_video_comments

# This allows you to use 'crud.user' if you prefer that syntax in your routes
from . import user
from . import video
from . import comment