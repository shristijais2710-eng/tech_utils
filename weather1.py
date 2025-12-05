import requests

def get_weather(city):
    api_key = "0deb9548231b4c98ba080146250412"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    # Agar city not found hai
    if "error" in data:
        return "City not found!"

    