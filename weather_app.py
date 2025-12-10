import requests
import json

# ------------------------------------
# LOAD CONFIG (optional but safe)
# ------------------------------------
try:
    with open("config.json", "r") as f:
        cfg = json.load(f)
except FileNotFoundError:
    cfg = {}

# ------------------------------------
# API DETAILS
# ------------------------------------
WEATHER_API_KEY = "0deb9548231b4c98ba080146250412"
WEATHER_BASE_URL = "http://api.weatherapi.com/v1/current.json"

# ------------------------------------
# WEATHER FUNCTION
# ------------------------------------
def get_weather(city):
    try:
        url = f"{WEATHER_BASE_URL}?key={WEATHER_API_KEY}&q={city},India&aqi=no"
        response = requests.get(url, timeout=10)
        data = response.json()

        if "error" in data:
            return "❌ City not found!"

        return {
            "City": data["location"]["name"],
            "Temperature": f"{data['current']['temp_c']}°C",
            "Feels Like": f"{data['current']['feelslike_c']}°C",
            "Humidity": f"{data['current']['humidity']}%",
            "Weather": data["current"]["condition"]["text"],
            "Wind Speed": f"{data['current']['wind_kph']} kph"
        }

    except Exception as e:
        return f"❌ Error: {e}"

# ------------------------------------
# RUN CODE ✅ (IMPORTANT)
# ------------------------------------
if __name__ == "__main__":
    city = input("Enter city name: ")
    result = get_weather(city)
    print("\n🌦 Weather Details:")
    print(result)
