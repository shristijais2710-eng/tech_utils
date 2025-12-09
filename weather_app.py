import requests

def get_weather(city):
    api_key = "0deb9548231b4c98ba080146250412"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}.india&aqi=no"

    response = requests.get(url)
    data = response.json()

    # Agar city not found hai
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

city_name = input("Enter city name: ")
result = get_weather(city_name)

print("\nReal-Time Weather:")
if isinstance(result, str):
    print(result)

else:
    for key, value in result.items():
        print(f"{key}: {value}")