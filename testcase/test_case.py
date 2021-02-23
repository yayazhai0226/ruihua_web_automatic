import sys
import pytest
from selenium import webdriver
sys.path.append('..')
from page_object.loginpage import LoginPage
from page_object.choose_mainmodule_page import Choose_MainModule_Page
from page_object.choose_module_page import Choose_Module_Page
from page_object.tworespmanage_tworespinput_page import Tworespmanage_Tworespinput_Page

class Test_Cases():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        #登录页面实例化
        self.lg = LoginPage(self.driver)
        #点击主模块实例化
        self.ch_mm = Choose_MainModule_Page(self.driver)
        #点击子模块实例化
        self.ch_m = Choose_Module_Page(self.driver)
        #点击【二级库入库】内的元素
        self.two_two_choose = Tworespmanage_Tworespinput_Page(self.driver)

    def teardown_class(self):
        pass
    def test_login(self):
        self.lg.login('admin','000000')

    def test_tworesp_input(self):
        self.ch_mm.choose_mainmodule('二级库管理')
        self.ch_mm.wait(2)
        self.ch_m.choose_module('二级库入库')
        self.two_two_choose.choose('勾选入库')
        self.two_two_choose.t_t_click_('勾选入库_开始日期')
        self.two_two_choose.t_t_click_('勾选入库_结束日期')
        self.two_two_choose.t_t_click_('勾选入库_查询')



if __name__ == '__main__':
    pytest.main(['-s','-v','./test_case.py'])
