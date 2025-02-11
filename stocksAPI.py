# stocksAPI.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")
STOCK = "BTC"
MARKET = "USD"

# Función para obtener el cambio de la acción
def get_stock_change(stock):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={stock}&market={MARKET}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Imprime toda la respuesta de la API
    # print(data)

    try:
        # Accede a la serie de datos de la API
        time_series = data['Time Series (Digital Currency Daily)']

        # Ordena las fechas y toma las dos primeras
        dates = sorted(time_series.keys(), reverse=True)[:2]

        # Obtén los precios de cierre de los dos días más recientes
        close_yesterday = float(time_series[dates[0]]["4. close"])  # Corregir la clave aquí
        close_before = float(time_series[dates[1]]["4. close"])  # Corregir la clave aquí

        # Calcula el cambio porcentual
        change = ((close_yesterday - close_before) / close_before) * 100

        # Determina si el cambio es positivo o negativo
        up_down = "🔺" if change > 0 else "🔻"

        return change, up_down

    except (IndexError, KeyError) as e:
        print(f"⚠️ Error al obtener datos para {stock}: {e}")
        return 0, None
