from dotenv import load_dotenv
import os
import requests
import datetime as dt

# Obtener la fecha actual
now = dt.datetime.now()
date = str(now).split(" ")[0]
print(f"Fecha actual: {date}")

# Obtener el día de la semana (lunes=0, domingo=6)
weekday = now.weekday()
print(f"Día de la semana (0=Lunes, 6=Domingo): {weekday}")

# Cargar las variables desde .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
stock_api = os.getenv("STOCKS_API_KEY")

# Verificar si es fin de semana (sábado=5, domingo=6)
if weekday == 5 or weekday == 6:  # Sábado o Domingo
    print("El mercado está cerrado. No se puede obtener información de la acción.")
else:
    # Si no es fin de semana, continuar con la solicitud
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={stock_api}"

    # Realizar la solicitud
    r = requests.get(url)

    # Asegurarse de que la respuesta contenga los datos
    try:
        data = r.json()["Time Series (Daily)"][date]
        print(data)  # Imprime los datos del día
    except KeyError:
        print(f"No se encontraron datos para la fecha {date}. Puede ser que la API no haya actualizado los datos.")
