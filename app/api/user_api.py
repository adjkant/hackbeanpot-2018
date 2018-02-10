# Flask
from flask import Blueprint, request, jsonify, make_response

from app.api.utils import *

from app.api.database import session_manager

from flask import redirect

import app.api.database.UserQueries as UserQueries
import app.api.database.SessionQueries as SessionQueries

user_api = Blueprint("user_api", __name__)

@user_api.route('/create', methods=['POST'])
@validate_json(['first', 'last', 'email', 'password', 'school_id'])
def create_user():
  db = session_manager.new_session()
  body = request.get_json()

  user_created, error = UserQueries.create_user(db, body)

  if user_created:
    # Log In User
    session = login_user_utility(db, body['email'], body['password'])
    response = jsonify(dict(success=True))
    response.set_cookie('sessionToken', session.token)
    return response, status.HTTP_200_OK
  else:
    if error == 'Duplicate Field':
      return jsonify(dict(success=False, error=3)), status.HTTP_200_OK
    else:
      return RESPONSE_DATABASE_ERROR

@user_api.route('/edit', methods=['PUT'])
def edit_user():
  db = session_manager.new_session()

  # Validate user editing is current user
  user = get_logged_in_user(db, request)
  if not user:
    return jsonify('User Not Logged In'), status.HTTP_401_UNAUTHORIZED

  body = request.get_json()

  success = UserQueries.edit_user(db, user.id, body)

  if success:
    return jsonify(dict(success=True)), status.HTTP_200_OK
  else:
    return RESPONSE_DATABASE_ERROR

@user_api.route('/delete', methods=['DELETE'])
def delete_user():
  db = session_manager.new_session()

  # Validate user deleting is current user
  user = get_logged_in_user(db, request)
  if not user:
    return jsonify('User Not Logged In'), status.HTTP_401_UNAUTHORIZED

  success = UserQueries.delete_user(db, user.id)

  if success:
    return status.HTTP_200_OK
  else:
    return RESPONSE_DATABASE_ERROR

@user_api.route('/get', methods=['GET'])
def get_user():
  db = session_manager.new_session()

  user = get_logged_in_user(db, request)
  if not user:
    return jsonify('User Not Logged In'), status.HTTP_401_UNAUTHORIZED

  user = UserQueries.get_user(db, user.id)

  if not user:
    return jsonify(dict(success=False, error='User not found')), status.HTTP_404_NOT_FOUND
  else:
    return jsonify(dict(success=True, body=user.serialize())), status.HTTP_200_OK

@user_api.route('/login', methods=['POST'])
@validate_json(['email', 'password'])
def login_user():
  db = session_manager.new_session()
  body = request.get_json()

  # Log in user
  session = login_user_utility(db, body['email'], body['password'])

  # Bad Email / Password
  if not session:
    return jsonify('User Not Logged In'), status.HTTP_401_UNAUTHORIZED

  # Create and send response
  response = jsonify(dict(success=True))
  response.set_cookie('sessionToken', session.token)
  return response, status.HTTP_200_OK

@user_api.route('/logout', methods=['POST'])
def logout_user():
  db = session_manager.new_session()
  session = get_session(db, request.cookies)

  result = SessionQueries.delete_session(db, session)

  # Create and send response
  response = jsonify(dict(success=True))

  if result:
    response.set_cookie('sessionToken', '', expires=0)

  return response, status.HTTP_200_OK

@user_api.route('/login/check', methods=['POST'])
def check_login():
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if user:
    return jsonify(dict(success=True)), status.HTTP_200_OK
  else:
    return jsonify('User Not Logged In'), status.HTTP_401_UNAUTHORIZED
