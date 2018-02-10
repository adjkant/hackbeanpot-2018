# Flask
from flask import Blueprint
from flask_api import status

# API Declaration
# Path: /api
example_api = Blueprint('example_api', __name__)

#############################################
# Staff Creation
#############################################

@example_api.route('/test', methods=['GET'])
def test():
  return 'Hello API', status.HTTP_200_OK
