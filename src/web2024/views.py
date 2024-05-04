from flask import render_template, request
import os
import sys
import werkzeug

from web2024 import app
from web2024.config import UPLOAD_DIR


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile/<string:id>")
def profile(id):
    return render_template("profile/" + id + "/index.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_post():
    """
    まずパスワードで認証する
    ユーザーがアップロードしたファイルを受け取り、templates/profile/<userid>以下に保存する
    useridとファイルはフォームから取得する
    """
    print("get request")
    # if request.form['password'] != 'password':
    #     return 'password is wrong'

    userid = request.form["userid"]

    # ファイルを取得
    html_list = request.files.getlist("html")
    css_list = request.files.getlist("css")
    image_list = request.files.getlist("image")

    print(html_list)
    print(css_list)
    print(image_list)

    # アップロード先のディレクトリを作成
    upload_dir = os.path.join(UPLOAD_DIR, userid)
    try:
        os.makedirs(upload_dir)
    except FileExistsError:
        pass

    try:
        os.makedirs(os.path.join(upload_dir, "css"))
    except FileExistsError:
        pass

    try:
        os.makedirs(os.path.join(upload_dir, "image"))
    except FileExistsError:
        pass

    # ファイルを保存
    for html in html_list:
        filename = html.filename
        if filename == "":
            continue
        if not filename.endswith(".html"):
            return "file is not html"
        html.save(os.path.join(UPLOAD_DIR, userid, filename))

    for css in css_list:
        filename = css.filename
        if filename == "":
            continue
        if not filename.endswith(".css"):
            return "file is not css"
        css.save(os.path.join(UPLOAD_DIR, userid, "css", filename))

    for image in image_list:
        filename = image.filename
        if filename == "":
            continue
        if (
            not filename.endswith(".png")
            and not filename.endswith(".jpg")
            and not filename.endswith(".jpeg")
        ):
            return "file is not image"
        image.save(os.path.join(UPLOAD_DIR, userid, "image", filename))

    return render_template("uploaded.html", uploaded_url="/profile/" + userid)


@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def handle_over_max_file_size(error):
    print("werkzeug.exceptions.RequestEntityTooLarge")
    return "result : file size is overed."
