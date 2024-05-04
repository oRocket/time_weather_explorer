#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "7,OP2u'o8Q-'|wl-x8zC_*Pa"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes, admin_routes

# Define user_loader function for Flask-Login
from app.models import User  # Assuming you have a User model defined

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
