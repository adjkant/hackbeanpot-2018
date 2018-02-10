from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  
  email = Column(String(80), unique=True)
  password = Column(String(100))
  
  first = Column(String(80))
  last = Column(String(80))
  
  school_id = Column(Integer, ForeignKey('schools.id'))
  school = relationship('School', foreign_keys='User.school_id')

  def __init__(self, email, password, first, last, school_id):
    self.email = email
    self.password = password
    self.first = first
    self.last = last
    self.school_id = school_id

  @property
  def serialize(self):
    return {
      'id': self.id,
      'email': self.email,
      'first': self.first,
      'last': self.last,
      'school_id': self.school_id
    }
