import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage

class Tworespmanage_Tworespinput_Page(BasePage):
    #有如下模块
    url = 'http://192.168.10.126:8040/#/home/hvcs-inventory/supply/2'
    #勾选入库
    choose1 = ('xpath','//span[text()="勾选入库"]')
    #勾选入库_开始日期
    choose1_input_begindate = ('xpath','//input[@class="ng-tns-c8-5 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
    #勾选入库_结束日期
    choose1_input_enddate = ('xpath','//input[@class="ng-tns-c8-6 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
    #勾选入库_查询按钮
    choose1_button_select = ('xpath','//button[@class="ui-datepicker-trigger ui-calendar-button ng-tns-c8-2 ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ng-star-inserted"]')
    #勾选入库_复现框1
    choose1_selects_clk1 = ('xpath','//div[@class="ui-chkbox-box ui-widget ui-state-default"]') 
    
    def choose(self,modulename):
        try:
            if modulename == "勾选入库":
                self.click_(self.choose1)
            else:
                print('选择的元素不存在')
        except Exception as e:
            print('二级库入库点击“勾选入库”页面错误:',e)

    def t_t_click_(self , loc_name):
        try:
            if loc_name == "勾选入库_开始日期":
                self.input_(self.choose1_input_begindate,'2020-12-23')
            if loc_name == "勾选入库_结束日期":
                self.input_(self.choose1_input_enddate,'2020-12-23')
            if loc_name == "勾选入库_查询":
                self.click_(self.choose1_button_select)
            else:
                print('选择的元素不存在')
        except Exception as e:
            print('二级库入库内页面错误:',e)