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

# App Declaration
app = Flask(__name__)
CORS(app)

app.secret_key = 'Hackbeanpot 2018'

# API Routes
app.register_blueprint(example_api, url_prefix='/api/test')
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(review_api, url_prefix='/api/review')

# Startup
if __name__ == "__main__":
  database_uri = 'sqlite:///app/local_db.db'
  session_manager.setup(database_uri)

  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
