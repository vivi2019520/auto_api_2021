#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:path.py
@time:2021/05/19
"""

import os


class Config:
    # 项目根路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path,'data')

    # 测试数据文件路径
    case_data_path = os.path.join(data_path, 'cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path,'test_cases')

    # log文件路径
    log_path = os.path.join(root_path,'log/log.txt')

    # 报告路径
    report_path = os.path.join(root_path,'report')

    # config路径
    config_path = os.path.join(root_path,'config')

    # config.yaml路径
    config_yaml_path = os.path.join(config_path,'config.yaml')






