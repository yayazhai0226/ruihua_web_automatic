import sys
sys.path.append('..')
from time import sleep
from base.base import BasePage
class LoginPage(BasePage):
    #url
    url = 'http://192.168.10.126:8040/#/login'
    #页面元素
    user = ('name','accountName')
    pwd = ('name','password')
    button = ('id','login')

    #元素的操作
    def login(self,username , password):
        try:
            #访问url
            self.open_(self.url)
            #输入账号
            self.input_(self.user,username)
            #输入密码
            self.input_(self.pwd,password)
            #点击确定
            self.click_(self.button)
        except  Exception as e:
            print('登录页面错误',e)

    