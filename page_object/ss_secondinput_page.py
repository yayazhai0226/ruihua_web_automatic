import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage

class Ss_SecondInput_InputSelect(BasePage):
    def si_open_(self, url):
        #打开二级库入库页面
        self.open_(url)

class Ss_SecondInput_Input(BasePage):
    #主模块
    mmoduleloc = ('xpath','//div[text()="基础数据"]')
    #子模块
    moduleloc = ('xpath','//div[text()="库房管理"]')

    #有如下模块
    url = 'http://192.168.10.126:8040/#/home/hvcs-inventory/supply/2'
    #勾选入库按钮
    storeinputloc = ('xpath','//span[text()="勾选入库"]')
    #勾选入库库房选择
    storeloc = ('xpath','//label[@class="ng-tns-c7-4 ui-dropdown-label ui-inputtext ui-corner-all ng-star-inserted"]')
    #勾选入库_开始日期
    datebeginloc = ('xpath','//input[@class="ng-tns-c8-5 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
    #勾选入库_结束日期
    dateendloc = ('xpath','//input[@class="ng-tns-c8-6 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
    #查询按钮
    selectbuttonloc = ('xpath','//*[@id="ui-tabpanel-1"]/app-inbound-checked/form/p-button[1]/button/span')

    
    #列表复选框1
    selectorloc_1 = ('xpath','//div[@class="ui-chkbox-box ui-widget ui-state-default"]')
    #入库按钮
    inputbuttonloc = ('xpath','//button[@class="pull-right ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"]')
    
    def si_open_(self):
        #打开二级库入库页面
        self.open_('http://192.168.10.126:8040/#/home/hvcs-inventory/supply/2')

    def si_select_(self, datebegin , dateend):
        #点击勾选入库
        self.click_(self.storeinputloc)
        #选择库房
        #输入开始日期
        self.keys_input_(self.datebeginloc , datebegin)
        #输入结束日期
        self.keys_input_(self.dateendloc , dateend)
        #点击确定
        self.click_(self.selectbuttonloc)
        self.wait(2)
    def si_storeinput_(self,num):
        #点选耗材
        if num == 1:
            self.click_(self.selectorloc_1)
            self.wait(2)
        else:
            print('目前只设计了选择第一个复选框')
        #点击入库
        self.click_(self.selectbuttonloc)
        self.wait(10)

