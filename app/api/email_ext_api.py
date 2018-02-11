# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json, serialize_all
from app.api.database import session_manager
import app.api.database.EmailExtQueries as EmailExtQueries

email_ext_api = Blueprint('email_ext_api', __name__)

@email_ext_api.route('/create', methods=['POST'])
@validate_json(['domain', 'school_id'])
def create_email_ext():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    if EmailExtQueries.create_email_ext(db, body):
      return "", status.HTTP_200_OK
    else:
      return "", status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return "", status.HTTP_401_UNAUTHORIZED


@email_ext_api.route('/<int:email_ext_id>/delete', methods=['DELETE'])
def delete_email_ext(email_ext_id):
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if EmailExtQueries.delete_email_ext(db, body, email_ext_id):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_400_BAD_REQUEST

@email_ext_api.route('/<int:school_id>', methods=['GET'])
def get_email_ext(school_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  email_exts = EmailExtQueries.get_email_exts(db, school_id)
  if email_exts:
    return jsonify(serialize_all(email_exts)), status.HTTP_200_OK
  else:
    return "", status.HTTP_404_NOT_FOUND

@email_ext_api.route('/find/<domain>', methods=['GET'])
def get_school(domain):
  db = session_manager.new_session()
  email_ext = EmailExtQueries.get_email_from_ext(db, domain)
  if email_ext:
    return jsonify(email_ext.serialize), status.HTTP_200_OK
  else:
    return "", status.HTTP_404_NOT_FOUND
