from sqlalchemy import Column, Integer, String

from app.api.database.models.Base import Base

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  
  email = Column(String(80), unique=True)
  
  password = Column(String(100))
  
  first = Column(String(80))
  last = Column(String(80))
  
  role = Column(Integer)
  
  def __init__(self, email, password, first, last, role):
    self.email = email
    self.password = password
    self.first = first
    self.last = last
    self.role = role