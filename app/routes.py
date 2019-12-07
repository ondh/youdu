from flask import render_template, request
from app import app, data

@app.route('/')
@app.route('/index')
def index():
  soul = data.get()
  return render_template('index.html', soul=soul[1])


@app.route('/init')
def init():
  data.init()
  soul = data.get()
  return render_template('index.html', soul=soul[1])

@app.route('/add', methods=['GET', 'POST'])
def add():
  soul = request.form['soul']
  data.add(soul)
  return render_template('index.html', soul=soul)