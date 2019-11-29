import requests
from selenium import webdriver
from time import sleep, time
from selenium.webdriver.chrome.options import Options

# 实例化浏览器
print('实例化浏览器,请求中...')
# driver = webdriver.Chrome()
# # 设置窗口大小
# ## driver.set_window_size(width=1300, height=1080, windowHandle="current")
# # 最大化浏览器
# driver.maximize_window()
#
# # 设置超时,抛出异常
# # set_page_load_timeout方法用来设置页面完全加载的超时时间，完全加载即页面全部渲染，异步同步脚本都执行完成。没有设置超时时间默认是等待页面全部加载完成才会进入下一步骤，设置超时时间3s是加载到3s时中断操作抛出异常；
# driver.set_page_load_timeout(3)
# # set_script_timeout设置异步脚本到超时时间，用法同pageLoadTimeout一样，异步脚本也就是有async属性的异步脚本，可以在页面解析的同时执行；
# driver.set_script_timeout(3)
# # implicitly_wait识别对象的超时时间，如果在设置的时间内没有找到就抛出一个NoSuchElement异常，用法参数和上述一样；
# driver.implicitly_wait(3)


# headless 无浏览器界面
chrome_options = Options()
# 设置无界面
chrome_options.add_argument("--headless")
# 设置窗口大小
chrome_options.add_argument('window-size=1980,1980')

print('禁止加载js和图片 ..')
# 设置禁止加载JavaScript和images
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'javascript': 2,
        'stylesheet':2,
    }
}
chrome_options.add_experimental_option('prefs', prefs)
# 实例化浏览器
driver = webdriver.Chrome(options=chrome_options)


''''''


# 使用代理ip
# proxy_str = '219.234.5.128:3128'
# chrome_options.add_argument('--proxy-server=https://{}'.format(proxy_str))

print('页面请求中...')
# 请求微博页面
driver.get('https://weibo.com/')
# 等待请求地址相应
sleep(5)
print('请求成功,加载页面...')
sleep(15)
# 输入账号
print('输入账号密码...')
driver.find_element_by_id('loginname').send_keys('18510556963')
sleep(1)
driver.find_element_by_name('password').send_keys('yaoqinglin2011')
print('点击登录按钮...')
sleep(2)
# 点击登录
driver.find_element_by_class_name('W_btn_a').click()

if 'class="info_list verify clearfix" style="display: none;"' not in driver.page_source:
    print('出验证码了 !!!')
    res = driver.find_element_by_xpath('//img[@node-type="verifycode_image"]')
    img_url = res.get_attribute('src')
    print('出现验证码: ',img_url)
    response = requests.get(img_url)
    with open('Verification.png', 'wb') as f:
        f.write(response.content)
    verify = input('输入验证码:  ')
    driver.find_element_by_tag_name('verifycode').send_keys(verify)
    driver.find_element_by_class_name('W_btn_a').click()

# 将渲染页面写入文件
# print('写入文件...')
# sleep(5)
# with open('detile.html','wb') as f:
#     f.write(driver.page_source.encode('utf-8'))
# ''''''

# 截屏 验证无界面
print('截屏中...')
sleep(3)
driver.get_screenshot_as_file("shotpic.png")

