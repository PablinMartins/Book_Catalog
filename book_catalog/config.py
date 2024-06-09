import os
from flask import abort

class Config:
    try:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'mysql+mysqlconnector://root:pablo123@localhost:3306/books'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    except Exception as e:
        abort(500)
