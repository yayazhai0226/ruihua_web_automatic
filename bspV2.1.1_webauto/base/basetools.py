"""
基类: 工具类，将常用的/与项目适配的相关函数，进行二次封装，变成自定义内容，便于测试调用
    存在的意义就是为了让页面对象类进行继承，从而获得基本的方法来实现页面的操作流程
常用项:
    访问url
    元素定位
    输入
    点击
    等待
    退出
"""
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait    # 用作显示等待：找元素的时候给点时间

# 创建基类
class BasePage(object):
    # 构造函数
    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open_(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 元素定位
    def locate_(self, loc, timeout=10):
        """
        方法名：元素定位
        参数：
            loc:定位属性单元，例如：('xpath','//a[@xpath="ke"]')
            timeout:显示等待，默认10秒
        返回值：一个元素
        """
        return WebDriverWait(self.driver, timeout).until(lambda s: s.find_element(*loc))

    # 元素定位s
    def locate_s(self, loc, timeout=10):
        """
            方法名：定位多个元素（当时实在没法精确定位使用）
            参数:
                loc:定位属性单元 例如： ('xpath','//a[@xpath="ke"]')
                timeout:显示等待，默认10秒
            返回值：
                多个元素
        """
        return WebDriverWait(self.driver, timeout).until(lambda s: s.find_elements(*loc))

    # 键盘操作（例如日期键盘）
    def keys_input_(self, loc, txt):
        self.locate_(loc).send_keys(Keys.CONTROL, 'a')   # 全选
        self.locate_(loc).send_keys(txt)                 # 输入值

    # 输入
    def input_(self, loc, txt):
        """
        输入
        :param loc:  输入框的定位
        :param txt: 输入的字符串
        :return:
        """
        self.locate_(loc).clear()
        self.locate_(loc).send_keys(txt)

    # 点击
    def click_(self, loc):
        self.locate_(loc).click()

    # 等待
    def wait_(self, time):
        sleep(time)

    # 关闭
    def quit_(self):
        self.driver.quit()

    # 最大化窗口
    def max_windows_(self):
        self.driver.maximize_window()

    # 跳转到最新的窗口
    def switch_to_windows_(self, num):
        """
        跳转到指定窗口
        :param num: 窗口号
        :return: 无
        """
        self.driver.switch_to.window(self.driver.window_handles[num])
