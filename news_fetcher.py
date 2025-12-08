import requests
from datetime import datetime, timedelta
 
NEWS_DATA_API = "pub_2495123ea5c1484488db3c1dbd8eb5af"
NEWS_API_KEY = "86050229de694186a0a1400ddf054f84"
 
 
# ------------------------------------
# LATEST NEWS (NewsData.io)
# ------------------------------------
def get_latest_news(query="india"):
    url = f"https://newsdata.io/api/1/news?apikey={NEWS_DATA_API}&q={query}&language=en"
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
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
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
# PAST 30 DAYS NEWS (Newsapi.org)
# ------------------------------------
def get_past_news(keyword, days=30):
    """Returns news from the past 'days' based on search keyword."""
   
    url = "https://newsapi.org/v2/everything"
   
    today = datetime.today()
    from_date = (today - timedelta(days=days)).strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')
   
    params = {
        "q": keyword,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "pageSize": 10,         # ⭐ ALWAYS 10 ITEMS
        "apiKey": NEWS_API_KEY
    }
   
    response = requests.get(url, params=params)
 
    if response.status_code != 200:
        print("❌ ERROR:", response.json().get("message"))
        return []
 
    data = response.json()
   
    return data.get("articles", [])
 
# ------------------------------------
# MAIN APP
# ------------------------------------
if __name__ == "__main__":
 
    print("\n🌍 SMART NEWS FETCHER")
    print("======================\n")
 
    # -------- LATEST NEWS ----------
    query = input("Enter keyword for latest news (Ex: India, Tech, Cricket): ").strip()
 
    latest = get_latest_news(query) + get_latest_news_newsapi(query)
 
    print("\n🔴 Latest Trending Headlines")
    print("----------------------------")
 
    if not latest:
        print("⚠️ No latest news found.")
    else:
        for i, news in enumerate(latest, start=1):
            print(f"{i}. {news.get('title')} [{news.get('source')}]")
 
 
 
    # -------- PAST NEWS ----------
    keyword = input("\nEnter keyword for past 30 days news: ").strip()
 
    past = get_past_news(keyword)
 
    print("\n🟡 Past 30 Days News Search")
    print("---------------------------")
 
    if not past:
        print("⚠️ No past news found.")
    else:
        for idx, article in enumerate(past, start=1):
            print(f"{idx}. {article.get('title')}")
   
    print("\n✔️ DONE! Latest + Past news fetched successfully.\n")