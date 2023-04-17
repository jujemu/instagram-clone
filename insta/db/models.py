from .database import Base
from sqlalchemy import Column, Integer, String


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
