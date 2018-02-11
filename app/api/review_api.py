# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json, serialize_all
from app.api.database import session_manager
import app.api.database.ReviewQueries as ReviewQueries
import app.api.database.CompanyQueries as CompanyQueries
import app.api.database.JobQueries as JobQueries

review_api = Blueprint('review_api', __name__)

def get_or_create_company(db, company_name):
  company = CompanyQueries.get_by_name(db, company_name)
  if company:
    return company.id
  else:
    print("=> Creating company:", company_name)
    return CompanyQueries.create_company(db, {'name': company_name})


def get_or_create_job(db, title, company_id):
  job = JobQueries.get_by_info(db, title, company_id)
  if job:
    return job.id
  else:
    print("=> Creating Job:", title, "for company: ", company_id)
    return JobQueries.create_job(db, {'title': title,
                                      'company_id': company_id})

review_fields = ['job_type',
                 'duration',
                 'location',
                 'salary',
                 'ratings',
                 'title',
                 'company',
                 'min_visible',
                 'show_immediate',
                 'review_text']

@review_api.route('/create', methods=['POST'])
@validate_json(review_fields)
def create_review():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    body['user_id'] = user.id
    body['school_id'] = user.school_id

    if 'company_id' not in body:
      company_id = get_or_create_company(db, body['company'])
      body['company_id'] = company_id
    if 'job_id' not in body:
      job_id = get_or_create_job(db, body['title'], company_id)
      body['job_id'] = job_id

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
  if not reviews:
    return "", status.HTTP_401_UNAUTHORIZED
  return jsonify(serialize_all(reviews)), status.HTTP_200_OK
