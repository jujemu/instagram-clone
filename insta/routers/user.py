from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db import db_user
from .schemas import UserDisplay, UserBase

router = APIRouter(
    tags=['User'],
    prefix='/user'
)


@router.post('', response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
def create_user(
    request: UserBase,
    db: Session = Depends(get_db)
):
    return db_user.create(request, db)


@router.get('', response_model=list[UserDisplay])
def show_all_user(
    db: Session = Depends(get_db)
):
    return db_user.show_all(db)


@router.get('/{id}', response_model=UserDisplay)
def show_user_with_id(
    id: int,
    db: Session = Depends(get_db)
):
    return db_user.show(id, db)
