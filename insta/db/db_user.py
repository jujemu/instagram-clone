from sqlalchemy.orm import Session

from ..routers.schemas import UserBase
from .models import DbUser


def create_user(
    request: UserBase,
    db: Session,    
):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = request.password, # it has to be hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
