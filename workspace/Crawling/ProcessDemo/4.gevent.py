'''
协程相关内容
gevent : 速率比较快
1. 不需要多启动进程或者线程
2. 进程和线程的切换比较耗时
3. 协程不需要cup的切换
4. 使用的是 yeild 实现方式

yeild的两种方式:
1. yeild ***
2. *** = yeild  和send一起使用
'''

import gevent
from gevent import monkey
monkey.patch_all()
# 放在其他的import之后会有警告
import time
import requests

# 猴子补丁,为了实现并发效果
'''
requests分为发送请求和接受返回数据两部分
中间有个时间间隔
目的是为了给requests请求过程中间加一个yeild

'''

def multipro(name):
    '''
    如果程序报错,可尝试在requests里加参数:verity=False
    若requests的请求过多,会占用大量资源
    :param name:协程
    :return:
    '''
    print('start :', name)
    response = requests.get('http://www.baidu.com')
    print('end :', name)


if __name__ == '__main__':
    start_time = time.time()
    p = gevent.spawn(multipro, 'xiaohua')
    p1 = gevent.spawn(multipro, 'sss')
    p2 = gevent.spawn(multipro, 'xiddddaohua')
    p3 = gevent.spawn(multipro, 'xiaohffua')
    p4 = gevent.spawn(multipro, 'gggg')

    gevent.joinall([p, p1, p2, p3, p4])
    print(time.time() - start_time)
    # 1.512552261352539

# for i in range(27, 1000):
    # print('p'+str(i)+"= gevent.spawn(multipro, 'xiaohua')")
    # print('p' + str(i), end=', ')

# 2.4857776165008545