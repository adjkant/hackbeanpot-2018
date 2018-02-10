# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json
from app.api.database import session_manager
import app.api.database.SchoolQueries as SchoolQueries

school_api = Blueprint('school_api', __name__)

@school_api.route('/create', methods=['POST'])
@validate_json(['name'])
def create_school():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    if SchoolQueries.create_school(db, body):
        return jsonify(success=True), status.HTTP_200_OK
    else:
        return jsonify(success=False), status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return jsonify(success=False), status.HTTP_401_UNAUTHORIZED

@school_api.route('/delete/<int:school_id>', methods=['DELETE'])
def delete_school(school_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return jsonify(success=False), status.HTTP_401_UNAUTHORIZED

  if SchoolQueries.delete_school(db, school_id):
    return jsonify(success=True), status.HTTP_200_OK
  else:
    return jsonify(success=False), status.HTTP_400_BAD_REQUEST

@school_api.route('/<int:school_id>', methods=['GET'])
def get_school(school_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return jsonify(success=False), status.HTTP_401_UNAUTHORIZED

  school = SchoolQueries.get_school(db, school_id)
  if school:
    return jsonify(school.serialize), status.HTTP_200_OK
