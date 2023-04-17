from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db.db_user import create_user
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
    return create_user
