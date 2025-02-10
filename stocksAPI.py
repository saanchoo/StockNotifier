import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")

def get_stock_change(crypto_symbol, market_currency="USD"):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={crypto_symbol}&market={market_currency}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json().get("Time Series (Digital Currency Daily)", {})

    try:
        dates = sorted(data.keys(), reverse=True)[:2]  # Últimos 2 días de datos disponibles
        close_yesterday = float(data[dates[0]]["4a. close (USD)"])
        close_before = float(data[dates[1]]["4a. close (USD)"])
        change = ((close_yesterday - close_before) / close_before) * 100
        up_down = "🔺" if change > 0 else "🔻"
        return round(change, 2), up_down
    except (IndexError, KeyError):
        print("⚠️ No se encontraron datos recientes para", crypto_symbol)
        return 0, ""
