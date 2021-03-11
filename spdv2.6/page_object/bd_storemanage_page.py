import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage

class Ss_SecondInput_InputSelect(BasePage):
    def si_open_(self, url):
        #打开二级库入库页面
        self.open_(url)


class Bd_StoreManage(BasePage):
    #有如下模块
    #页面地址
    url = 'http://192.168.10.126:8040/#/home/basic/storehouse'
    #新增按钮
    addbuttonloc = ('xpath','//span[@class="fa fa-plus ui-clickable ui-button-icon-left ng-star-inserted"]')
    #库房编码
    codeloc = ('xpath','//input[@name="storehouse.sthCode"]')
    #库房名称
    nameloc = ('xpath','//input[@name="storehouse.sthName"]')
    #库房级别
    levelloc = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[3]/div[2]/p-dropdown/div/label')
    chooselevelloc = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[3]/div[2]/p-dropdown/div/div[3]/div/ul/li[1]/span')
    #库房类别
    typeloc = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[4]/div[2]/p-dropdown/div/label')
    choosetypeloc = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[4]/div[2]/p-dropdown/div/div[3]/div/ul/li[1]/span')
    #地址
    #管理科室
    #库房管理员
    #描述
    #是否启用
    #保存
    saveloc = ('xpath','//span[text()="保存"]')

    def sm_open_(self):
        #打开库房管理页面
        self.open_('http://192.168.10.126:8040/#/home/basic/storehouse')
    def sm_add_(self, code , name , level , type):
        #点击新增
        self.click_(self.addbuttonloc)
        #输入code
        self.input_(self.codeloc , code)
        #输入name
        self.input_(self.nameloc , name)
        #选择level
        if level == '一级库':
            self.click_(self.levelloc)
            self.click_(self.chooselevelloc)
        else:
            print('你选择的库房级别不存在')
        #选择type
        if type == '高值':
            self.click_(self.typeloc)
            self.click_(self.choosetypeloc)
        else:
            print('你选择的库房类别不存在')
        #点击保存
        self.click_(self.saveloc)

        
