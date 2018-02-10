from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.api.database.models.UserModel import User

def user_by_id(db, user_id):
  q = db.query(User).filter(User.id == user_id).first()
  return q

def user_by_credentials(db, email, password):
  q = db.query(User).filter(User.email == email, User.password == password).first()
  return q

def create_user(db, body):
  new_user = User(body['email'],
          body['password'],
          body['first'],
          body['last'],
          body['school_id'])
  try:
    db.add(new_user)
    db.commit()
  except IntegrityError:
    # Field is duplicate
    db.rollback()
    return False, 'Duplicate Field'
  except SQLAlchemyError:
    db.rollback()
    return False, 'Database Error'

  return True, None

def edit_user(db, user_id, body):
  user = user_by_id(db, user_id)

  if not user:
    return False

  for key, value in body.items():
      setattr(user, key, value)

  try:
    db.commit(user)
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def delete_user(db, user_id):
  user = user_by_id(db, user_id)

  if not user:
    return False

  try:
    db.delete(user)
    db.commit()
  except SQLAlchemyError:
    db.rollback()
    return False

  return True

def get_user(db, user_id):
  return user_by_id(db, user_id)
