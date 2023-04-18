import datetime
import random
import string
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from ..db.database import get_db
from ..db import db_post
from .schemas import PostBase, PostDisplay

router = APIRouter(
    tags=['Post'],
    prefix='/post'
)

image_url_type = ['relative', 'absolute']


@router.post('', response_model=PostDisplay, status_code=status.HTTP_201_CREATED)
def create_post(
    request: PostBase,
    db: Session = Depends(get_db)
):
    if request.image_url_type not in image_url_type:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Parameter image_url_type can only take values absolute or relative.'
        )
        
    return db_post.create(request, db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    # for unique name of image
    letters = string.ascii_letters
    rand_str = ''.join([random.choice(letters) for _ in range(5)]) + datetime.datetime.now().strftime("%Y-%m-%d")
    
    
@router.get('', response_model=list[PostDisplay])
def show_all_post(
    db: Session = Depends(get_db)
):
    return db_post.show_all(db)


@router.get('/{id}', response_model=PostDisplay)
def show_post_with_id(
    id: int,
    db: Session = Depends(get_db)
):
    return db_post.show(id, db)
