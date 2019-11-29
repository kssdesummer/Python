# 元组,元素不可改
a = 1, 2, 3
b = (4, 5, 6)
c = a, b
print(a[0], b, c[0])

# 元组推导式,结果是迭代器
toup1 = (x for x in range(5) if x != 3)
print(type(toup1))
for i in toup1:
    print(i)

# 使用yield方式生成一个生成器
def generator():
    yield 2
    yield 2
    yield 2
    yield 2
res = generator()   # 得到生成器generator
print(type(res))