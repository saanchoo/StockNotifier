from stocksAPI import get_stock_change
from newsAPI import get_news
from whatsapp import send_whatsapp_message

STOCK = "BTC"
COMPANY_NAME = "Bitcoin"

# Obtenemos el cambio del Bitcoin
stock_change, up_down = get_stock_change(STOCK)

# Si la variación es >= 5%, obtenemos noticias y enviamos WhatsApp
if abs(stock_change) >= 5:
    articles = get_news(COMPANY_NAME)
    for article in articles:
        message = f"{STOCK}: {up_down}{abs(stock_change)}%\n"
        message += f"Headline: {article['title']}\nBrief: {article['description']}"
        send_whatsapp_message(message)
        print("✅ Mensaje enviado.")
else:
    print(f"📉 La variación de {STOCK} es menor al 1% ({stock_change}%). No se envían noticias.")
