
# 面向对象
class Demo:
    i = 123
    def func(self,i):
        i += 1
        return i

demo = Demo()
result = demo.func(11)
# print(result)



list1 = [x for x in range(1,51)]
list2 = []
for i in list1:
    if 2*i in list1:
        list2.append(2*i)
        list1.remove(2*i)

print(list1)
print(list2)
print(len(list1))