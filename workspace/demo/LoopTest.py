# 2019-11-5 复习循环部分
# 顺序结构，自上而下执行
# 分支结构：if...else...
# 循环结构：while条件语句与for循环语句
# 其他语句：continue，break，pass
# 单支语句:类似与三目运算符  真值 if 条件 else 假值


'''
# if ... else ...分支结构

i = int(input("please input greater than 0 : "))
if i == 0:
    print("this num is : 0 \n")
elif 0 < i <= 5:
    print("this num between 0 and 5 \n")
else:
    print("this num greater than five")
'''

'''
# for 循环遍历
testList = ["small","middle","big","more"]
for i in testList:
    print(i,len(i))
# 遍历字典
testDict = {"name":"xiaoming","age":20,"job":"student"}
for m,n in testDict.items():
    print(m,":",n)
# 遍历多级容器
manyList = [["smile","badly"],["happy","cry"]]
for i1,i2 in manyList:
    print(i1,i2)
# 取值与索引值 enumerate
for index,value in enumerate(testList):
    print(index+1,":",value)

# 得到质数，else为for的子句，当循环用尽或条件为假时执行
# break跳出本次循环并结束
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n," is a prime number")
'''


'''
# while循环嵌套使用

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    # i += 1  写在这里的话会深度过深，原因是continue跳出本次循环，这句话不执行，之后的i只等于3
'''

'''
# 单支语句

singleVle = int(input("please input num ："))
num = singleVle if singleVle > 2 else 0
print("The vlue is : ",num)
'''

# 打印十行十列星星
for i in range(10):
    for j in range(10):
        if j % 2 == 0:
            print("* ",end="")
        else:
            print("# ",end="")
        if j == 9:
            print("")