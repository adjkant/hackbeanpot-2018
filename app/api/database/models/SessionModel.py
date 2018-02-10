import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base

class Session(Base):
  __tablename__ = 'sessions'

  id = Column(Integer, primary_key=True, autoincrement=True)
  token = Column(String(36), unique=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', foreign_keys='Session.user_id')
  
  def __init__(self, user_id):
    self.user_id = user_id
    self.token = str(uuid.uuid4())

  def __str__(self):
    return self.token
