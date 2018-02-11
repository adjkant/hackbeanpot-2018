# Flask
from flask import Blueprint, request, jsonify
from flask_api import status

from app.api.utils import get_logged_in_user, validate_json, serialize_all
from app.api.database import session_manager
import app.api.database.CompanyQueries as CompanyQueries

company_api = Blueprint('company_api', __name__)

@company_api.route('/create', methods=['POST'])
@validate_json(['name'])
def create_company():
  db = session_manager.new_session()
  body = request.get_json()

  user = get_logged_in_user(db, request)
  if user:
    if CompanyQueries.create_company(db, body):
        return "", status.HTTP_200_OK
    else:
        return "", status.HTTP_500_INTERNAL_SERVER_ERROR
  else:
    return "", status.HTTP_401_UNAUTHORIZED


@company_api.route('/<int:company_id>/edit', methods=['PUT'])
def edit_company(company_id):
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if CompanyQueries.edit_company(db, body, company_id):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@company_api.route('/delete', methods=['DELETE'])
def delete_company():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  if CompanyQueries.delete_company(db, body):
    return "", status.HTTP_200_OK
  else:
    return "", status.HTTP_400_BAD_REQUEST

@company_api.route('/<int:company_id>', methods=['GET'])
def get_company(company_id):
  db = session_manager.new_session()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  company = CompanyQueries.get_company(db, company_id)
  if company:
    return jsonify(company.serialize), status.HTTP_200_OK
  else:
    return "", status.HTTP_404_NOT_FOUND

@validate_json(['name'])
@company_api.route('/search', methods=['POST'])
def search_job_title():
  db = session_manager.new_session()
  body = request.get_json()
  user = get_logged_in_user(db, request)
  if not user:
    return "", status.HTTP_401_UNAUTHORIZED

  companies = CompanyQueries.get_like_name(db, body['name'])
  if not companies:
    return "", status.HTTP_401_UNAUTHORIZED
  return jsonify(serialize_all(companies)), status.HTTP_200_OK
