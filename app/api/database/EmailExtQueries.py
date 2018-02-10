from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.EmailExtModel import EmailExt


def create_email_ext(db, body):
  domain = body['domain']
  school_id = body['school_id']
  email_ext = EmailExt(domain, school_id)

  try:
    db.add(email_ext)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def delete_email_ext(db, body, email_ext_id):
  try:
    db.query(EmailExt).filter(EmailExt.id == email_ext_id).delete()
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  return True

def get_email_exts(db, school_id):
  return db.query(EmailExt).filter(EmailExt.school_id == school_id).all()

def get_email_from_ext(db, domain):
    return db.query(EmailExt).filter(EmailExt.domain == domain).first()
