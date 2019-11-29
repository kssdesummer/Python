import requests
from lxml import etree
import json
import time


def get_free_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # with open('xici.html', 'wb') as f:
    #     f.write(response.content)
    res = etree.HTML(response.text)
    # 这是拷贝过来的xpath里的tbody层是获取不到的
    # //*[@id="ip_list"]/tbody/tr[2]/td[2]
    num_ip = res.xpath('//*[@id="main"]/div/div[1]/table/tr/td[1]')
    num_port = res.xpath('//*[@id="main"]/div/div[1]/table/tr/td[2]')
    # print(num_ip, num_port)
    # print(len(num_ip))
    ip_list = []
    for i in range(1,len(num_ip)):
        proxyIp =  num_ip[i].text + ':' + num_port[i].text
        # print(proxyIp)
        ip_list.append(proxyIp)
    return ip_list


def test_ip(ip):
    time.sleep(0.5)
    print('验证ip:', ip)
    # url = 'http://httpbin.org/get'
    url = 'http://www.baidu.com'
    proxy = {
        # 'http://180.122.151.35:49645'
        'http': 'http://'+ip,
        'https': 'https://'+ip,
    }
    try:
        # verity=False
        response = requests.get(url, proxies=proxy)
        print(response.status_code)
        # # print(response.text)
        # res = json.loads(response.text)
        # ip_ele = res['origin']
        print('ip可用:', ip)
        return ip
    except:
        print('ip不可用')


if __name__ == '__main__':
    useful_ip = []
    for i in range(1,3):
        url = 'http://www.66ip.cn/{}.html'.format(i)
        ip_list = get_free_url(url)

        for ip in ip_list:
            res = test_ip(ip)
            if res != None:
                useful_ip.append(res)
        print('第{}页'.format(i))
    print(useful_ip)
# ['210.48.204.134:59916', '103.9.227.210:53281', '41.242.57.34:38783', '95.142.219.181:56379', '118.174.196.130:8080', '157.245.205.81:8080', '95.9.150.33:47923', '157.100.58.97:999', '103.93.90.246:23500']