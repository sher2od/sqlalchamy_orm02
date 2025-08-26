from datetime import datetime
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    user_id = Column('id',Integer,primary_key=True,index=True,nullable=False)
    username = Column('username',String(length=64),unique=True,nullable=False)

    created_at = Column('created_at',DateTime,default=datetime.now)
    updated_at = Column('updated_at',DateTime,onupdate=datetime.now)

    posts = relationship('Post',back_populates='user')

class Post(Base):
    __tablename__ = 'posts'

    post_id = Column('id',Integer,primary_key=True,index=True,nullable=False)
    title = Column('title',String(length=128),nullable=False)
    content = Column('content',Text,nullable=False,default="")
    user_id = Column('user_id',Integer,ForeignKey('users.id'))

    created_at = Column('created_at',DateTime,default=datetime.now)
    updated_at = Column('updated_at',DateTime,onupdate=datetime.now)

    user = relationship('User',back_populates='posts')
