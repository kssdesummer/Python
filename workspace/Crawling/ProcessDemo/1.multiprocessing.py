from multiprocessing import Process
import time
# 多进程创建

def multipro(name):
    print('start :', name)
    time.sleep(2)
    print('end :', name)


if __name__ == '__main__':
    # 获取开始时间
    start_time = time.time()
    # 生成一个多线程的类
    # 参数target:函数 args:元组,函数传参
    p = Process(target=multipro, args=('xiaohua',))
    p1 = Process(target=multipro, args=('cis',))
    p2 = Process(target=multipro, args=('xhisd',))
    # 线程开始
    p.start()
    p1.start()
    p2.start()
    # 等待线程结束 (阻塞)
    p.join()
    p1.join()
    p2.join()

    # 打印程序运行时间
    print(time.time()-start_time)
    # 2.1795127391815186