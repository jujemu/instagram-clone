from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class DbUser(Base):
    """
    Args:
        id = int, primary key,
        username = str, required,
        email = str, required,
        password = str, required,
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    
    items = relationship('DbPost', back_populates='user')


class DbPost(Base):
    """
    Args:
        id = int, primary_key,
        image_url = required,
        image_url_type = required,
        caption = required,
        timestamp = datetime when created,
        user_id = foreign_key,
    """
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String) 
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('DbUser', back_populates='items')
    