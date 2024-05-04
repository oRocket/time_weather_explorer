#!/usr/bin/python3

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import Town
from app.forms import LoginForm, SearchForm
from weather_api import get_weather

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    town = {  # Example town data (replace with actual data)
        'temperature': '20°C',
        'weather_condition': 'Sunny'
    }
    current_user = {'username': 'JohnDoe'}  # Example current user data

    if request.method == 'POST' and form.validate_on_submit():
        # Process the form data (e.g., perform search)
        search_query = form.search_query.data
        # Update the town variable with actual data based on search query
        town = {
            'temperature': '25°C',  # Example temperature
            'weather_condition': 'Cloudy'  # Example weather condition
        }

    return render_template('index.html', form=form, town=town, current_user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Logic for user authentication
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/town/<town_id>')
@login_required
def town_detail(town_id):
    town = Town.query.get(town_id)
    if not town:
        flash('Town not found', 'danger')
        return redirect(url_for('index'))
    
    # Get weather information for the town
    api_key = 'your_openweathermap_api_key'
    temperature, weather_condition = get_weather(api_key, town.name)
    if temperature is not None and weather_condition is not None:
        town.temperature = temperature
        town.weather_condition = weather_condition
        db.session.commit()
    else:
        flash('Failed to retrieve weather information', 'danger')
    
    return render_template('town_detail.html', town=town)

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # Logic to search for towns/cities
        return redirect(url_for('search_results'))
    return render_template('search.html', form=form)

@app.route('/search_results')
@login_required
def search_results():
    # Logic to display search results
    return render_template('search_results.html')