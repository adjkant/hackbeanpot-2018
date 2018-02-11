# Flask
from flask import Blueprint, request, jsonify, make_response

from app.api.utils import *

from app.api.database import session_manager

from flask import redirect

import app.api.database.UserQueries as UserQueries
import app.api.database.SessionQueries as SessionQueries
import app.api.database.SchoolQueries as SchoolQueries
import app.api.database.ReviewQueries as ReviewQueries
import app.api.database.EmailExtQueries as EmailExtQueries

user_api = Blueprint("user_api", __name__)

@user_api.route('/create', methods=['POST'])
@validate_json(['first', 'last', 'email', 'password', 'school'])
def create_user():
  db = session_manager.new_session()
  body = request.get_json()

  school = SchoolQueries.get_by_name(db, body['school'])
  if school:
    body['school_id'] = school.id
  else:
    school_info = {'name': body['school']}
    SchoolQueries.create_school(db, school_info)
    school = SchoolQueries.get_by_name(db, body['school'])
    print('=> Created new School: ', school.name)
    body['school_id'] = school.id
    ext = {'domain': body['email'].split('@')[1],
           'school_id': school.id}
    EmailExtQueries.create_email_ext(db, ext)

  user_created, error = UserQueries.create_user(db, body)

  if user_created:
    # Log In User
    session = login_user_utility(db, body['email'], body['password'])
    response = jsonify(success=True)
    response.set_cookie('sessionToken', session.token)
    return response, status.HTTP_200_OK
  else:
    if error == 'Duplicate Field':
      return jsonify(dict(success=False, error=3)), status.HTTP_200_OK
    else:
      return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@user_api.route('/edit', methods=['PUT'])
def edit_user():
  db = session_manager.new_session()

  # Validate user editing is current user
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  body = request.get_json()

  if UserQueries.edit_user(db, user.id, body):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@user_api.route('/delete', methods=['DELETE'])
def delete_user():
  db = session_manager.new_session()

  # Validate user deleting is current user
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if UserQueries.delete_user(db, user.id):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@user_api.route('/get', methods=['GET'])
def get_user():
  db = session_manager.new_session()

  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return jsonify(user.serialize), status.HTTP_200_OK

@user_api.route('/reviews', methods=['GET'])
def get_reviews():
  db = session_manager.new_session()

  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED
  else:
    reviews = ReviewQueries.get_reviews_filtered(db, {}, user.id)
    if reviews:
      return jsonify(serialize_all(reviews)), status.HTTP_200_OK
    else:
      return "", status.HTTP_404_NOT_FOUND


@user_api.route('/login', methods=['POST'])
@validate_json(['email', 'password'])
def login_user():
  db = session_manager.new_session()
  body = request.get_json()

  # Log in user
  session = login_user_utility(db, body['email'], body['password'])

  # Bad Email / Password
  if not session:
    return "", status.HTTP_401_UNAUTHORIZED

  # Create and send response
  response = jsonify(success=True)
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
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_401_UNAUTHORIZED
