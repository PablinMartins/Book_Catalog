from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User
from werkzeug.security import  check_password_hash
from flask import abort

try:
    class BookForm(FlaskForm):
        title = StringField('Title', validators=[DataRequired()])
        author = StringField('Author', validators=[DataRequired()])
        comment = TextAreaField('Comment', validators=[DataRequired()])
        review = SelectField('Review', choices=[('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')], validators=[DataRequired()])
        submit = SubmitField('Submit')

    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
        password = PasswordField('Password', validators=[DataRequired()])

        submit = SubmitField('Sign In')

    class RegistrationForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
        submit = SubmitField('Sign Up')

        def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already taken. Please choose a different one.')
except Exception as e:
    abort(500)  
