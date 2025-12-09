import requests
import json

def get_weather(city):
    api_key = cfg["WEATHER_API_kEY"]
    url = cfg["weather_BASE_URL"]

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
        "Weather": data["current"]["condition"]["text"],
        "Wind Speed": f"{data['current']['wind_kph']} kph"
    }
    return weather


# For command line testing
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    result = get_weather(city_name)

    print("\nReal-Time Weather:")
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
