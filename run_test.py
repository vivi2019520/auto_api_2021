import os

import pytest
import allure

if __name__ == '__main__':
    # 执行pytest单元测试，生成allure报告到allure_report下
    pytest.main(["-v", "--alluredir=./allure_report"])
    # 生成测试报告到report目录下
    os.system("allure generate ./allure_report -o ./report --clean")
