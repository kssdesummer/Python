from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
from time import time, sleep

# render_template 调用页面的包,使用时要在同级文件夹里创建一个 templates文件夹,将网页写进去
# 实例化对象
app = Flask(__name__)
'''
# 登陆限制
limiter = Limiter(
    app,
    key_func=get_remote_address,   #根据访问者的IP记录访问次数
    default_limits=["20 per day", "5 per hour"]  #默认限制，一天最多访问20次，一小时最多访问5次
)
'''


# 设置路由
@app.route('/')
def index():  # 函数名可以自定义
    return '设置路由页面'


# 返回字符串
@app.route('/hello')
def hello():
    return '<h1>你好hello页面</h1>'


# 返回一个网页
@app.route('/page')
def page():
    '''
    使用的时候必须先导入包render_template
    传参,参数必须是要返回的文件名
    py文件同级目录下创建templates文件夹放入所有的html文件
    :return:
    '''
    return render_template('1.html')


# get请求带参数
@app.route('/msg')
def msg():
    # 接受用户发送的数据
    # request 请求
    uname = request.values['name']
    print(uname)
    return 'ok'


# post 请求带参数
@app.route('/posts', methods=['POST'])
def posts():
    # 接受用户发送的数据
    # request 请求
    return 'ok'


@app.route('/msgposts', methods=['POST'])
def msgposts():
    # 接受用户发送的数据
    # request 请求
    data = request.values.to_dict()
    evl = json.dumps(data)
    # return 只能返回字符串或者json
    return evl


@app.route('/ajax', methods=['post', 'get'])
def ajax():
    gooinfo = request.values.to_dict()
    sleep(4)
    return json.dumps(gooinfo)


if __name__ == "__main__":
    # 开启调试模式,及自动重启
    # port指定端口号
    # host 指定ip,0.0.0.0用来监听所有的ip
    app.run(debug=True, port=8088, host='0.0.0.0')
