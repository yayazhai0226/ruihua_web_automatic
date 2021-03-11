from base.basetools import BasePage
from base.yamltools import YamlTools
ytools = YamlTools()
class Platform_Login(BasePage):
    page_urllist = ytools.yaml_read('../data/page_url.yaml')
    def platform_login(self, username, password):
        self.open_(self.page_urllist['平台登录'])
        self.input_(('xpath', '//input[@name="phoneNo"]'), username)
        self.input_(('xpath', '//input[@name="password"]'), password)
        self.click_(('xpath', '//button[@id="login"]'))