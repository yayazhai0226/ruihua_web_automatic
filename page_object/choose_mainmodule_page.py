
import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage

class Choose_MainModule_Page(BasePage):
    #有如下模块
    url = 'http://192.168.10.126:8040/#/home'
    m1 = ('xpath','//div[text()="基础数据"]')
    # m2 = ''
    m3 = ('xpath','//div[text()="二级库管理"]')
    # m4 = ''
    # m5 = ''
    # m6 = ''
    # m7 = ''
    # m8 = ''
    def teardown_class(self):
        sleep(2)
    def choose_mainmodule(self,modulename):
        try:
            if modulename == "基础数据":
                self.click_(self.m1)
            # elif modulename == '一级库管理':
            #     self.click_(self.m2)
            elif modulename == '二级库管理':
                self.click_(self.m3)
            # elif modulename == '字典管理':
            #     self.click_(self.m4)
            # elif modulename == '患者管理':
            #     self.click_(self.m5)
            # elif modulename == '综合统计查询':
            #     self.click_(self.m6)
            # elif modulename == '系统管理':
            #     self.click_(self.m7)
            # elif modulename == '紧急抢救补录':
            #     self.click_(self.m8)
            else:
                print('选择的模块不存在')
        except Exception as e:
            print('选择主模块页面错误:',e)

