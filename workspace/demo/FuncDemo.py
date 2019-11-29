import keyword
# print("内建关键字列表:\n",keyword.kwlist)
import time
'''
# 写一个斐波那契数列
# 0 1 1 2 3 5 8 13
'''
def FeiBo(n):
    a,b = 0,1
    list = []
    for i in range(n):
        list.append(a)
        b, a = a+ b, b
        # a = b
        # b = a+b
    return list
print(FeiBo(8))


'''
用递归函数实现一个斐波那契

'''
def feibo(n):
    if n ==0 or n == 1:
        return n
    elif n > 1:
        # start = time.perf_counter()
        return feibo(n-1) + feibo(n-2)
        # feibo(n-1)
        # end = time.perf_counter()
        # timer = end - start
        # print(timer)
def feiboList(num):
    resList = []
    for i in range(num):
        resList.append(feibo(i))
    return resList
res = feiboList(8)
print(res)
'''
# 收集参数关键字 命名关键字收集参数
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("普通关键字收集: \n类型是:",type(arguments))
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print("命名关键字收集: \n类型是:",type(keywords))
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
           
# 解包,*args 用于得到列表或元组的
# **kwargs 用于得到key对应的value

args = [3,6,9]
print(*args)
print(range(*args))
print(list(range(*args)))
print(range(0,3))
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
kwargs = {"voltage": "four million", "action": "VOOM", "state": "bleedin' demised"}
parrot(**kwargs)


# lambda 表达式:匿名函数
def demo():
    """
    这是一个实验lambda
    :return: lamdba运算得到的值
    """
    return lambda x : x + 1
value = demo()
result = value(2)
print(result)

a = lambda x,y : x + y
print(a(2,3))

'''