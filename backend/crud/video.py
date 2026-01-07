from sqlalchemy.orm import Session
from uuid import UUID
from backend.models.video import Video
from backend.schemas.video import VideoCreate, VideoUpdate

def create_video(db: Session, video_in: VideoCreate):
    """Creates a video record linked to an author."""
    # .model_dump() converts Pydantic to a dict we can unpack with **
    db_video = Video(**video_in.model_dump())
    
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_video(db: Session, video_id: UUID):
    """Fetch a specific video by ID."""
    return db.query(Video).filter(Video.id == video_id).first()

def get_all_videos(db: Session, skip: int = 0, limit: int = 20):
    """Fetch a list of videos for a feed."""
    return db.query(Video).offset(skip).limit(limit).all()

def update_video_status(db: Session, db_video: Video, status: str):
    """Updates status (e.g., from 'uploading' to 'ready')."""
    db_video.status = status
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video