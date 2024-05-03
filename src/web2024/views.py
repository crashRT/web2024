from flask import render_template

from web2024 import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<string:id>')
def profile(id):
    return render_template('profile/'+id+'/index.html')