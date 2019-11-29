# 集合,无序去重,无索引
fruit = {"apple", "banana", "orange", "pear"}
anmail = {"pig", "dog", "orange", "pear"}
print(fruit)
for i in fruit:
    if i in anmail:
        print("anmail eat :", i)
    else:
        print("it's bad")

# 集合推导式
sets1 = {x for x in range(30) if x % 6 == 0}
print(sets1)

# 集合专用函数:
'''
add() 添加
pop() 随机删除
remove("删除值")   删除某值
discard("删除值") 删除值,无不操作
clear() 清除集合
copy() 拷贝,得到新的集合

'''

'''
# 集合的运算函数
difference() 差集
intersection()  交集
union() 并集
对称差集
更新差集
更新交集
更新并集
更新对称差集

'''

