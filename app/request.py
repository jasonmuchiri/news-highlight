from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        description = news_item.get('description')

        if news:
            news_object = News(id,title,description)
            news_results.append(news_object)

    return news_results        