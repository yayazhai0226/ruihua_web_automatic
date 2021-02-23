import sys
import pytest
sys.path.append('..')
from time import sleep
from selenium import webdriver
from utils.base_page import BasePage

#类实例化
driver = BasePage()
class Test():
    def test_open_loginpath(self):
        #打开网址&最大化窗口
        url = 'http://192.168.10.126:8040/#/login'
        #--------------------------------------
        driver.open_(url)
        driver.maximize_window()
    def test_lodin(self):
        accountNameloc = ('name','accountName')
        accountName = 'admin'
        passpordloc = ('name','password')
        passpord = '000000'
        comfirmloc = ('id','login')
        #--------------------------------------
        #输入用户名密码，并点登录
        driver.input_(accountNameloc,accountName)
        driver.input_(passpordloc,passpord)
        driver.click_(comfirmloc)
    def test_basedata(self):
        #点击基础数据
        driver.click_(('xpath','//div[text()="基础数据"]'))

    def test_basedata_stage(self):
        #点击库房管理
        driver.wait(1)
        moduleloc = ('xpath','//div[text()="库房管理"]')
        #--------------------------------------
        driver.click_(moduleloc)

    def test_basedata_stage_addbutton(self):
        #点击新增
        addbutton = ('xpath','//span[@class="fa fa-plus ui-clickable ui-button-icon-left ng-star-inserted"]')
        #--------------------------------------
        driver.click_(addbutton)

    def test_basedata_stage_addinput(self):
        #输入参数值
        aloc = ('xpath','//input[@name="storehouse.sthCode"]')
        a = 'code001'
        bloc = ('xpath','//input[@name="storehouse.sthName"]')
        b = 'name001'
        cloc = ('xpath','//div[@class="ng-tns-c3-7 ui-dropdown ui-widget ui-state-default ui-corner-all ui-helper-clearfix"]')
        dloc = ('xpath','//span[@class="ng-tns-c3-7 ng-star-inserted"]')
        eloc = ('xpath','//label[@class="ng-tns-c3-8 ui-dropdown-label ui-inputtext ui-corner-all ui-placeholder ng-star-inserted"]')
        floc = ('xpath','//span[@class="ng-tns-c3-8 ng-star-inserted"]')
        gloc = ('xpath','//input[@name="storehouse.address"]')
        g = 'address001'
        #--------------------------------------
        driver.input_(aloc,a)
        driver.input_(bloc,b)
        driver.click_(cloc)
        driver.locate_s(dloc)[0].click()
        driver.click_(eloc)
        driver.locate_s(floc)[0].click()
        driver.input_(gloc,g)

    def test_basedata_stage_addsave(self):
        #点击保存
        savebutton = ('xpath','//span[text()="保存"]')
        #--------------------------------------
        driver.click_(savebutton)

    def test_xxx_wait(self):
        #调试用等待&退出
        sleep(10)
        driver.quit()

if __name__ == '__main__':
    pytest.main(['-s' , '-v','./test_02spd2_6.py'])    #-s：小点；-v展示用例名称；