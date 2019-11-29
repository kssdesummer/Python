from threading import Thread
import time

# 线程创建
def threadDemo(name):
    print('start :', name)
    time.sleep(1)
    print('end :', name)
    time.sleep(0.5)

if __name__ == '__main__':
    start_time = time.time()
    # 参数target:函数 args:元组,函数传参
    t = Thread(target=threadDemo, args=('xiaohua',))
    t1 = Thread(target=threadDemo, args=('kjljkf',))
    t2 = Thread(target=threadDemo, args=('fsdf',))
    t3 = Thread(target=threadDemo, args=('xiaohua',))
    t4 = Thread(target=threadDemo, args=('kjljkf',))
    t5 = Thread(target=threadDemo, args=('fsdf',))


    # 线程开始
    t.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()


    # 等待线程结束 (阻塞)
    t.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


    # 打印程序运行时间
    print(time.time() - start_time)
    # 2.0028369426727295
    # 线程的运行时间比进程的要短,是因为1.进程里都有一个线程2.进程发生切换创建耗时

# for i in range(27, 1000):
    # print('t'+str(i)+" = Thread(target=threadDemo, args=('xiaohua',))")
    # print('t' + str(i)+'.start()')
    # print('t' + str(i)+'.join()')

# 1.8989250659942627