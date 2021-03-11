from base.basetools import BasePage

class Bsp_Login(BasePage):
    def bsp_login(self, username, password):
        try:
            self.input_(('xpath', '//input[@name="accountName"]'), username)
            self.input_(('xpath', '//input[@name="password"]'), password)
            self.click_(('xpath', '//button[@class="ui-button-info"]'))
        except Exception as e:
            print('bsp登录页面错误', e)


