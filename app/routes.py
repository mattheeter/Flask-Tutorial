from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

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
