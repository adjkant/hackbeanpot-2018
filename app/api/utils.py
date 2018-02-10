# Flask
from flask import request, jsonify
from flask_api import status

# Basics
from functools import wraps

import app.api.database.UserQueries as UserQueries
import app.api.database.SessionQueries as SessionQueries

from app.api.database import session_manager

# Response Constants
RESPONSE_DATABASE_ERROR = ('Database Error', status.HTTP_500_INTERNAL_SERVER_ERROR)


def validate_json(expected_fields):
  def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
      # This gets cached so that it can be reused after
      body = request.get_json(silent=True)

      # Check valid JSON
      if not body:
        return 'Not JSON', status.HTTP_400_BAD_REQUEST

      for field in expected_fields:
        if field not in body:
          return 'Missing Required Field', status.HTTP_400_BAD_REQUEST

      return func(*args, **kwargs)

    return wrapper
  return decorator

def get_logged_in_user(db, request):
  session = get_session(db, request.cookies)
  if not session or not session.user_id:
    return False
  else:
    user = UserQueries.get_user(db, session.user_id)
    if not user:
      return False
    else:
      return user

def login_user_utility(db, email, password):
  user = UserQueries.user_by_credentials(db, email, password)

  # Bad Email / Password
  if not user:
    return None

  # Return session
  return SessionQueries.create_session(db, user.id)

def get_session(db, cookies):
  if 'sessionToken' not in cookies:
    return None

  session = SessionQueries.session_by_token(db, cookies['sessionToken'])

  if not session:
    return None

  return session

def serialize_all(collection):
  return [i.serialize for i in collection]
