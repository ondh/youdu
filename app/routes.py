from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    soul = '蠢也没那么可怕，毕竟水母没有脑子，也活了6亿年。'
    return render_template('index.html', soul=soul)
