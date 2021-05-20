#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:run_test.py
@time:2021/05/20
"""
import os
import unittest
import time

from libs.HTMLTestRunnerNew import HTMLTestRunner
from config.path import Config

# 加载器
testloader = unittest.TestLoader()
suite = testloader.discover(Config.case_path)
# 通过模块名，类名

# 测试报告
ts = str(int(time.time()))
file_name = 'test_result_{}.html'.format(ts)
file_path = os.path.join(Config.report_path, file_name)

with open(file_path, 'wb') as f:
    # 使用 HTMLTestRunner
    runner = HTMLTestRunner(f, title="接口测试报告", description='第一个版本')
    runner.run(suite)
