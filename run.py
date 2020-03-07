"""

File:run.py
Author:wangduoyu
Date:2020-03-02
Connect:854429157@qq.com
Description:

"""
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'westos'
# 初始化flask_bootstrap
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    flash('login success')
    return render_template('index.html')

@app.route('/bbs/')
def bbs():
    return render_template('bbs.html') \

@ app.route('/blog/')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    app.run(port=5005)