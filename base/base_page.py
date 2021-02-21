'''
    基类：工具类，将常用的相关函数，编程自定义模块，便于测试调用
        存在的意义是为了让页面对象类进行继承，从而获得基本方法来实现页面的操作流程
    常用项：
        访问url
        元素定位
        输入
        点击
        退出
        等待
'''
from selenium import webdriver
from time import sleep
#创建基类
class BasePage:
    driver = webdriver.Chrome()
    #构造函数
    def __init__(self , driver):
        self.driver = driver

    #访问url
    def open(self , url):
        self.driver.get(url)
    
    #元素定位
    def locator(self , loc):
        return self.driver.find_element(*loc)

    #输入
    def input_(self , loc , txt):
        self.locator(loc).send_keys(txt)
    
    #点击
    def click(self , loc):
        self.locator(loc).click()
    
    #等待
    def wait(self , time_):
        sleep(time_)

    #关闭
    def quit(self):
        self.driver.quit()

