# Need to go to this path: C:\Users\matth\OneDrive - University of Cincinnati\Coding\Environments\flask_tutorial_env\Scripts
# then choose the python application with the dark background to get venv to work

# Importing the Flask class
from flask import Flask

# Instantiating a Flask class called app to act as our WSGI (Web Server Gateway Interface)
# __name__ is a variable that stores the name of the module, tells flask where to look for templates, static files, etc.
# If script is run with Python directly, __name__ == __main__
app = Flask(__name__)

# Routes are what are typed into browser to go to different pages (home, about, etc.)
# / says this is the root or home page of the website
@app.route("/") # Called a decorator, specifically the route decorator
def home():
    return "<h1>Home Page</h1>"
# Need to run "set FLASK_APP=flaskblog.py" before running - Nevermind, just set the file name to app.py
# To run use: "flask run" - still need to do this - After adding below conditional, just run using typical run button

# Adding an about route
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# Only true when this script is run directly, as stated above
if __name__ == "__main__":
    # Running in debug mode so that changes take effect without restarting web server
    app.run(debug=True)
    

