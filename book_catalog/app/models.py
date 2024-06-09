from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import abort

try:
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(150), nullable=False)
        author = db.Column(db.String(100), nullable=False)
        comment = db.Column(db.Text, nullable=True)
        review = db.Column(db.String(1))
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  

        def __repr__(self):
            return f"Book('{self.title}', '{self.author}', '{self.review}')"

    class User(UserMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(64), index=True, unique=True, nullable=False)
        password_hash = db.Column(db.String(128), nullable=False)
        books = db.relationship('Book', backref='owner', lazy=True)  

        def __repr__(self):
            return '<User {}>'.format(self.username)
        
        def set_password(self, password):
            self.password_hash = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hash, password)
except Exception as e:
    abort(500)  
