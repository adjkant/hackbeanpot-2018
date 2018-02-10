from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base
from app.api.database.models.SchoolModel import School
from app.api.database.models.JobModel import Job
from app.api.database.models.UserModel import User

class Review(Base):

  __tablename__ = 'reviews'

  id = Column(Integer, primary_key=True, autoincrement=True)

  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship('User', foreign_keys='Review.user_id')

  school_id = Column(Integer, ForeignKey('schools.id'))
  school = relationship('School', foreign_keys='Review.school_id')

  job_id = Column(Integer, ForeignKey('jobs.id'))
  job = relationship('Job', foreign_keys='Review.job_id')

  job_type = Column(Enum('co-op', 'internship', 'reu', name='job_types'))

  duration = Column(Integer)

  location = Column(String(80))

  def __init__(self, user_id, school_id, job_id, job_type, duration, location):
    self.user_id = user_id
    self.school_id = school_id
    self.job_id = job_id
    self.job_type = job_type
    self.duration = duration
    self.location = location

  @property
  def serialize(self):
    return {
      'id': self.id,
      'school_id': self.school_id,
      'job_id': self.job_id,
      'job_type': self.job_type,
      'duration': self.duration,
      'location': self.location
    }
