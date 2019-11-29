'''
引入进程池的概念为了解决:
1. 每个任务一个进程,100个任务时,限制进程的数量
2. 如果任务过多,频繁的创建和销毁进程,影响性能
'''

from multiprocessing import Pool
import time


# 多进程创建
def multipro(name):
    print('start :', name)
    time.sleep(1)
    print('end :', name)
    time.sleep(0.5)


if __name__ == '__main__':
    # 用法
    # 创建限制同时进行的进程为3
    # 并且进程池是复用的
    pool = Pool(processes=3)
    names = ['aa', 'bb', 'cc', 'dd', 'ff']

    for name in names:
        # 这里会将所有的name放入pool里面
        # 参数target:函数 args:元组,函数传参
        pool.apply_async(func=multipro, args=(name,))
    # 当用完pool进程池之后,需要关闭
    pool.close()
    # 关闭后不能再使用进程池
    # pool.apply_async(func=multipro, args=('name',))
    # 打印错误 : ValueError: Pool not running

    # 关闭后,需要等待所有的进程执行结束
    pool.join()
