import requests
import re
import json
import time
import random
import hashlib

'''
1.确定需求
2.分析需求
3.发送请求
4.解析数据
5.存储数据
'''
'''
url = 'http://www.baidu.com'
# 调用get请求并返回信息
response = requests.get(url)
# 返回请求的状态码
print(response)
# response.text 返回html信息字符串类型
# 解决乱码
response.encoding = 'utf-8'
print(response.text)
# response.content 返回html信息二进制 bytes : b',
print(response.content)
with open('baidu.html','wb') as f:
    f.write(response.content)
'''

'''
url = 'https://www.xicidaili.com/'
headers = {
   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
   'Accept-Encoding':'gzip, deflate, br',
   'Accept-Language':'zh-CN,zh;q=0.9',
   'Cache-Control':'max-age=0',
   'Connection':'keep-alive',
   'Cookie':'free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTVjMjBmMzc2N2VmYTAyNmE5NjQyNTA0MjEzZDY0YzhmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUFPYW5uQW5RN2R3T3RpWlFFd0J6MnNSRlZTL2hqVFlEMWVyMzNWWURKOG89BjsARg%3D%3D--7f1a7d5a2bbdbd7180c2d15386246ed0a321677b; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1573873734; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1573873734',
   'Host':'www.xicidaili.com',
   'If-None-Match':'W/"4edae45af2483a381671fe837e5dd20a"',
   'Sec-Fetch-Mode':'navigate',
   'Sec-Fetch-Site':'none',
   'Sec-Fetch-User':'?1',
   'Upgrade-Insecure-Requests':'1',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}
response = requests.get(url,headers=headers)
with open('xici.html','wb')as f:
    f.write(response.content)
'''
'''
# 哔哩哔哩
url = 'https://api.bilibili.com/x/space/upstat?mid=43222001&jsonp=jsonp&callback=__jp5'
headers = {
'Referer': 'https://space.bilibili.com/43222001?spm_id_from=333.788.b_765f7570696e666f.1',
'Sec-Fetch-Mode':'no-cors',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
response = requests.get(url,headers=headers)
print(response.text)
# __jp5({"code":0,"message":"0","ttl":1,"data":{"archive":{"view":71132146},"article":{"view":51149},"likes":3155719}})
pattern = r'__jp5\((.*)\)'
res = re.search(pattern,response.text)
print(res.group(1))
# 正则得到想要的数据,字符串
# {"code":0,"message":"0","ttl":1,"data":{"archive":{"view":71132146},"article":{"view":51149},"likes":3155719}}
res1 = res.group(1)
resoult = json.loads(res1)
# 将字符串转化为字典 dict
print(type(resoult))
# 索引取值拿到想要的数据
print(resoult['data']['archive'])
'''

'''
# 请求地址 人人网登录
url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=20191061544221'
# data 数据表单
data = {
   'email': '15518103321',
   'icode': '',
   'origURL': 'http://www.renren.com/home',
   'domain': 'renren.com',
   'key_id': 1,
   'captcha_type': 'web_login',
   'password': '6be7f54bec45dfbb579002c0cf4f37071397422b505332c214ac57bdfa22c1e3',
   'rkey': '8674c4b1b7f9d56a99bf48984a0591ba',
   'f': 'http%3A%2F%2Fwww.renren.com%2F972876598%2Fnewsfeed%2Fphoto',
}
# 由于http每次访问的是分开的,所以转换页面之后无法直接访问
# 引入一个requests.session() 类
s = requests.session()

# response = requests.post(url,data=data)
# 使用带有session的requests请求
response = s.post(url,data=data)
print(response.text)
# 得到响应正文,并解析跳转页面
# {"code":true,"homeUrl":"http://www.renren.com/home"}
res = json.loads(response.text)

# 访问跳转页面url
home_url = res['homeUrl']
print(home_url)
# http://www.renren.com/home
# response1 = requests.get(home_url)
response1 = s.get(home_url)
print(response1)
with open('post_renren.html','wb') as f:
   f.write(response1.content)
   print('人人网采集完毕')

'''

'''
# 有道翻译,进行简单的解密
'''
'''
js页面里面的加密数据
ts是当前的时间戳是r
r = "" + (new Date).getTime()
salt是i用时间戳加一个在10以内的随机数
i = r + parseInt(10 * Math.random(), 10);
sign是一个字符串加密
sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
'''

def translate(key):
   ts = int(time.time() * 1000)
   salt = str(ts + random.randint(0, 10))
   sign = hashlib.md5(("fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj").encode(encoding='UTF-8')).hexdigest()

   url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
   data = {
      'i': key,
      'from': 'AUTO',
      'to': 'AUTO',
      'smartresult': 'dict',
      'client': 'fanyideskweb',
      'salt': salt,
      'sign': sign,
      'ts': ts,
      'bv': 'a4f4c82afd8bdba188e568d101be3f53',
      'doctype': 'json',
      'version': '2.1',
      'keyfrom': 'fanyi.web',
      'action': 'FY_BY_REALTlME',
   }
   headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
      'Referer':'http://fanyi.youdao.com/',
      'Cookie':'GA1.2.2086576260.1573286502; P_INFO=15518103321|1573286520|1|youdaonote|00&99|null&null&null#bej&null#10#0|&0||15518103321; OUTFOX_SEARCH_USER_ID_NCOO=1187541123.7925053; OUTFOX_SEARCH_USER_ID="1147024065@10.108.160.18"; JSESSIONID=aaar5QNZezots4gSjg85w; ___rl__test__cookies=1574040270926',

   }
   response = requests.post(url,data=data,headers=headers)
   res = response.text
   result = json.loads(res)
   print('翻译结果: ',result['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
   while True:
      try:
         key = input('请输入翻译内容(q退出):\n')
         if key == 'q':
            break
         translate(key)
      except:
         print('可能是网络波动,请检查网络!')


'''
微博爬取个人主页的所有内容
发布时间:created_at
评论数:comments_count
点赞数:attitudes_count
观看数:obj_ext
转发数:reposts_count
发布内容：text


# 删除标签 <a>之类的
from w3lib.html import remove_tags

# url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050'
# url1 = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050&page=2'
def weiboInfoPage(url,i):
   headers = {
      'Referer': 'https://m.weibo.cn/u/1239246050',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
   }

   response = requests.get(url,headers=headers)
   requests.endcoding = 'utf-8'
   # print(response.text)
   res = json.loads(response.text)['data']['cards']
   # print(type(res))
   print('开始爬取第',i+1,'页')
   for item in res:

      if 'mblog' in item:
         data = item['mblog']
         created_at = data['created_at']
         comments_count = data['comments_count']
         attitudes_count = data['attitudes_count']
         reposts_count = data['reposts_count']
         content = remove_tags(data['text']).replace('\n','')
         if data['pic_types'] == '0':
            content_type = "图文"
         elif 'page_info' in data and 'type' in data['page_info']:
            content_type = data['page_info']['type']
         else:
            content_type = '纯文字'
         if 'page_info' in data and 'play_count' in data['page_info']:
            watch_count = data['page_info']['play_count']
         else:
            watch_count = 0
         print(content_type,'created_at:',created_at,'comments_count:',comments_count,'attitudes_count:',attitudes_count,'watch_count:',watch_count,'reposts_count:',reposts_count,'text：',content)

if __name__ == '__main__':
   # url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050'
   for i in range(3):
      url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&' \
            'containerid=1076031239246050&page='+str(i+1)
      weiboInfoPage(url,i)
      time.sleep(3)
'''