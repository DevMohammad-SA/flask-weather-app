from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   url_for)

from api_request import WeatherApi

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    city = None
    weather_status = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_status = WeatherApi(city)
            if not weather_status.get_weather():
                flash("Unable to fetch weather data. Please try again.", "error")
                weather_status = None
    else:
        weather_status = None

    return render_template('home.html', city=city, weather_status=weather_status)
