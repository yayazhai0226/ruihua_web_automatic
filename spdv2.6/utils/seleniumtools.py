from selenium.webdriver.support.ui import WebDriverWait #用作显示等待：找元素的时候给点时间

def find_element(driver , locator_value , timeout=10):
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
    try:
        locator = ('xpath' , locator_value)
        return WebDriverWait(driver , timeout).until(lambda s: s.find_element(*locator))
    except:
        print('用xpath定位元素失败')
        
def assert_element_exist(locator , timeout=10):
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

def hover(locator):
    '''
        方法名：鼠标悬停
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
        返回值：
            -找到元素：True
            -没找到元素：False
    '''
    try:
        element = find_element(driver , locator)
        ActionChains(driver).move_to_element(element).perform()
        print('找到元素并悬停')    
    except:
        print('未找到元素')    

def notselect_click(driver , select_frist , select_later_list):
    '''
        方法名：常规下拉点选框（不是select类型的元素用）
        参数:
            driver:find_element默认参数
            select_frist:展开下拉框对应的元素属性值 例如：'aaaa'  "aaaa"
            select_later_list:下拉框需要点选的元素属性值列表 例如：('aa','bb','cc')
        返回值：
            无
    '''
    try:
        find_element(driver , select_frist).click()
    except:
        print('点击元素失败')
    try:
        for i in select_later_list:
            selected = find_element(driver , i).is_selected()
            if not selected:
                find_element(driver , i).click()
            else:
                pass
    except Exception as e:
        print("点选复选框失败",e)


