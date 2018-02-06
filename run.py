# System and Flask
import os
from flask import Flask, send_file

# Database
from app.api.database import session_manager

# API Parts
from app.api.example_api import example_api

# App Declaration
app = Flask(__name__, static_url_path='')
app.secret_key = 'The Modern Citizen'

# API Routes
app.register_blueprint(example_api, url_prefix='/api/test')


# Web Routes
@app.route('/')
def send_app():
  return send_file('static/index.html', cache_timeout=0)


# Startup
if __name__ == "__main__":
  database_uri = 'sqlite:///app/local_db.db'
  session_manager.setup(database_uri)
  
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)