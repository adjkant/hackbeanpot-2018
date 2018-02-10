# Flask
from flask import request, jsonify
from flask_api import status

# Basics
from functools import wraps

# Response Constants
RESPONSE_DATABASE_ERROR = ('Database Error', status.HTTP_500_INTERNAL_SERVER_ERROR)
RESPONSE_NOT_LOGGED_IN = dict(success=False, error=1)


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

def login_user_utility(email, password):
  db = session_manager.new_session()

  user = UserQueries.user_by_credentials(db, email, password)

  # Bad Email / Password
  if not user:
    return None

  # Return session
  return SessionQueries.create_session(db, user.id)
