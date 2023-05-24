# Need to go to this path: C:\Users\matth\OneDrive - University of Cincinnati\Coding\Environments\flask_tutorial_env\Scripts
# then choose the python application with the dark background to get venv to work

from datetime import datetime
# Importing the Flask class and the render template function (used to add html templates to the pages)
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
# Instantiating a Flask class called app to act as our WSGI (Web Server Gateway Interface)
# __name__ is a variable that stores the name of the module, tells flask where to look for templates, static files, etc.
# If script is run with Python directly, __name__ == __main__
app = Flask(__name__)

app.config["SECRET_KEY"] = "94b0d2b2264bdab0bb38cb91ce256007"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db" # Setting location of our database, "///" specify that database
                                                            # will be created in current directory
db = SQLAlchemy(app) # Instantiating a data base

class User(db.Model): # Creating class User which inherits from db.model
    id = db.Column(db.Integer, primary_key=True) # ID is of integer type and is unique to user (primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg") # User profile picture, not unique
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)
    
    def __repr__(self): # Returns a printable representation of an object
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Using db.DateTime type for type, and datetime for default
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

# Adding dummy data to show how data is passed to the app using list of dictionaries
posts = [
    {
        "author":"Matthew Heeter",
        "title":"Blog Post 1",
        "content":"First post content",
        "date_posted":"May 5, 2023"
    },
    {
        "author":"Jane Doe",
        "title":"Blog Post 2",
        "content":"Second post content",
        "date_posted":"May 6, 2023"
    }
]

# Routes are what are typed into browser to go to different pages (home, about, etc.)
# / says this is the root or home page of the website
@app.route("/") # Called a decorator, specifically the route decorator
@app.route("/home") # Adding second decorator so that you can use both / and /home to go to the home page
def home():
    return render_template("home.html", posts=posts) # Using posts variable to pass data to templates
# Need to run "set FLASK_APP=flaskblog.py" before running - Nevermind, just set the file name to app.py
# To run use: "flask run" - still need to do this - After adding below conditional, just run using typical run button

# Adding an about route
@app.route("/about")
def about():
    return render_template("about.html", title="About") # Passing in title so that default from template's else is not used

@app.route("/register", methods=["GET", "POST"]) # Creating a registration route (for creating accounts)
def register():
    form = RegistrationForm() # Instantiating a RegistrationForm object
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        # If the form is validated, flash a message with the username
        return redirect(url_for("home"))
        # And redirect to the home page 
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            # If the email and password match, allow the login
            flash("You have been logged in!", "success")
            # Flash a message and return home
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)

# Only true when this script is run directly, as stated above
if __name__ == "__main__":
    # Running in debug mode so that changes take effect without restarting web server
    app.run(debug=True)
    

