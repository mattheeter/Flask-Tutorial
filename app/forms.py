from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# Fields useful for inputting strings and passwords, submitting, and remembering users
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User # Importing User class for validation (no duplicate usernames, emails, etc.)

class RegistrationForm(FlaskForm): # Class for our registration from that inherits from FlaskForm
    username = StringField("Username",  # New attribute for inputting strings
                           validators=[DataRequired(),Length(min=2, max=20)])
    # DataRequied ensures data is actually entered, length enforces set length
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", 
                                     validators=[DataRequired(), EqualTo("password")])
    # EqualTo validator ensures confirm_password and password are the same
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        # Error for when username is already taken
        user = User.query.filter_by(username=username.data).first() # Querying database to see if new username already exists
        if user: # If user is not None
            raise ValidationError('That username is taken. Please choose a different one.') # Error message to user
        
    def validate_email(self, email):
        # Error for when email is already taken
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm): # Class for our login from that inherits from FlaskForm
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")