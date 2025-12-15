from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
COINGECKO = "https://api.coingecko.com/api/v3"

@app.route("/")
def home():
    return render_template("crypto.html")

@app.route("/api/prices")
def api_prices():
    coin = request.args.get("coin", "bitcoin")
    days = request.args.get("days", "1")

    # Chart data
    url_chart = f"{COINGECKO}/coins/{coin}/market_chart"
    params_chart = {"vs_currency": "usd", "days": days}

    # Current, high, low data
    url_current = f"{COINGECKO}/coins/markets"
    params_current = {"vs_currency": "usd", "ids": coin}

    try:
        # Fetch chart
        r_chart = requests.get(url_chart, params=params_chart, timeout=10)
        r_chart.raise_for_status()
        chart_data = r_chart.json().get("prices", [])

        # Fetch current/high/low
        r_current = requests.get(url_current, params=params_current, timeout=10)
        r_current.raise_for_status()
        current_json = r_current.json()
        if not current_json:
            current_data = {"current_price": 0, "high_24h": 0, "low_24h": 0}
        else:
            current_data = current_json[0]
            # Safely get keys
            current_data = {
                "current_price": current_data.get("current_price", 0),
                "high_24h": current_data.get("high_24h", 0),
                "low_24h": current_data.get("low_24h", 0)
            }

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Process chart data safely
    labels, prices = [], []
    for item in chart_data:
        if len(item) != 2:
            continue  # skip malformed entries
        ts, price = item
        if ts < 1e12:
            ts *= 1000
        time_str = datetime.utcfromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M")
        labels.append(time_str)
        prices.append(price)

    return jsonify({
        "labels": labels,
        "prices": prices,
        "last_fetched": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "current_price": current_data["current_price"],
        "high_24h": current_data["high_24h"],
        "low_24h": current_data["low_24h"]
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



