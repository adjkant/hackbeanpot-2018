from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base
from app.api.database.models.CompanyModel import Company

class Job(Base):
  __tablename__ = 'jobs'

  id = Column(Integer, primary_key=True, autoincrement=True)

  title = Column(String(80))

  company_id = Column(Integer, ForeignKey('companies.id'))
  company = relationship('Company', foreign_keys='Job.company_id')

  def __init__(self, title, company_id):
    self.title = title
    self.company_id = company_id

  @property
  def serialize(self):
    return {
      'id': self.id,
      'title': self.title,
      'company_id': self.company_id
    }
