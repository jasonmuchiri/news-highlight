from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to the best News Highlight website online'
    return render_template('index.html',title = title,popular = popular_news)