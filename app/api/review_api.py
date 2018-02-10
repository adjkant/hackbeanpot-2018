# Flask
import flask
from flask import Blueprint, request
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json
from app.api.database import session_manager, ReviewQueries

import json

review_api = Blueprint('review_api', __name__)

@review_api.route('/create', methods=['POST'])
@validate_json(['job_id', 'job_type','duration', 'location'])
def create_review():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    body['uid'] = user.id
    body['school_id'] = user.school_id

    if ReviewQueries.create_review(db, body):
        return status.HTTP_200_OK
    else:
        return status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return status.HTTP_401_UNAUTHORIZED


@review_api.route('/edit', methods=['POST'])
def edit_review():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return status.HTTP_401_UNAUTHORIZED

  if ReviewQueries.edit_review(db, body):
    return status.HTTP_200_OK
  else:
    return status.HTTP_500_INTERNAL_SERVER_ERROR

@review_api.route('/delete', methods=['DELETE'])
def delete_review():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return status.HTTP_401_UNAUTHORIZED

  if ReviewQueries.delete_review(db, body):
    return status.HTTP_200_OK
  else:
    return status.HTTP_400_BAD_REQUEST

@review_api.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return status.HTTP_401_UNAUTHORIZED

  review = ReviewQueries.get_review(db, review_id)
  if review:
    response = flask.app.response_class(
      response=json.dumps(review),
      status=200,
      mimetype='application/json'
    )
    return response

@review_api.route('/select', methods=['GET'])
def get_filtered_reviews():
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return status.HTTP_401_UNAUTHORIZED

  reviews = ReviewQueries.get_review_filtered(db, request.args)
  if reviews:
    response = flask.app.response_class(
      response=json.dumps(reviews),
      status=200,
      mimetype='application/json'
    )
    return response
  else:
    return status.HTTP_500_INTERNAL_SERVER_ERROR
