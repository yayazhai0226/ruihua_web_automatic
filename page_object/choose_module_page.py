
import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage

class Choose_Module_Page(BasePage):
    #有如下模块
    url = 'http://192.168.10.126:8040/#/home'
    m1 = ('xpath','//div[text()="二级库入库"]')
    def choose_module(self,modulename):
        try:
            if modulename == "二级库入库":
                self.click_(self.m1)
            else:
                print('选择的模块不存在')
        except Exception as e:
            print('选择主模块页面错误:',e)
