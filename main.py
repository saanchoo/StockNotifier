# main.py
from stocksAPI import get_stock_change
from newsAPI import get_news
from whatsapp import send_whatsapp_message

# Crypto a seguir
STOCK = "BTC"
COMPANY_NAME = "Bitcoin"



# Obtenemos el cambio del Bitcoin
stock_change, up_down = get_stock_change(STOCK)

# Comprobamos si se ha obtenido un cambio válido
if stock_change != 0:
    if abs(stock_change) >= 0:
        articles = get_news(COMPANY_NAME)
        if articles:  # Comprobamos si se han obtenido artículos
            for article in articles:
                message = f"{STOCK}: {up_down}{abs(stock_change)}%\n"
                message += f"Headline: {article['title']}\nBrief: {article['description']}"
                send_whatsapp_message(message)
                print("✅ Mensaje enviado.")
        else:
            print(f"⚠️ No se encontraron noticias relevantes para {COMPANY_NAME}.")
    else:
        print(f"📉 La variación de {STOCK} es menor al 5% ({stock_change}%). No se envían noticias.")
else:
    print(f"⚠️ No se pudo obtener el cambio para {STOCK}.")
