# 1. 修改不可变类型会如何,何种异常
def demo1():
    print('报错,TypeError')


# demo1()

# 2. 不用中间变量交换a,b
def change():
    a, b = 2, 3
    # 方法一
    a, b = b, a
    print(a, b)
    # 方法二
    a = a + b
    b = a - b
    a = a - b
    print(a, b)
    # 方法三:异或
    a = a ^ b
    b = b ^ a
    a = a ^ b
    print(a, b)
    # 方法四:借助容器
    a = str(a) + str(b)
    b = int(a[0])
    a = int(a[1])
    print(a, b)


# change()

# 3.print调用python底层的什么方法
def demo3():
    print('调用 sys.stdout.write方法,在控制台打印字符串')


# demo3()

# 4 下面这段代码的输出结果将是什么？请解释？(2018-3-30-lxy)
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

'''
1 1 1 #继承自父类的类属性 x,所以都一样,指向同一块内存地址。
1 2 1 #更改 Child1,Child1 的 x 指向了新的内存地址。
3 2 3 #更改 Parent,Parent 的 x 指向了新的内存地址。
'''


# 5.input()函数理解
def demo5():
    print(
        '''
        在python3中,input获取用户输入,获取到的只有字符串类型
        在python2中,有raw_input()和input()
            raw_input():与python中的用法一样
            input():用户输入什么类型就是什么类型
        ''')


# demo5()

# 6.A0-An 的结果
def demo6():
    A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
    A1 = range(10)
    # python2中是列表占大量内存,python3里是range(0,10)
    A2 = [i for i in A1 if i in A0]
    A3 = [A0[s] for s in A0]
    A4 = [i for i in A1 if i in A3]
    A5 = {i: i * i for i in A1}
    A6 = [[i, i * i] for i in A1]
    print(A0, '\n', A1, '\n', A2, '\n', A3, '\n', A4, '\n', A5, '\n', A6)
    # alt + 左键选中多个复制 粘贴
# demo6()