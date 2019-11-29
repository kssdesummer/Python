import time
# 时间模块

startTime = time.perf_counter() # 现在的时间
print(startTime)
numTime = time.time()   # 本地时间戳
print(numTime)
nowTime = time.ctime(numTime)   # 时间字符串
print(nowTime)
tupleTime = time.localtime()    #  时间元组
print(tupleTime)
stopTime = time.perf_counter()
print(stopTime)
print(stopTime-startTime)

norTime = time.strptime("2019-11-06 20:59:20","%Y-%m-%d %H:%M:%S")
print(type(norTime))  # 输入指定格式提取到时间元组

strTime = time.strftime("%Y-%m-%d %H:%M:%S",norTime)
print(strTime)  # 格式化时间字符串
# t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
# t = time.mktime(t)
# print(type(time.gmtime(t)))
# print(time.strftime("%b %d %Y %H:%M:%S", norTime))
