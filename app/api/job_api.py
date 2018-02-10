# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json, serialize_all
from app.api.database import session_manager
import app.api.database.JobQueries as JobQueries

job_api = Blueprint('job_api', __name__)

@job_api.route('/create', methods=['POST'])
@validate_json(['title', 'company_id'])
def create_job():
  db = session_manager.new_session()
  body = request.get_json()

  # If not logged in, return unauthorized
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if JobQueries.create_job(db, body):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@job_api.route('/delete', methods=['DELETE'])
def delete_job():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if JobQueries.delete_job(db, body):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_400_BAD_REQUEST

@job_api.route('/<int:job_id>', methods=['GET'])
def get_job(job_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  job = JobQueries.get_job(db, job_id)
  if job:
    return jsonify(job.serialize()), status.HTTP_200_OK
  else:
    return "", status.HTTP_404
