import requests
import re
import json
import time
import random
# md5加密
import hashlib
# 删除标签 <a>之类的
from w3lib.html import remove_tags
from workspace.Crawling.CrawlWeibo.MysqlData import Store

store = Store()
'''
微博爬取个人主页的所有内容
发布时间:created_at
评论数:comments_count
点赞数:attitudes_count
观看数:obj_ext
转发数:reposts_count
发布内容：text

'''


# url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050'
# url1 = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050&page=2'
def weiboInfoPage(url, i):
    headers = {
        'Referer': 'https://m.weibo.cn/u/1239246050',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    requests.endcoding = 'utf-8'
    # print(response.text)
    res = json.loads(response.text)['data']['cards']
    # print(type(res))
    print('开始采集第', i + 1, '页')
    time.sleep(3)
    for item in res:

        if 'mblog' in item:
            data = item['mblog']
            created_at = data['created_at']
            if isinstance(data['comments_count'], str):
                reposts_count = int(data['comments_count'].replace('万+', '0000'))
            else:
                comments_count = data['comments_count']
            attitudes_count = data['attitudes_count']
            if isinstance(data['reposts_count'], str):
                reposts_count = int(data['reposts_count'].replace('万+', '0000'))
            else:
                reposts_count = data['reposts_count']
        content = remove_tags(data['text']).replace('\n', '')
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
        sql = 'insert into weibo_data(type,content,create_time,talk_count,zan_count,zhuan_count,watch_count)VALUES(%s,%s,%s,%s,%s,%s,%s)'
        data = (content_type, content, created_at, comments_count, attitudes_count, reposts_count, watch_count)
        store.execute_sql(sql, data)
        # print(content_type,'created_at:',created_at,'comments_count:',comments_count,'attitudes_count:',attitudes_count,'watch_count:',watch_count,'reposts_count:',reposts_count,'text：',content)
    print('第', i + 1, '页内容完毕')
    time.sleep(1)

if __name__ == '__main__':
    # url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&containerid=1076031239246050'
    for i in range(30,50):
        url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=1239246050&' \
              'containerid=1076031239246050&page=' + str(i + 1)
        weiboInfoPage(url, i)
    print('内容采集完毕,退出程序')
