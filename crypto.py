import requests

CRYPTO_API = "2540cc6703a5479baf48bc4544878bd0"

# ------------------------------------
# LATEST CRYPTO NEWS (CoinMarketCap)
# ------------------------------------
def get_latest_news(limit=5):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/news"

    headers = {
        "X-CMC_PRO_API_KEY": CRYPTO_API,
        "Accept": "application/json"
    }

    params = {
        "limit": limit
    }

    response = requests.get(url, headers=headers, params=params)
    res = response.json()

    articles = []

    if "data" in res:
        for item in res["data"]:
            articles.append({
                "source": "CoinMarketCap",
                "title": item.get("title"),
                "link": item.get("url")
            })

    return articles


# TEST
if __name__ == "__main__":
    news = get_latest_news()
    for n in news:
        print(n["title"])
        print(n["link"])
        print("-" * 50)
