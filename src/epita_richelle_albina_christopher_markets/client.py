# src/epita_richelle_albina_christopher_markets/client.py
import requests
from epita_richelle_albina_christopher_markets.config import config

def fetch_live_data(symbol: str = "NVDA") -> dict:
    config.validate()
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}"
    headers = {"X-Finnhub-Token": config.api_key}
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return {
        "status": "LIVE_SUCCESS",
        "symbol": symbol,
        "current_price": data.get("c"),
        "high_of_the_day": data.get("h"),
        "low_of_the_day": data.get("l"),
        "previous_close": data.get("pc")
    }