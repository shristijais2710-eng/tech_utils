import requests
import pandas as pd

API_KEY = "LUNWS9A7PBOACY5Z"

def get_stock_data(symbol):
    url = (
        "https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_DAILY_ADJUSTED"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        return "❌ Invalid symbol or API limit reached"

    df = pd.DataFrame.from_dict(
        data["Time Series (Daily)"],
        orient="index"
    )

    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    return df.sort_index()

def filter_stock_data(df, timeframe):
    if timeframe == "weekly":
        return df.resample("W").mean()

    elif timeframe == "monthly":
        return df.resample("M").mean()

    elif timeframe == "yearly":
        return df.resample("Y").mean()

    else:
        return "❌ Invalid filter (weekly / monthly / yearly)"

def stock_analysis(df):
    return {
        "Average Close Price": round(df["4. close"].mean(), 2),
        "Highest Price": round(df["2. high"].max(), 2),
        "Lowest Price": round(df["3. low"].min(), 2),
        "Total Volume": int(df["6. volume"].sum())
    }
