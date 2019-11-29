import requests
from lxml import etree

url = 'http://datachart.500.com/dlt/history/newinc/history.php?start=08104&end=19133'

response = requests.get(url)
# print(response.text)
# response.encoding = 'utf-8'
# with open('data.html', 'wb') as f:
#     f.write(response.content)

data = response.text
strText = etree.HTML(data)
# str = '//*[@id="tdata"]/tr[@class="t_tr1"][{}]/td'.format(1)
# qianqu = strText.xpath(str)[0].text
# houqu = strText.xpath('//*[@id="tdata"]/tr[@class="t_tr1"][1]/td')[0].text
# str = '//*[@id="tdata"]/tr[@class="t_tr1"][{}]/td'.format(1)

res = ''
for m in range(1, 2001):
    str = '//*[@id="tdata"]/tr[@class="t_tr1"][{}]/td'.format(m)
    # print(str)
    for i in range(1, 8):
        num = strText.xpath(str)[i].text
        if i == 4:
            num += '\t'
        else:
            num += '\t'
        res += num
    with open('data.txt', 'a+') as f:
        f.write(res+'\n')
    print('写入第{}条'.format(m))
    res = ''
