from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..routers.schemas import PostBase
from .models import DbPost


def create(
    request: PostBase,
    db: Session    
):
    new_post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        user_id = request.creator_id
    )
    
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


def show_all(
    db: Session
):
    posts = db.query(DbPost).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No post in db")

    return posts


def show(
    id: int,
    db: Session
):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id {id} in db")
    
    return post
