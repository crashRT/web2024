from flask import Flask

app = Flask(__name__)
app.config.from_object('web2024.config')

import web2024.views