# Flask
from flask import Blueprint, request, jsonify

from app.api.utils import *

from app.api.database import session_manager

# API Declaration
# Path: /api
example_api = Blueprint('example_api', __name__)

#############################################
# Staff Creation
#############################################

@example_api.route('/test', methods=['GET'])
def test():
  return 'Hello API', status.HTTP_200_OK