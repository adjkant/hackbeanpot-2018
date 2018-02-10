from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.SchoolModel import School


def create_school(db, body):
  school = School(body['name'])

  try:
    db.add(school)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def delete_school(db, school_id):
  try:
    db.query(School).filter(School.id == school_id).delete()
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def get_school(db, school_id):
  return db.query(School).filter(School.id == school_id).first()
