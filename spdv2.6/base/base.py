'''
基类: 工具类，将常用的/与项目适配的相关函数，进行二次封装，变成自定义内容，便于测试调用
    存在的意义就是为了让页面对象类进行继承，从而获得基本的方法来实现页面的操作流程
常用项:
    访问url
    元素定位
    输入
    点击
    等待
    退出
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #用作显示等待：找元素的时候给点时间
from  selenium.webdriver.common.keys import Keys

#创建基类
class BasePage(object):
    #driver = webdriver.Chrome()
    #构造函数
    def __init__(self,driver):
        self.driver = driver
    #访问url
    def open_(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    #元素定位
    def locate(self,loc,timeout=10):
        '''
            loc：定位属性单元 例如： ('xpath','//a[@xpath="ke"]')
            timeout:显示等待，默认10秒
        '''
        return WebDriverWait(self.driver , timeout).until(lambda s: s.find_element(*loc))
    #元素定位s
    def locate_s(self,loc,timeout=10):
        '''
            方法名：定位多个元素（当时实在没法精确定位使用）
            参数:
                loc:定位属性单元 例如： ('xpath','//a[@xpath="ke"]')
                timeout:显示等待，默认10秒
            返回值：
                多个元素
        '''
        return WebDriverWait(self.driver , timeout).until(lambda s: s.find_elements(*loc))
    #情空
    # def clear_(self,loc):
    #     self.locate(loc).clear()

    #键盘操作
    def keys_input_(self,loc,txt):
        self.locate(loc).send_keys(Keys.CONTROL,'a')
        self.locate(loc).send_keys(txt)

    #输入
    def input_(self,loc,txt):
        self.locate(loc).clear()
        self.locate(loc).send_keys(txt)
    #点击
    def click_(self,loc):
        self.locate(loc).click()
    #等待
    def wait(self , time):
        sleep(time)
    
    #关闭
    def quit_(self):
        self.driver.quit()

    #最大化窗口
    def maximize_window(self):
        self.driver.maximize_window()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path= '../common/chromedriver.exe')
    # driver.get('https://www.baidu.com')
    # driver.find_element_by_id('kw').clear()
    # driver.find_element_by_id('kw').send_keys('hi mom')
    bs = BasePage(driver)
    bs.open_('https://www.baidu.com')
    bs.input_(('xpath','//input[@id="kw"]'),'你好')
    sleep(3)
    bs.input_(('xpath','//input[@id="kw"]'),'hi mom')
    bs.open_('https://www.baidu.com/s?wd=send-keys(keys.control)&rsv_spt=1&rsv_iqid=0xa04a34d50009315c&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=62095104_19_oem_dg&rsv_dl=tb&rsv_enter=1&rsv_sug3=26&rsv_sug1=13&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=11760&rsv_sug4=16660')
    sleep(5)
    bs.quit_()