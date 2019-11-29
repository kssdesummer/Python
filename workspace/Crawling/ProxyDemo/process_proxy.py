import requests
from lxml import etree
import time
from multiprocessing import Pool


# 根据传参url,获取当页所有的ip和端口号
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
    for i in range(1, len(num_ip)):
        proxyIp = num_ip[i].text + ':' + num_port[i].text
        # print(proxyIp)
        ip_list.append(proxyIp)
    return ip_list


# 验证ip是否可用
def test_ip(ip):
    time.sleep(0.5)
    print('验证ip:', ip)
    # url = 'http://httpbin.org/get'
    url = 'http://www.baidu.com'
    proxy = {
        # 'http://180.122.151.35:49645'
        'http': 'http://' + ip,
        'https': 'https://' + ip,
    }
    try:
        # verity=False
        response = requests.get(url, proxies=proxy,timeout=5)
        print(response.status_code)
        # # print(response.text)
        # res = json.loads(response.text)
        # ip_ele = res['origin']
        print('ip可用:', ip)
        return ip
    except:
        print('ip不可用')

# 进程池函数
def processPool():
    # 初始化存放列表
    useful_ip = []
    # 循环遍历页数
    for i in range(2, 3):
        print('第{}页'.format(i))
        url = 'http://www.66ip.cn/{}.html'.format(i)
        # 调用获取ip函数
        ip_list = get_free_url(url)

        # 创建线程池
        pool = Pool(processes=5)
        for ip in ip_list:
            # 进程池启动将所有ip存入进程池
            res = pool.apply_async(func=test_ip, args=(ip,))
            # 将所有ip存入列表
            useful_ip.append(res)
        pool.close()
        pool.join()
    # 得到的是线程池返回值,拿值需要遍历用get()
    # print(useful_ip)
    # <multiprocessing.pool.ApplyResult object at 0x037E6A78>
    res_list = []
    for useIp in useful_ip:
        if useIp.get() != None:
            # 将进程池返回值用get()方式取出
            res_list.append(useIp.get())
    return  res_list

if __name__ == '__main__':
    '''
        程序入口
        验证 66代理 网站的可用ip
    '''
    start_time = time.time()
    res_list = processPool()
    print('可用ip列表:\n', res_list)
    print(time.time() - start_time)
# ['210.48.204.134:59916', '103.9.227.210:53281', '41.242.57.34:38783', '95.142.219.181:56379', '118.174.196.130:8080', '157.245.205.81:8080', '95.9.150.33:47923', '157.100.58.97:999', '103.93.90.246:23500']
