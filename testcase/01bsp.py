import sys
from time import sleep
sys.path.append('..')
from utils.seleniumtools import find_element , assert_element_exist ,notselect_click
from selenium import webdriver
url = 'http://47.94.220.173/#/show'

#1.打开网址
driver = webdriver.Chrome(executable_path ="../common/chromedriver.exe")
driver.maximize_window()
driver.get(url)

#2.把元素的定位方式先收集起来，在用自己封装的方法(只用xpath id 属性的value值)
#平台登录
login_name = '//input[@name = "phoneNo"]'
login_pwd = '//input[@name = "password"]'
login_but = '//button[@id= "login"]'
#点击bsp
bsp_select = '//a[@class= "content__block ng-star-inserted"]'
#bsp登录
bsplogin_name = '//input[@name = "accountName"]'
bsplogin_pwd = '//input[@name = "password"]'
bsplogin_but = '//button[@id= "login"]'
#基础数据
base_data = '//div[text()="基础数据"]'
#区域管理
base_data_area = '/html/body/app-root/app-home/div/app-sidebar-menu/div/nav/ul/app-menu-item[1]/li/ul/li[7]/app-menu-item/li/a/div/span'
area_add = '//button[@class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-icon-left ng-star-inserted"]'
area_add_name = '//input[@id="areaName"]'
area_add_code = '//input[@id="areaCode"]'
area_add_hiscode = '//input[@id="hisCode"]'
area_add_sys = '//span[@class="ui-multiselect-label ui-corner-all"]'
area_add_sys_need_list = ('//span[text() = "远程手术指导系统"]','//span[text() = "协同任务管理系统"]')
area_add_sys_close = '//a[@class="ui-multiselect-close ui-corner-all"]'
area_add_area_scope = '//i[@class="pi pi-chevron-down"]'
area_add_area_scope_need_list = ('//span[text()="外科"]','//span[text()="口腔科"]','//span[text()="胸外科"]')
area_add_area_scope_close = '//div[@class="tree-input tree-input-active"]'
area_add_area_save = '//span[text()="保存"]'
area_add_area_saveok = '//span[@class="ui-button-icon-left ui-clickable pi pi-check"]'


#平台登录
find_element(driver , login_name).send_keys('bsp1')
find_element(driver , login_pwd).send_keys('111111')
find_element(driver , login_but).click()
#点击bsp
find_element(driver , bsp_select).click()
#跳转到最新的网页，bsp登录
driver.switch_to.window(driver.window_handles[-1])
#print(driver.title) #查看是否跳转成功
find_element(driver , bsplogin_name).send_keys('bsp1')
find_element(driver , bsplogin_pwd).send_keys('111111')
find_element(driver , bsplogin_but).click()
#基础数据
find_element(driver , base_data).click()
#区域管理-add
sleep(2)    #【疑问】不清楚为啥要等待一会儿才能找到如下这个元素。。。。
find_element(driver , base_data_area).click()
find_element(driver , area_add).click()

#add
#输入
find_element(driver , area_add_name).send_keys('name')
find_element(driver , area_add_code).send_keys('code')
find_element(driver , area_add_hiscode).send_keys('hiscode')
#选择
notselect_click(driver , area_add_sys , area_add_sys_need_list)
find_element(driver , area_add_sys_close).click()
notselect_click(driver , area_add_area_scope , area_add_area_scope_need_list)
find_element(driver , area_add_area_scope_close).click()
#点击保存
find_element(driver , area_add_area_save).click()
#关闭成功提示框
find_element(driver , area_add_area_saveok).click()



#方法一：这种判断方法是可以的
# res = find_element(driver , search_result).text
# assert res == '此地全面放开生育政策?国家卫健委回应'

#方法二：判断这个元素是否存在即可
#assert assert_element_exist(driver , search_result) is True

#find_element(driver , search_result).click()
# #切换作用域：切换window
# print(driver.window_handles)    #s所有window的句柄
# driver.switch_to_window(driver.window_handles[-1])  #切换到最后一个窗口





sleep(10)
driver.quit()


