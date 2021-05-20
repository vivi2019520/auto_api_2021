#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:logger_handler.py
@time:2021/05/13
"""

import logging
from common.yaml_handler import yaml_data
from config.path import Config


class LoggerHandler(logging.Logger):

    def __init__(self, name='root', level='DEBUG', file=None, format=None):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # # 定义一个日志收集器
        # self.logger = logging.getLogger(name)
        #
        # # 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
        # self.logger.setLevel(level)

        # 设置日志格式
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)

            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)

        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


# 从yaml配置文件中读取logging相关配置
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file=Config.log_path,
                       format=yaml_data['logger']['format'])
