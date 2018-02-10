from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.api.database.models.Base import Base

class School(Base):

	__tablename__ = 'schools'

	id = Column(Integer, primary_key=True, autoincrement=True)

	name = Column(String(80), unique=True)

	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name
		}