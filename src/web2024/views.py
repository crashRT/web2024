from flask import render_template

from web2024 import app

@app.route('/')
def index():
    return render_template('index.html')
