## Ajax

### Ajax定义

​	是与服务器交换数据并更新部分网页的技术,在不冲加载整个页面的情况下,基于js和HTTP请求,,不是一种新的语言而是一种使用现有标准的新方法

通过HTTP请求加载远程数据

​	jQuery底层对AJAX实现进行了封装

​	$.get $.post $.ajax() 返回其创建的XMLHttpRequest对象,多数情况下不需要操作返回的对象

### Flask搭建一个简单的服务

安装Flask库:pip install flask

1.写一个py文件

	1. 导包
 	2. 实例化
 	3. 添加路由
 	4. 绑定函数
 	5. 调用run方法启动
      	1. debug调试模式
      	2. port端口号
      	3. 默认端口5000

2.在浏览器访问 http://127.0.0.1:5000/ 

3.导入js,css时在同级文件夹创建static文件夹

```python
from flask import Flask,render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# render_template 调用页面的包,使用时要在同级文件夹里创建一个 templates文件夹,将网页写进去
# 实例化对象
app = Flask(__name__)

# 导入包设置限制访问次数
limiter = Limiter(
    app,   
    # 根据访问者的IP记录访问次数
    key_func=get_remote_address, 
    # 默认限制，一天最多访问20次，一小时最多访问5次
    default_limits=["20 per day", "5 per hour"] 
)

# 设置路由
@app.route('/')
def index():
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

if __name__ == "__main__":
    # 开启调试模式,及自动重启
    # port指定端口号
    # host 指定ip,0.0.0.0用来监听所有的ip
    app.run(debug=True,port=8088,host='0.0.0.0')
```

在文件存在位置shift+右键打开命令行,运行py文件 python demo.py开启本地服务器



### $.get/$.post

​	格式:   $.get/$.post('url',{uname:'zhang',age:18},function(),’type’)

​				$.get/$.post('请求地址',[发送请求时携带的参数],[回调函数],[指定返回的数据类型])

​				请求地址:请求数据的地址

​				携带的参数:键值对的形式

​				回调函数:请求成功时执行的函数

​				数据类型:默认字符串,可选xml(可以通过选择器直接选择里面的内容),json

### $.ajax

格式:

```js
$.ajax({
	url:"",
    tpye:"POST",	// 默认GET
    data:{name:"liya",age:18},
    dataType:'json',	// 返回数据类型
    success:function(data){
        console.log(data)
    },
    error:function(){},
    timeout:2000,
    async:True,	//默认同步false,异步可以同时进行ajax和别的
})
```



