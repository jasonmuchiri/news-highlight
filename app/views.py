from flask import render_template
from app import app

@app.route('/')
def index():

    title = 'Home - Welcome to the best News Highlight website online'
    return render_template('index.html',title = title)