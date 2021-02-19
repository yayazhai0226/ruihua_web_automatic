import sys
from time import sleep
sys.path.append('..')
from utils.seleniumtools import find_element , assert_element_exist
from selenium import webdriver

#1.打开网址
driver = webdriver.Chrome(executable_path ="../common/chromedriver.exe")
driver.maximize_window()
driver.get('https://baidu.com')

#2.把元素的定位方式先收集起来，在用自己封装的方法
search_imput = ('id','kw')
search_button = ('xpath','//*[@id="su"]')
search_result = ('xpath','//*[@id="2"]/h3/a')

find_element(driver , search_imput).send_keys('国家')
find_element(driver , search_button).click()
#方法一：这种判断方法是可以的
# res = find_element(driver , search_result).text
# assert res == '此地全面放开生育政策?国家卫健委回应'

#方法二：判断这个元素是否存在即可
#assert assert_element_exist(driver , search_result) is True

#
find_element(driver , search_result).click()
# #切换作用域：切换window
# print(driver.window_handles)    #s所有window的句柄
# driver.switch_to_window(driver.window_handles[-1])  #切换到最后一个窗口





sleep(10)
driver.quit()


