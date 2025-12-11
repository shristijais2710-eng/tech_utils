from flask import Flask, render_template, jsonify, request
from weather_app import get_weather
from news_fetcher import get_latest_news, get_latest_news_newsapi, get_past_news

app = Flask(__name__, static_folder="static", template_folder="templates")


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")


# -------------------------
# WEATHER API ROUTE
# -------------------------
@app.route("/api/weather")
def api_weather():
    city = request.args.get("city", "").strip()

    # City blank?
    if not city:
        return jsonify({"error": "City name is required"}), 400

    # Fetch data from weather app
    result = get_weather(city)

    # Strict validation to block WeatherAPI fuzzy matches
    if (
        not result or
        isinstance(result, str) or
        "City" not in result or
        result.get("City", "").lower() != city.lower()   # 🔥 main fix
    ):
        return jsonify({"error": "City not found"}), 404

    # Valid response → format and return
    return jsonify({
        "city": result.get("City", ""),
        "country": "India",
        "temperature": result.get("Temperature", "").replace("°C", ""),
        "feels_like": result.get("Feels Like", "").replace("°C", ""),
        "condition": result.get("Weather", ""),
        "humidity": result.get("Humidity", "").replace("%", ""),
        "wind_speed": result.get("Wind Speed", "").replace(" kph", ""),
        "pressure": "N/A"
    })


# -------------------------
# LATEST NEWS API ROUTE
# -------------------------
@app.route("/api/news")
def api_news():
    category = request.args.get("category", "general").strip()

    news_list = []
    news_list.extend(get_latest_news(category))
    news_list.extend(get_latest_news_newsapi(category))

    if not news_list:
        return jsonify({"error": "No news found"}), 404

    articles = []
    for item in news_list:
        articles.append({
            "title": item.get("title", ""),
            "source": item.get("source", ""),
            "description": item.get("title", ""),
            "url": item.get("link") or item.get("url") or "#",
            "published_at": "N/A"
        })

    return jsonify({"articles": articles})


# -------------------------
# PAST NEWS HISTORY
# -------------------------
@app.route("/api/news/history")
def api_news_history():
    keyword = request.args.get("keyword", "").strip()

    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    history = get_past_news(keyword)
    return jsonify(history)


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
