from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def index():
    return render_template('contato.html')

@app.route('/contato')
def index():
    return render_template('contato.html')