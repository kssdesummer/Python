# 字典:键值对存在,python3.6以后有序,之前是无序的
# 没有索引,无法分片,以及加乘

info = {"name": "Daive", "age": "18", "state": "single"}
print("键值对输出 : ")
for i in info.items():
    print(i)    # 得到元组
print("输出键 : ")
for i in info.keys():
    print(i)
print("输出值: ")
for i in info.values():
    print(i)

name = info.pop("name")
print(name)

# 删除某值
del info["age"]
print(info)

# 声明字典
'''

dict(形参=值,形参=值...)
dict(符合嵌套容器)    元组
dict(zip(键容器,值容器))  元组或者列表

'''
touple1 = ((1,6),(2,9),(3,5))
dict1 = dict(touple1)
a = dict1
print(type(a))


# 常用函数
'''
dict.clear() 清空
dict.copy() 深拷贝
dict.keys() 
dict.values()
dict.items()
dict.pop()  根据键删除
dict.popitem()  删除最后一对
dict.setdefault()   添加数据
dict.update(键=值,键=值,键=值,..)
dict.update({键:值,键:值,键:值,...})
dict.get(key,默认值)   得到对应值,找不到返回None,反之默认值

'''