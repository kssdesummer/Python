import requests
import json
from time import time, sleep
import re
import os


# 解析请求地址
def get_url():
    # url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1574412774248'
    # url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1574413473906'

    # 从上面的url的set值在翻页的时候有20的变化
    # 将所有的url放入列表中,拿到一个url就去调用对应的函数
    my_list = []
    for i in range(10):
        setnum = i * 20
        page_url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset={}&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1574413473906'.format(
            setnum)
        print('请求页面{}'.format(i+1))
        my_list.append((page_url, list_page))
    while my_list:
        print('while等待1秒...')
        sleep(1)
        # 将列表中的(url,函数)取出
        (my_url, func) = my_list[0]
        #
        func(my_url,my_list)
        my_list.pop(0)
        # list_page(page_url)

# 获取json的url
def list_page(url,my_list):
    # 请求列表页数据
    response = requests.get(url, headers=headers)

    # with open('toutiao.html','wb') as f:
    #     f.write(response.content)
    # 得到json字符串
    jsonStr = response.text
    # 将json字符串转为字典
    jsonstr = json.loads(jsonStr)
    # print(type(jsonstr))
    # 得到文章列表
    # print(jsonstr['data'][0]['article_url'])
    for i in range(3):
        if 'article_url' in jsonstr['data'][i]:
            list_url = jsonstr['data'][i]['article_url']
            print("详情页url:", list_url)

            my_list.append((list_url,details_page))

            # details_page(list_url)

# json里面获取的url
def details_page(url,my_list):
    print('details_page等待1秒...')
    sleep(1)
    # list_url = 'http://toutiao.com/group/6761972340126384647/'
    response1 = requests.get(url, headers=headers)
    # with open('detil.html','wb') as f:
    #     f.write(response1.content)

    # 一次调用放在循环外
    # pattern = 'gallery: JSON.parse\((.*)\),'
    # pat = re.compile(pattern)
    resp = response1.text
    # 重复使用时用compile,省去多次创建删除
    # pattern = 'gallery: JSON.parse\((.*)\),'
    # res = re.search(pattern, resp)
    res = pat.search(resp)
    if res:
        json_str = res.group(1)
        # json_str 本身是字符串,里面包含了引号的字符串
        # 用两次json.loads解析得到字典
        # 第一次得到取出外层字符串引号
        str = json.loads(json_str)
        res = json.loads(str)
        img_list = res['sub_images']

        for item in img_list:
            img_url = item['url']

            my_list.append((img_url,img_page))
            # img_page(img_url)

# 详情页的url
def img_page(url,my_list):
    print('img_page等待1秒...')
    sleep(1)
    filename = mydir + '/' + url.split('/')[-1] + '.jpg'
    response = requests.get(url, headers=headers)
    print('downloading..', filename)
    with open(filename, 'wb') as f:
        f.write(response.content)

# 程序入口
if __name__ == '__main__':
    # 创建文件夹
    mydir = 'download'
    if not os.path.exists(mydir):
        os.mkdir('download')
    # 重复使用的正则匹配部分
    pattern = 'gallery: JSON.parse\((.*)\),'
    pat = re.compile(pattern)
    # 请求头信息
    headers = {
        'cookie': 'tt_webid=6762043061985871374; s_v_web_id=84053cda68b08ee0f73aab391f289892; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=b3wec7y2o1574410854629; csrftoken=c6db8a9d842dd6cf95627a9a393621cb; tt_webid=6762043061985871374; UM_distinctid=16e92351e3a1bb-086ff665703d3-5373e62-1fa400-16e92351e3b9; CNZZDATA1259612802=1410974685-1574409634-https%253A%252F%252Fwww.toutiao.com%252F%7C1574409634; _ga=GA1.2.564560248.1574410985; _gid=GA1.2.1834392643.1574410985',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    # 调用函数
    get_url()
