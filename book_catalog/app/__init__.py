from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import abort

try:
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)
except Exception as e:
    abort(500)

from app import routes, models
