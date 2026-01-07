from sqlalchemy.orm import Session
from uuid import UUID
from backend.models.comment import Comment
from backend.schemas.comment import CommentCreate

def create_comment(db: Session, comment_in: CommentCreate, author_id: UUID):
    """Saves a comment and links it to both the video and the author."""
    db_comment = Comment(
        **comment_in.model_dump(),
        author_id=author_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_video_comments(db: Session, video_id: UUID):
    """Fetches all comments for a specific video."""
    return db.query(Comment).filter(Comment.video_id == video_id).all()