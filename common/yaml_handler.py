#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:yaml_handler.py
@time:2021/05/13
"""

import yaml
from config.path import Config


class YamlHandler:

    def __init__(self, file):
        self.file = file

    def read_yaml(self):
        with open(self.file) as f:
            return yaml.load(f.read(), Loader=yaml.Loader)

    def write_yaml(self, data):
        with open(self.file, mode="w") as f:
            return yaml.dump(data, stream=f, allow_unicode=True)


yaml_data = YamlHandler(Config.config_yaml_path).read_yaml()
