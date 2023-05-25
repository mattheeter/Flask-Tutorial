# Need to go to this path: C:\Users\matth\OneDrive - University of Cincinnati\Coding\Environments\flask_tutorial_env\Scripts
# then choose the python application with the dark background to get venv to work

# Importing the Flask class and the render template function (used to add html templates to the pages)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiating a Flask class called app to act as our WSGI (Web Server Gateway Interface)
# __name__ is a variable that stores the name of the module, tells flask where to look for templates, static files, etc.
# If script is run with Python directly, __name__ == __main__
app = Flask(__name__)

app.config["SECRET_KEY"] = "94b0d2b2264bdab0bb38cb91ce256007"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # Setting location of our database, "///" specify that database
                                                            # will be created in current directory
db = SQLAlchemy(app) # Instantiating a data base

from app import routes