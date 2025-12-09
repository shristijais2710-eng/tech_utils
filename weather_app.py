import requests
import json

# ------------------------------------
# LOAD CONFIG
# ------------------------------------
with open("config.json", "r") as f:
    cfg = json.load(f)

WEATHER_API_KEY = cfg["WEATHER_API_KEY"]
WEATHER_BASE_URL = cfg["WEATHER_BASE_URL"]


# ------------------------------------
# WEATHER FUNCTION
# ------------------------------------
def get_weather(city):
    # Build URL from config
    url = f"{WEATHER_BASE_URL}?key={WEATHER_API_KEY}&q={city},india&aqi=no"

    response = requests.get(url)
    data = response.json()

    # If city not found
    if "error" in data:
        return "City not found!"

    weather = {
        "City": data["location"]["name"],
        "Temperature": f"{data['current']['temp_c']}°C",
        "Feels Like": f"{data['current']['feelslike_c']}°C",
        "Humidity": f"{data['current']['humidity']}%",
        "Weather": data['current']['condition']['text'],
        "Wind Speed": f"{data['current']['wind_kph']} kph"
    }

    return weather


# ------------------------------------
# TESTING
# ------------------------------------
if _name_ == "_main_":
    city_name = input("Enter city name: ")
    result = get_weather(city_name)

    print("\nReal-Time Weather:")
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(f"{key}: {value}")