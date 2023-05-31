# Need to go to this path: C:\Users\matth\OneDrive - University of Cincinnati\Coding\Environments\flask_tutorial_env\Scripts
# then choose the python application with the dark background to get venv to work

# Importing the Flask class and the render template function (used to add html templates to the pages)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager # Class to easily manage logins

# Instantiating a Flask class called app to act as our WSGI (Web Server Gateway Interface)
# __name__ is a variable that stores the name of the module, tells flask where to look for templates, static files, etc.
# If script is run with Python directly, __name__ == __main__
app = Flask(__name__)

app.config["SECRET_KEY"] = "94b0d2b2264bdab0bb38cb91ce256007"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # Setting location of our database, "///" specify that database
                                                            # will be created in current directory
db = SQLAlchemy(app) # Instantiating a data base
bcrypt = Bcrypt(app) # Instantiating a Bcrypt class
login_manager = LoginManager(app) # Instantiating a LoginManager class
login_manager.login_view = 'login' # Telling login_manager where our login page is
login_manager.login_message_category = 'info' # Prettying up alert asking to login

from app import routes