from app import app
from flask import render_template
# 导入表单处理方法
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'lhf'}
    posts = [
        {
            'author': {'username':'刘'},
            'body': '这是模板模块中循环的例子~1'
        },
        {
            'author': {'username':'东墙'},
            'body': '这是模板模块中循环的例子~2'
        }
    ]
    return render_template('index.html', title='我的', user=user, posts=posts)

@app.route('/login')
def login():
    # 创建一个表单实例
    form = LoginForm
    return render_template('login.html', title='登录', form=form)