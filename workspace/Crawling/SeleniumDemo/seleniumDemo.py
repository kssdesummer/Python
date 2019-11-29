from selenium import webdriver
# 导入selenium库里的webdriver包
import time

# chromedriver.exe插件,与chrome的版本相对照
# driver = webdriver.Chrome(executable_path = R'D:chromedriver.exe') # 指定插件位置
# 推荐存放的位置是python安装路径下就行

'''
　　get_window_size() 　　　　获取浏览器大小
　　set_window_size() 　　　　设置浏览器位置
　　get_window_position() 　 　获取浏览器在屏幕上的坐标
　　set_window_position() 　 　设置浏览器在屏幕的位置　
　　maximize_window()  　　    最大化浏览器
'''

# 调用一个浏览器
driver = webdriver.Chrome()
# 请求网址
driver.get('http://www.baidu.com')
size = driver.get_window_size()
print(size['width'])
# 打印访问地址
print(driver.current_url)
# 通过id寻找元素,send_keys输入内容
driver.find_element_by_id('kw').send_keys('翻译')
time.sleep(1)
# click() 点击
driver.find_element_by_id('su').click()
time.sleep(3)
# 写入文件
with open('selenium.html', 'wb') as f:
    # 将请求数据写入,encode指定编码
    f.write(driver.page_source.encode('utf-8'))
