import os
from flask import Flask, render_template, jsonify, request
from weather_app import get_weather
from news_fetcher import get_latest_news, get_latest_news_newsapi, get_past_news

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather')
def api_weather():
    city = request.args.get('city', '').strip()
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    result = get_weather(city)
    if isinstance(result, str):
        return jsonify({"error": result}), 400
    
    # Format the response for frontend
    return jsonify({
        "city": result.get("City", ""),
        "country": "",
        "temperature": result.get("Temperature", "").replace("°C", "").strip(),
        "feels_like": result.get("Feels Like", "").replace("°C", "").strip(),
        "condition": result.get("Weather", ""),
        "humidity": result.get("Humidity", "").replace("%", "").strip(),
        "wind_speed": result.get("Wind Speed", "").replace(" kph", "").strip(),
        "pressure": "N/A"
    })

@app.route('/api/news')
def api_news():
    category = request.args.get("category", "general").strip()
    news_list = get_latest_news(category) + get_latest_news_newsapi(category)
    
    
    # Format the response for frontend
    articles = []
    for item in news_list:
        articles.append({
            "title": item.get("title", ""),
            "source": item.get("source", ""),
            "description": item.get("title", ""),
            "url": item.get("link", "#"),
            "published_at": "N/A"
        })
    
    return jsonify({"articles": articles})


@app.route('/api/news/history')
def api_news_history():
    keyword = request.args.get("keyword", '')
    past_news = get_past_news(keyword)
    return jsonify(past_news)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
