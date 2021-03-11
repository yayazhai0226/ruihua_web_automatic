from base.basetools import BasePage
from base.yamltools import YamlTools
ytools = YamlTools()
class Platform_Home(BasePage):
    page_urllist = ytools.yaml_read('../data/page_url.yaml')
    def platform_home(self, username, password):
        self.open_(self.page_urllist['平台首页'])

    def platform_choosesys(self, modulename):
        if modulename == '基础服务平台':
            self.click_(('xpath', '//span[text()="基础服务平台"]'))
        else:
            print("暂时不支持其他系统，请选择：基础服务平台")