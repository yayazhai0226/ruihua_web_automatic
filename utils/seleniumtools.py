from selenium.webdriver.support.ui import WebDriverWait #用作显示等待：找元素的时候给点时间

def find_element(driver , locator , timeout=10):
    '''
        方法名：DIY查找元素
        参数:
            driver:浏览器的句柄
            locator:元素的定位方式,格式:
                （'id','xxxx'）
                （'xpath','xxxx'）
                （'name','xxxx'）
                （'class name','xxxx'）
                （'css selector','xxxx'）
                （'link text','xxxx'）
                （'partial link text','xxxx'）
                （'id','xxxx'）
            timeout:超时时间，默认10
        返回值：
            -找到元素：返回元素
            -没找到元素：直接报错
    '''
    return WebDriverWait(driver , 10).until(lambda s: s.find_element(*locator))

def assert_element_exist(driver , locator , timeout=10):
    '''
        方法名：判断元素是否存在
        参数:
            driver:浏览器的句柄
            locator:元素的定位方式,格式:
                （'id','xxxx'）
                （'xpath','xxxx'）
                （'name','xxxx'）
                （'class name','xxxx'）
                （'css selector','xxxx'）
                （'link text','xxxx'）
                （'partial link text','xxxx'）
                （'id','xxxx'）
            timeout:超时时间，默认10
        返回值：
            -找到元素：True
            -没找到元素：False
    '''
    try:
        WebDriverWait(driver , 10).until(lambda s: s.find_element(*locator))
        return True
    except:
        return False
