from datetime import datetime
from app import db, login_manager # Getting database and login manager classes
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    # Function to have LoginManager manage sessions for us
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): # Creating class User which inherits from db.model and UserMixin
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