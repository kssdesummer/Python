headers = {
    ':authority': 'www.toutiao.com',
    ':method': 'GET',
    ':path': '/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1574412774248',
    ':scheme': 'https',
    'accept': 'application/json, text/javascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'tt_webid=6762043061985871374; s_v_web_id=84053cda68b08ee0f73aab391f289892; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=b3wec7y2o1574410854629; csrftoken=c6db8a9d842dd6cf95627a9a393621cb; tt_webid=6762043061985871374; UM_distinctid=16e92351e3a1bb-086ff665703d3-5373e62-1fa400-16e92351e3b9; CNZZDATA1259612802=1410974685-1574409634-https%253A%252F%252Fwww.toutiao.com%252F%7C1574409634; _ga=GA1.2.564560248.1574410985; _gid=GA1.2.1834392643.1574410985',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

str = '&#20320;&#22312;&#21738;&#25214;&#30340;&#36825;&#26434;&#19971;&#26434;&#20843;'
str1 = str.replace(';&#', ' ')
print(str1)

a = 2  # 10
b = 3  # 11
a = a ^ b
b = b ^ a
a = a ^ b
print(a)
print(b)
