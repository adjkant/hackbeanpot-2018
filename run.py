# System and Flask
import os
from flask import Flask
from flask_cors import CORS

# Database
from app.api.database import session_manager

# API Parts
from app.api.example_api import example_api
from app.api.user_api import user_api
from app.api.review_api import review_api
from app.api.school_api import school_api
from app.api.company_api import company_api
from app.api.email_ext_api import email_ext_api

# App Declaration
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.secret_key = 'Hackbeanpot 2018'

# API Routes
app.register_blueprint(example_api, url_prefix='/api/test')
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(review_api, url_prefix='/api/review')
app.register_blueprint(school_api, url_prefix='/api/school')
app.register_blueprint(company_api, url_prefix='/api/company')
app.register_blueprint(email_ext_api, url_prefix='/api/email-ext')

# Startup
if __name__ == "__main__":
  database_uri = 'sqlite:///app/local_db.db'
  session_manager.setup(database_uri)

  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
