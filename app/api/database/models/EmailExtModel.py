from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base

class EmailExt(Base):

  __tablename__ = 'email_exts'

  id = Column(Integer, primary_key=True, autoincrement=True)

  domain = Column(String(80))

  school_id = Column(Integer, ForeignKey('schools.id'))
  school = relationship('School', foreign_keys='EmailExt.school_id')

  def __init__(self, domain, school_id):
    self.domain = domain
    self.school_id = school_id

  @property
  def serialize(self):
    return {
      'id': self.id,
      'domain': self.domain,
      'school_id': self.school_id
    }
