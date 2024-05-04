from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Add additional fields as needed

class Town(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    timezone = db.Column(db.String(100))
    temperature = db.Column(db.Float)
    weather_condition = db.Column(db.String(100))
    checks = db.relationship('Check', backref='town', lazy=True)

class Check(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    town_id = db.Column(db.Integer, db.ForeignKey('town.id'), nullable=False)
    check_time = db.Column(db.DateTime, default=datetime.utcnow)