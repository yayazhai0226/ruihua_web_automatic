from selenium import webdriver
from time import sleep

url = 'http://192.168.10.126:8040/#/login'

#创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome(executable_path ="../common/chromedriver.exe")
#隐式等待：对全局进行控制
driver.implicitly_wait(6)

#通过浏览器向服务器发送URL请求
driver.get(url)
#刷新
driver.refresh()
#最大化浏览器
driver.maximize_window()
#输入账号密码
driver.find_element_by_name('accountName').send_keys('admin')
driver.find_element_by_name('password').send_keys('000000')
#点击登录
driver.find_element_by_id('login').click()
#进入模块
driver.find_element_by_xpath('/html/body/app-root/app-home/div/app-sidebar-menu/div/nav/ul/app-menu-item[1]/li/a/div').click()
#进入子模块
driver.find_element_by_xpath('/html/body/app-root/app-home/div/app-sidebar-menu/div/nav/ul/app-menu-item[1]/li/ul/li[3]/app-menu-item/li/a').click()





#固定等待
sleep(6)
#返回上一页
# driver.back()
#切换到下一页
# driver.forward()
#退出
driver.quit()