
# 反向输出字符串
a = "dfsdfsdfdsfffffff"
print(a[::-1])

# 尝试爬出拼多多商品
import requests

url = 'http://mobile.yangkeduo.com/search_catgoods.html?opt_id=9502&opt1_id=999998&opt2_id=999999&opt_g=1&opt_type=3&opt_name=%E6%AF%9B%E8%A1%A3%E9%92%88%E7%BB%87&_x_link_id=50bccebe-b140-425f-be17-d04d0be211a6&refer_page_name=search&refer_page_id=10031_1574319917687_ZoT89JaXmR&refer_page_sn=10031'
response = requests.get(url)
print(response.text)
with open('pinduo.html','wb') as f:
    f.write(response.content)


'''
(^.*): (.*)
'$1':'$2'
'''