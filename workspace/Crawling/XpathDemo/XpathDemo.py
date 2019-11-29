from lxml import etree
import requests

url = 'http://mobile.yangkeduo.com/catgoods.html?refer_page_name=index&opt_id=485&opt_name=%E8%A3%99%E8%A3%85&opt_type=2&goods_id=5350608164&refer_page_id=10002_1574325360535_PPJUro1HwE&refer_page_sn=10002'

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'api_uid=rBQGBl3PqlucjDYGU55QAg==; _nano_fp=Xpd8n0gjn0ganqXbnT__vJI0k0SLyojSn3DqBDl8; ua=Mozilla%2F5.0%20(Linux%3B%20Android%206.0%3B%20Nexus%205%20Build%2FMRA58N)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F76.0.3809.132%20Mobile%20Safari%2F537.36; webp=1; JSESSIONID=5BBDE543F2B83C21A7CCBA7E4B3179DB; pdd_user_id=2167245165276; pdd_user_uin=6WWQ27BN5PDEMINRRUWHBF4SUE_GEXDA; PDDAccessToken=SGJWW4ZRGABNTMB3ALXRP2EZHDLW5KBT26IJ7D5ZFOZSOG6PUORA112dc62; rec_list_index=rec_list_index_qJ9nho',
    'Host':'mobile.yangkeduo.com',
    'Referer':'http://mobile.yangkeduo.com/catgoods.html?refer_page_name=index&opt_id=485&opt_name=%E8%A3%99%E8%A3%85&opt_type=2&goods_id=5350608164&refer_page_id=10002_1574325360535_PPJUro1HwE&refer_page_sn=10002',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36',
}

response = requests.get(url,headers=headers)

# 将响应正文写入文件
# with open('pinduoduo.html', 'wb')as f:
#     f.write(response.content)

# 得到需要解析的字符串
strText = etree.HTML(response.text)
titleList = strText.xpath('//div[@class="pHbSR-xp _1cP_KihG"]')
# title = strText.xpath('//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]')
print(titleList)
for i in range(0,len(titleList)):
    # 得到宝贝的标题
    title = strText.xpath('//div[@class="pHbSR-xp _1cP_KihG"]')[i].text
    print(title)
