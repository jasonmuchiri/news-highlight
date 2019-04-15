from app import app
import urllib.request,json
from .models import news

News = news.News

apiKey = app.config['NEWS_API_KEY']