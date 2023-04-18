from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    class Config:
        orm_mode = True
        
    username: str
    email: str


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int
    

# For PostDisplay
class User(BaseModel):
    class Config:
        orm_mode = True
    
    username: str

class PostDisplay(BaseModel):
    class Config:
        orm_mode = True
        
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    