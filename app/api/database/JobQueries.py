from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.JobModel import Job


def create_job(db, body):
  title = body['title']
  company_id = body['company_id']
  job = Job(title, company_id)

  try:
    db.add(job)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def delete_job(db, body):
  try:
    db.query(Job).filter(Job.id == body['job_id']).delete()
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def get_job(db, job_id):
  return db.query(Job).filter(job.id == job_id).first()


