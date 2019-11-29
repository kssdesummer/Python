import pickle

# 序列化模块
'''
pickle.dumps(数据):序列化数据,转为机器语言便于存储使用
pickle.loads(bytes数据):将序列化的bytes转回原数据

'''
word = "this is 序列化"
word1 = pickle.dumps(word) # bytes类型
print(word1)
word2 = pickle.loads(word1) + "模块"
print(word2)

# 将数据序列化后写入
with open('../data/test.md',"wb") as io:
    pickle.dump(word,io)

# 将数据反序列化后取出
with open("../data/test.md","rb") as rd:
    data = pickle.load(rd)
    print(data)