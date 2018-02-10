# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json, serialize_all
from app.api.database import session_manager
import app.api.database.ReviewQueries as ReviewQueries

review_api = Blueprint('review_api', __name__)

@review_api.route('/create', methods=['POST'])
@validate_json(['job_id', 'job_type','duration', 'location'])
def create_review():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    body['user_id'] = user.id
    body['school_id'] = user.school_id

    if ReviewQueries.create_review(db, body):
        return "", status.HTTP_200_OK
    else:
        return "", status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return "", status.HTTP_401_UNAUTHORIZED


@review_api.route('<int:review_id>/edit', methods=['PUT'])
def edit_review(review_id):
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if ReviewQueries.edit_review(db, body, review_id):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@review_api.route('/delete', methods=['DELETE'])
def delete_review():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if ReviewQueries.delete_review(db, body):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_400_BAD_REQUEST

@review_api.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  review = ReviewQueries.get_review(db, review_id)
  if review:
    return jsonify(review), status.HTTP_200_OK
  else:
    return "", status.HTTP_404_NOT_FOUND

@review_api.route('/select', methods=['GET'])
def get_filtered_reviews():
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  reviews = ReviewQueries.get_review_filtered(db, request.args, user.id)
  if reviews == False:
    return "", status.HTTP_401_UNAUTHORIZED
  return jsonify(serialize_all(reviews)), status.HTTP_200_OK
