"""
Frontend module for the Flask application.

This module defines a simple Flask application that
serves as the frontend for the project.
"""

from flask import Flask, render_template
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

"""Configuration for the FastAPI backend URL."""
FASTAPI_BACKEND_HOST = 'http://backend'
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class QueryForm(FlaskForm):
    """
    Form class to handle query input from the user.
    """

    destination = StringField('Destination:')
    piscina_checkbox = BooleanField('Swimming pool')
    accesso_disabili_checkbox = BooleanField('Disabled access')
    fitness_checkbox = BooleanField('Fitness corner')
    sauna_checkbox = BooleanField('Sauna')
    aria_condizionata_checkbox = BooleanField('Air conditioning')
    lago_checkbox = BooleanField('Lake')
    submit_field = SubmitField('Search')

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the data from the backend
    return render_template('index.html')