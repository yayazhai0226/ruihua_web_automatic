# import sys
# sys.path.append('..')
import pytest
from selenium import webdriver
from base.basetools import BasePage
from base.yamltools import YamlTools
from pageobject.bsp_login_page import Bsp_Login
from pageobject.platform_login_page import Platform_Login
from pageobject.platform_home_page import Platform_Home
from pageobject.bdata_courtyard_page import Courtyard


class Test_Case():
    # 前置
    def setup_class(self):
        """
        实例化页面类
        :return:无
        """
        # chrome驱动
        options = webdriver.ChromeOptions()
        options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument('origin="http://47.94.220.173"')
        options.add_argument('referer="http://47.94.220.173/bsp/"')
        self.driver = webdriver.Chrome(executable_path='../common/chromedriver.exe', chrome_options=options)
        # 实例化：基础
        self.base = BasePage(self.driver)
        # 实例化：平台登录
        self.pl = Platform_Login(self.driver)
        # 实例化：平台首页
        self.ph = Platform_Home(self.driver)
        # 实例化：bsp登录
        self.bl = Bsp_Login(self.driver)
        # 实例化：院区管理页面
        self.cy = Courtyard(self.driver)
        # 实例化：yaml工具
        self.ytools = YamlTools()
        # 页面地址列表
        self.pageurllist = self.ytools.yaml_read('../data/page_url.yaml')

        # 登录平台>选择基础平台>bsp登录(以备后续测试使用)
        self.base.open_(self.pageurllist['平台登录'])  # 打开平台登录页
        self.pl.platform_login('bsp1', '111111')  # 平台登录
        self.ph.platform_choosesys('基础服务平台')  # 打开bsp登录页——点选bsp系统
        self.base.switch_to_windows_(-1)  # 跳转到最新窗口
        self.bl.bsp_login('bsp1', '111111')  # bsp登录
        self.base.wait_(2)
        self.base.open_(self.pageurllist['院区管理'])   #打开院区管理页面

    # 后置
    def teardowm_class(self):
        pass

    # ...................................以上是前置setup后置teardown代码........................................
    # ...........................................以下是用例....................................................
    @pytest.mark.parametrize(('name', 'abbrname', 'code'), yaml_read('../data/test_case_bd_courtyard.yaml'))
    def test_courtyardadd(self):
        self.cy.add_('test_name', 'test_abbrname', 'test_code')

    def test_downloaddemo(self):
        # self.base.wait_(2)
        self.cy.downloaddemo_()

    def test_courtyardselect(self):
        # self.base.wait_(2)
        self.cy.select_('test', '全部')

    def test_courtyardstatus(self):
        # self.base.wait_(2)
        self.cy.status_()

    def test_courtyardupdate(self):
        # self.base.wait_(2)
        self.cy.update_()

    def test_courtyardlookup(self):
        # self.base.wait_(2)
        self.cy.lookup_()

    def test_courtyarddelete(self):
        # self.base.wait_(2)
        self.cy.delete_()

    def test_quit_(self):
        self.base.wait_(20)
        self.base.quit_()

if __name__ == '__main__':
    pytest.main(['-s', '-v', './test_case_bd_courtyard.py'])
