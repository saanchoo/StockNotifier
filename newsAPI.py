import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_api = NewsApiClient(api_key=NEWS_API_KEY)

def get_news(company_name):
    articles = news_api.get_top_headlines(q=company_name, category="business", language="en", country="us")["articles"]
    return [{"title": article["title"], "description": article["description"]} for article in articles[:3]]
