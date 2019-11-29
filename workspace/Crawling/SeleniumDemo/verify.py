import requests
from lxml import etree


response = requests.get('https://weibo.com/')
xstr = etree.HTML(response.text)

if 'class="info_list verify clearfix" style="display: none;"' not in response.text:
    print('出验证码了 !!!')
    res = xstr.xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img[@action-type="btn_change_verifycode"]/@src')
    print('出现验证码: ',res)
    response = requests.get(res)
    with open('Verification.png', 'wb') as f:
        f.write(response.content)
    verify = input('输入验证码:  ')
    driver.find_element_by_tag_name('verifycode').send_keys(verify)
    driver.find_element_by_class_name('W_btn_a').click()