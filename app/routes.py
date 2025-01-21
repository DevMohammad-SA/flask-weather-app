from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   url_for)

from api_request import WeatherApi

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    city = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_status = WeatherApi(city)
        weather_status.get_weather()

    return render_template('home.html', city=city, weather_status=weather_status)
