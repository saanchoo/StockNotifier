import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STOCKS_API_KEY")
STOCK = "ETH"
MARKET = "USD"

# Comprobar si la clave de la API está cargada
if not API_KEY:
    print("⚠️ No se ha cargado la API_KEY correctamente.")
else:
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={STOCK}&market={MARKET}&apikey={API_KEY}"
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()

        # Imprimir toda la respuesta de la API
        # print("Respuesta completa de la API:")
        # print(data)

        try:
            # Acceder a la serie de datos de la API
            time_series = data.get('Time Series (Digital Currency Daily)', {})

            if time_series:
                # Ordena las fechas y toma las dos primeras
                dates = sorted(time_series.keys(), reverse=True)[:2]

                # Obtener los precios de cierre de los dos días más recientes
                close_yesterday = float(time_series[dates[0]]["4. close"])  # Cambio aquí
                close_before = float(time_series[dates[1]]["4. close"])  # Cambio aquí

                # Calcular el cambio porcentual
                change = ((close_yesterday - close_before) / close_before) * 100

                # Determinar si el cambio es positivo o negativo
                up_down = "🔺" if change > 0 else "🔻"

                # Mostrar la variación
                print(f"Variación de {STOCK} respecto al día anterior: {up_down} {round(change, 2)}%")
            else:
                print("⚠️ No se encontraron datos de series de tiempo para la criptomoneda.")
        except (IndexError, KeyError) as e:
            print(f"⚠️ Error al procesar los datos: {e}")
    else:
        print(f"⚠️ Error en la solicitud de la API. Código de estado: {response.status_code}")
