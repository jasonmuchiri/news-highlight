from flask import render_template
from app import app

@app.route('/news/<int:news_id>')
def index():

    title = 'Home - Welcome to the best News Highlight website online'
    return render_template('index.html',title = title)