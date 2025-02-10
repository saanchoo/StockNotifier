#  Este file sirve para ver si la API funciona

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")
STOCK = "BTC"
MARKET = "USD"

url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={STOCK}&market={MARKET}&apikey={API_KEY}"
response = requests.get(url)
data = response.json()

print(data)  # Muestra toda la respuesta de la API
