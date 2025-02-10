# This file contains the logic to get the news
import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

# Cargamos las variables entorno
load_dotenv()

# Asignamos las variables de entorno a variables del sistema

news_api = NewsApiClient(api_key= os.getenv("NEWS_API_KEY"))


# /v2/top-headlines
top_headlines = news_api.get_top_headlines(
        q='crypto',
        category='business',
        country='us',
        language='en')

def form_message():
    # /v2/top-headlines/sources
    sources = news_api.get_sources()

    title = top_headlines["articles"][0]["title"].split("-")[0]
    description = top_headlines["articles"][0]["description"]

    content = f"Title: {title}\n\n {description}"

    return content
