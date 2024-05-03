from flask import render_template, request

from web2024 import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<string:id>')
def profile(id):
    return render_template('profile/'+id+'/index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_post():
    '''
    まずパスワードで認証する
    ユーザーがアップロードしたファイルを受け取り、templates/profile/<userid>以下に保存する
    useridとファイルはフォームから取得する
    '''
