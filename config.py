#!/usr/bin/python3

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "7,OP2u'o8Q-'|wl-x8zC_*Pa"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False