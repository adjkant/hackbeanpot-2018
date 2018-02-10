from sqlalchemy.exc import SQLAlchemyError

from app.api.database.models.ExampleModel import User


def create_message(db, to_id, from_id, subject, message):
  message = User(to_id, from_id, subject, message)
  
  try:
    db.add(message)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  
  return True


def get_messages_to_user(db, user_id):
  q = db.query(User).filter(User.to_id == user_id).all()
  return q


def get_message(db, user_id, message_id):
  q = db.query(User).filter(User.id == message_id, User.to_id == user_id).first()
  return q


def read_message(db, user_id, message_id):
  message = get_message(db, user_id, message_id)
  
  if not message:
    return False
  
  message.read = True
  
  try:
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False
  
  return True
