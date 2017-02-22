from www import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build')
def builder():
    return render_template('build.html')

@app.route('/train')
def trainer():
    return render_template('train.html', network_name=request.args.get("network") or None)