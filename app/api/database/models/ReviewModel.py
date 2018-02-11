from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
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
  job_type = Column(Enum('co-op', 'internship', 'reu', 'remote', name='job_types'))

  company_id = Column(Integer, ForeignKey('companys.id'))
  company = relationship('Company', foreign_keys='Review.company_id')

  duration = Column(Integer)
  location = Column(String(80))

  salary = Column(Float)

  culture = Column(Integer)
  inclusivity = Column(Integer)
  facilities = Column(Integer)
  workload = Column(Integer)
  perks = Column(Integer)
  opps = Column(Integer)
  mentors = Column(Integer)
  purpose = Column(Integer)
  min_visible = Column(Integer)
  show_immediate = Column(Boolean)

  review_text = Column(String(1000))


  def __init__(self, user_id, school_id, job_id, job_type, company_id, duration, location, salary, ratings, min_visible, show_immediate, review_text):
    self.user_id = user_id
    self.school_id = school_id
    self.job_id = job_id
    self.job_type = job_type
    self.duration = duration
    self.location = location
    self.salary = salary

    self.culture = ratings[0]
    self.inclusivity = ratings[1]
    self.facilities = ratings[2]
    self.workload = ratings[3]
    self.perks = ratings[4]
    self.opps = ratings[5]
    self.mentors = ratings[6]
    self.purpose = ratings[7]

    self.min_visible = min_visible
    self.show_immediate = show_immediate
    self.review_text = review_text

  @property
  def serialize(self):
    return {
      'id': self.id,
      'school_id': self.school_id,
      'job_id': self.job_id,
      'job_type': self.job_type,
      'duration': self.duration,
      'location': self.location,
      'salary': self.salary,
      'culture': self.culture,
      'inclusivity': self.inclusivity,
      'facilities': self.facilities,
      'workload': self.workload,
      'perks': self.perks,
      'opps': self.opps,
      'mentors': self.mentors,
      'purpose': self.purpose,
      'min_visible': self.min_visible,
      'show_immediate': self.show_immediate,
      'review_text': self.review_text,
    }
