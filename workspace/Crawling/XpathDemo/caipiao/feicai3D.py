import requests
from lxml import etree
from time import sleep, time

url = 'http://datachart.500.com/sd/history/inc/history.php?start=2010282&end=2019311'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'sdc_session=1574388812409; bdshare_firstime=1574388812439; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1574388819; _jzqc=1; _jzqckmp=1; _qzjc=1; __utmc=63332592; PHPSESSID=8f8r7mudfpvjll74r1dvsnc0f1; ck_RegUrl=datachart.500.com; ck_RegFromUrl=http%3A//datachart.500.com/dlt/history/history.shtml; _jzqa=1.4230165881882599000.1574388819.1574388819.1574392185.2; _jzqx=1.1574392185.1574392185.1.jzqsr=datachart%2E500%2Ecom|jzqct=/dlt/history/history%2Eshtml.-; __utma=63332592.592455340.1574388836.1574388836.1574392186.2; __utmz=63332592.1574392186.2.2.utmcsr=datachart.500.com|utmccn=(referral)|utmcmd=referral|utmcct=/dlt/history/history.shtml; __utmt=1; WT_FPC=id=undefined:lv=1574394031742:ss=1574392567378; sdc_userflag=1574392184310::1574394031750::16; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1574394032; _qzja=1.1482283222.1574388819686.1574388819686.1574392567483.1574393926132.1574394031818.0.0.0.14.2; _qzjb=1.1574392567482.11.0.0.0; _qzjto=14.2.0; _jzqb=1.16.10.1574392185.1; __utmb=63332592.16.10.1574392186; motion_id=1574394062644_0.8183583082541552; CLICKSTRN_ID=221.218.211.182-1574388814.843922::03ADA9D3DECBD4803BCD1145ED699905',
    'Host': 'datachart.500.com',
    'Referer': 'http://datachart.500.com/sd/history/inc/history.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}

response = requests.get(url, headers=headers)
data = response.text
strText = etree.HTML(data)

'//tr[@class="t_tr1"]'
res = ''
for m in range(1, 3000):
    if m % 9 == 0:
        sleep(0.5)
    str = '//tr[@class="t_tr1"][{}]/td'.format(m)
    # print(str)
    for i in range(0, 3):
        num = strText.xpath(str)[i].text + '\t'
        res += num

    with open('data1.txt', 'a+') as f:
        f.write(res + '\n')
    print('写入第{}条'.format(m))
    res = ''
