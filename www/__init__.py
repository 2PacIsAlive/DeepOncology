from os import environ
from flask import Flask
app = Flask(__name__, static_url_path='')

app.config["GITHUB_SECRET"] = bytes(environ["GITHUB_SECRET"])

import views
import api
import ci