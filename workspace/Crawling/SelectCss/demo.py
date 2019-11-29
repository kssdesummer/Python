
import requests
from bs4 import BeautifulSoup
'''
> 紧接着


'''

response = requests.get('https://www.baidu.com/')
response.encoding = 'utf-8'

# with open('baidu.html','wb') as f:
#     f.write(response.content)

# 实例化选择器,指定解析器
soup = BeautifulSoup(response.text, 'lxml')
res = soup.select('#su')
print(res[0])
# 取属性
print(res[0]['value'])
# 取内容
print(res[0].text)
