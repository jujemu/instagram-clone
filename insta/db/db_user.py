from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..routers.schemas import UserBase
from .hashing import Hash
from .models import DbUser


def create(
    request: UserBase,
    db: Session,    
):
    hashed_password = Hash.bcrypt(request.password)
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def show_all(
    db: Session
):
    blogs = db.query(DbUser).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blog in db")

    return blogs


def show(
    id: int,
    db: Session
):
    blog = db.query(DbUser).filter(DbUser.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No blog with id {id} in db")
    
    return blog
