from sqlalchemy.orm import Session
from uuid import UUID
from models.user import User
from models.video import Video
from models.follows import Follow
from models.likes import likes

def toggle_like(db: Session, user_id: UUID, video_id: UUID):
    """Adds or removes a like from a video."""
    # Check if like exists
    video = db.query(Video).filter(Video.id == video_id).first()
    user = db.query(User).filter(User.id == user_id).first()
    
    if video in user.liked_videos:
        user.liked_videos.remove(video)
        video.likes_count -= 1
    else:
        user.liked_videos.append(video)
        video.likes_count += 1
    
    db.commit()
    return {"likes_count": video.likes_count}

def follow_user(db: Session, follower_id: UUID, following_id: UUID):
    """Creates a follow relationship."""
    db_follow = Follow(follower_id=follower_id, following_id=following_id)
    db.add(db_follow)
    db.commit()
    return db_follow