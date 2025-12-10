import requests
from datetime import datetime, timedelta
import json

# ------------------------------------
# LOAD CONFIG.JSON
# ------------------------------------
with open("config.json", "r") as f:
    cfg = json.load(f)

# Extract API keys & URLs
NEWS_DATA_API = cfg["NEWSDATA_API_KEY"]
NEWS_DATA_URL = cfg["NEWSDATA_BASE_URL"]

NEWS_API_KEY = cfg["NEWS_API_KEY"]
NEWS_API_URL = cfg["NEWS_API_URL"]


# ------------------------------------
# LATEST NEWS (NewsData.io)
# ------------------------------------
def get_latest_news(query="india"):
    url = NEWS_DATA_URL.replace("{NEWSDATA_API_KEY}", NEWS_DATA_API).replace("{query}", query)

    res = requests.get(url).json()
    articles = []

    if "results" in res:
        for item in res["results"]:
            articles.append({
                "source": "NewsData.io",
                "title": item.get("title"),
                "link": item.get("link")
            })
    return articles


# ------------------------------------
# LATEST NEWS (NewsAPI.org)
# ------------------------------------
def get_latest_news_newsapi(query="india"):
    url = NEWS_API_URL.replace("{NEWS_API_KEY}", NEWS_API_KEY).replace("{query}", query)

    res = requests.get(url).json()
    articles = []

    if "articles" in res:
        for item in res["articles"]:
            articles.append({
                "source": "NewsAPI.org",
                "title": item.get("title"),
                "link": item.get("url")
            })
    return articles


# ------------------------------------
# PAST 30 DAYS NEWS (NewsAPI.org)
# ------------------------------------
def get_past_news(keyword, days=30):
    url = "https://newsapi.org/v2/everything"
    
    today = datetime.today()
    from_date = (today - timedelta(days=days)).strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')
    
    params = {
        "q": keyword,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY
    }
    
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("❌ ERROR:", response.json().get("message"))
        return []

    data = response.json()
    return data.get("articles", [])



