#!/usr/bin/python3

from . import app  # Import the 'app' object from the parent package
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Town, Check
from .forms import AddTownForm, RemoveTownForm, CheckWeatherForm
from weather_api import get_weather

@app.route('/admin/add_town', methods=['GET', 'POST'])
@login_required
def add_town():
    form = AddTownForm()
    if form.validate_on_submit():
        town = Town(name=form.name.data, timezone=form.timezone.data)
        db.session.add(town)
        db.session.commit()
        flash('Town added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('admin/add_town.html', form=form)

@app.route('/admin/remove_town/<int:town_id>', methods=['POST'])
@login_required
def remove_town(town_id):
    town = Town.query.get_or_404(town_id)
    db.session.delete(town)
    db.session.commit()
    flash('Town removed successfully', 'success')
    return redirect(url_for('index'))

@app.route('/admin/check_weather/<int:town_id>', methods=['POST'])
@login_required
def check_weather_admin(town_id):
    town = Town.query.get_or_404(town_id)
    api_key = 'your_openweathermap_api_key'  # Replace with your actual API key
    temperature, weather_condition = get_weather(api_key, town.name)
    if temperature is not None and weather_condition is not None:
        town.temperature = temperature
        town.weather_condition = weather_condition
        db.session.commit()
        flash('Weather information updated successfully', 'success')
    else:
        flash('Failed to retrieve weather information', 'danger')
    return redirect(url_for('index'))