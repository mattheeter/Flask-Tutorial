from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt # Importing all the objects we instantiated in app.py
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home')) # If a user is logged in, redirect them to home page if they go to register
    form = RegistrationForm() # Instantiating a RegistrationForm object
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # Getting hashed pw from user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # Creating user object for db
        db.session.add(user) # This line and next adding user to db
        db.session.commit()
        flash(f"Your account has been created! You are now able to login.", "success")
        # If the form is validated, flash a message with the username
        return redirect(url_for("login"))
        # And redirect to the home page 
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) # If a user is logged in, redirect them to home page if they go to login again
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # Querying data base user info
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data) # Logging the user in
            next_page = request.args.get('next') # If accessing login page thru other page (account, etc.), redirect to page trying to access
            return redirect(next_page) if next_page else redirect(url_for('home')) # Home page if no next_page exists
        else:
            flash("Login Unsuccessful. Please check email and password.", "danger") # Message if incorrect credentials
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    # Function to log current_user out
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required # Need to be logged in to access the account route, if '/account' is added to address, will be directed to login page
def account():
    return render_template("account.html", title="Account")