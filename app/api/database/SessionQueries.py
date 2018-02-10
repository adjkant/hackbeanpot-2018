from app.api.database.models.SessionModel import Session

from sqlalchemy.exc import SQLAlchemyError

def create_session(db, user_id):
  session = Session(user_id)

  try:
    db.add(session)
    db.commit()
  except SQLAlchemyError as e:
    db.rollback()
    return None

  return session

def delete_session(db, session):
  try:
    db.delete(session)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def session_by_token(db, token):
  q = db.query(Session).filter(Session.token == token).first()
  return q