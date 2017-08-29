"""
Code used to initialize the app module

PEP8 demands that names of constants should be in all caps.
Pylint, as PEP8, expects module level variables to be "constants".
"""
from flask import Flask

from app import views

# Initialize the app
APP = Flask(__name__, instance_relative_config=True)

# Load the config file
APP.config.from_object('config')

APP.static_folder = 'static'
