from sqlalchemy import Column, Integer, String

from app.api.database.models.Base import Base

class Company(Base):

  __tablename__ = 'companies'

  id = Column(Integer, primary_key=True, autoincrement=True)

  name = Column(String(80))

  website = Column(String(80), nullable=True)

  def __init__(self, name, website):
    self.name = name
    self.website = website

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'website': self.website
    }
