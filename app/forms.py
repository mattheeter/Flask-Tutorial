from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
# Fields useful for inputting strings and passwords, submitting, and remembering users
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm): # Class for our login from that inherits from FlaskForm
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")