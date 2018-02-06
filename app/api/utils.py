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
