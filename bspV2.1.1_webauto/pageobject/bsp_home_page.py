from selenium import webdriver
from base.basetools import BasePage
from base.yamltools import YamlTools
ytools = YamlTools()
class Home(BasePage):
    def home_page(self):
        """
        进入页面：bsp首页
        :return: 无
        """
        pass
        # home_page_url = ytools.yaml_read('../data/page_url.yaml')['bsp首页']
        # print(home_page_url)
        # self.open_(home_page_url)

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='../common/chromedriver.exe')
    home = Home(driver)
    home.home_page()
