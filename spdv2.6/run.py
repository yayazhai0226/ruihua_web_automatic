import os
import pytest

if __name__ == '__main__':
    #运行测试用例
    pytest.main(['./testcase/test_case.py', '--alluredir', './result'])
    # #结果整理成报告html
    os.system('allure generate ./result -o ./report --clean')
    #打开网页报告
    os.system('allure open -h 127.0.0.1 -p 10086 ./report')