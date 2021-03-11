import sys
import pytest
import allure
from selenium import webdriver
sys.path.append('..')
from page_object.loginpage import LoginPage
from page_object.home_page import Home_Mainmodule , Home_Module
from page_object.ss_secondinput_page import Ss_SecondInput_InputSelect , Ss_SecondInput_Input
from page_object.bd_storemanage_page import  Bd_StoreManage

class Test_Cases():
    '''
        用例：
    '''
    def setup_class(self):
        self.driver = webdriver.Chrome()
        #登录页面实例化
        self.lg = LoginPage(self.driver)
        #【二级库入库】的实例化
        self.ss_si = Ss_SecondInput_Input(self.driver)
        #【库房管理】的实例化
        self.bd_sm = Bd_StoreManage(self.driver)

    def teardown_class(self):
        pass
    #---------------------------------------以上实例化&setup teardown，以下是用例-------------------------
    @pytest.mark.skip()
    def test_login(self):
        '''
            用例：登录
        '''
        #登录
        self.lg.login('admin','000000')
        self.lg.wait(2)
    
    # @pytest.mark.skip()
    def test_storeadd(self):
        '''
            用例：库房新增
        '''
        #打开库房新增
        self.bd_sm.sm_open_()
        #库房新增
        self.bd_sm.sm_add_('code1','name1','一级库','高值')
    
    @pytest.mark.skip()
    def test_inputstore(self):
        '''
            用例：二级库入库
        '''
        #打开二级库入库页面
        self.ss_si.si_open_()
        #查询
        self.ss_si.si_select_('2020-09-23' , '2021-02-23')
        #勾选并入库
        self.ss_si.si_storeinput_(1)    #选第一个复现框
    
    def test_001(self):
        pass
    def test_002(self):
        pass
    def test_003(self):
        pass


if __name__ == '__main__':
    pytest.main(['-s','-v','./test_case.py'])