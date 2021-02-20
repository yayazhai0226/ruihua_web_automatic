import sys
sys.path.append('..')
from time import sleep
from selenium import webdriver
from utils.seleniumtools import find_element , assert_element_exist , hover

url = 'http://192.168.10.126:8040/#/login'#地址
driver = webdriver.Chrome(executable_path='../common/chromedriver.exe')#获取句柄
driver.get(url)#访问
driver.maximize_window()#最大化窗口

se_username = ('name','accountName')    #账户
se_password = ('name','password')       #密码
cl_denglu = ('id','login')              #登录
cl_basedata = ('xpath','/html/body/app-root/app-home/div/app-sidebar-menu/div/nav/ul/app-menu-item[1]/li/a')#基础数据
cl_repository = ('link text','库房管理')#库房管理
cl_add = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/form/span/p-button[1]/button/span[2]')#新增
cl_add_window = ('class name','ui-dialog-content ui-widget-content')#新增窗口
se_repo_code = ('class name','ui-grid-col-8')
se_repo_name = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[2]/div[2]/input')
cl_repo_grade = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[3]/div[2]/p-dropdown/div/label')
cl_repo_grade_child = ('xpath','/html/body/app-root/app-home/div/main/div/app-basic/app-storehouse/p-dialog[1]/div/div[2]/form/div[3]/div[2]/p-dropdown/div/div[3]/div/ul/li[1]')
se_repo_code = ('xpath','')
se_repo_code = ('xpath','')





find_element(driver , se_username).send_keys('admin')#账户
find_element(driver , se_password).send_keys('000000')#密码
find_element(driver , cl_denglu).click()#登录
find_element(driver , cl_basedata).click()#基础数据
#hover(cl_basedata)#鼠标悬停
find_element(driver , cl_repository).click()#仓库管理
find_element(driver , cl_add).click()#新增
find_element(driver , se_repo_code).send_keys('000000')#编码
find_element(driver , se_repo_name).send_keys('000000')#名称
find_element(driver , cl_repo_grade).click()#级别
find_element(driver , cl_repo_grade_child).click()#级别下拉







sleep(60)
#driver.quit()