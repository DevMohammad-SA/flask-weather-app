import os

import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherApi:
    def __init__(self, query):
        self.access_key = os.getenv("ACCESS_KEY")
        self.query = query
        self.city = None
        self.weather_descriptions = None
        self.temperature = None
        self.wind_speed = None
        self.humidity = None
        self.is_day = None
        self.weather_icons = None
        self.feels_like = None

    def get_weather(self):
        response = requests.get(
            f"https://api.weatherstack.com/current?access_key={
                self.access_key}&query={self.query}"
        )
        data = response.json()
        self.city = data.get("request", {}).get("query", "Unknown Location")
        self.weather_descriptions = data.get("current", {}).get(
            "weather_descriptions", "N/A"
        )[0]
        self.is_day = data.get("current", {}).get("is_day", "N/A")
        self.weather_icons = data.get("current", {}).get(
            "weather_icons", ["N/A"])[0]
        self.feels_like = f"{
            data.get('current', {}).get('feelslike', 'N/A')} C"
        self.temperature = f"{
            data.get('current', {}).get('temperature', "N/A")} C"
        self.wind_speed = f"{
            data.get('current', {}).get('wind_speed', "N/A")} km/h"
        self.humidity = f"{data.get('current', {}).get('humidity', "N/A")} %"


if __name__ == "__main__":
    app = WeatherApi()
    app.get_weather()
