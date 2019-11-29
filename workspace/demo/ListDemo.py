from collections import deque
from math import pi
import copy
# 容器
# list 列表
# 列表推导式
list3 = [x for x in range(10) if x %2 == 0]
print(list3)

list4 = [str(round(pi,i)) for i in range(1,5)]
print(list4)

# round 取小数点后的位数
# 列表的常用函数
List1 = []
List2 = []

List1.append("a")   # append 在列表最后添加元素
List2.append("a")

List1.extend(List2) # extend 合并两个列表

List1.insert(2,"b") # insert 在索引位置插入元素

List1.remove("a")   # remove 删除某个元素

List1.pop(1)    # pop 删除索引位置的元素,null删除最后一项

num = List1.count("a")  # count 统计某元素的出现的次数

List1.append("a")
List1.append("b")
List1.append("c")
List1.append("a")
List1.sort(reverse=True)    # sort 排序默认false正序


List2.clear()
List3 = List1.copy()    # copy 浅拷贝
print(List1)
print(List3)

List3.append("a")
List1.append("b")

print(List1)
print(List3)

# 列表实现堆栈:先入后出
list1 = [3,4,5]
list1.append(6)
list1.append(7)
print(list1.pop())
print(list1.pop())
print(list1.pop())
print(list1.pop())
print(list1.pop())

# 列表实现队列,先入先出,使用collections.deque
queue = deque(["alen","adle","bob"])
queue.append("garry")
queue.append("willen")
queue.popleft()
queue.popleft()
print(queue)

# 嵌套列表
matrix = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
]
list1 = [row for row in matrix]
list = [[row[i] for row in matrix] for i in range(4)]
print(list)
print(list1)

# del list[开始值:结束值] 删除列表元素,默认冒号删除全部
del list[1:2]
del list[:]


list = [[1,2],3,4]
list2 = copy.copy(list)
list1 = copy.deepcopy(list)
list[0][1] = 5
print(list1)
print(list2)



