#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:test_login.py
@time:2021/05/13
"""
import json
import unittest
from common.excel_handler import ExcelHandler
from common.request_handler import RequestHandler
import ddt
from common.logger_handler import logger
from config.path import Config
from common.yaml_handler import yaml_data


@ddt.ddt
class TestLogin(unittest.TestCase):
    excel = ExcelHandler(Config.case_data_path)
    data = excel.read_excel("login")

    def setUp(self):
        self.req = RequestHandler()

    def tearDown(self):
        self.req.close_session()

    @ddt.data(*data)
    def test_login(self, items):
        logger.info('*'*88)
        logger.info("当前是第{}条用例：{}".format(items['case_id'],items['case_title']))
        logger.info("当前用例的测试数据：{}".format(items))
        res = self.req.request(method=items["method"], url=yaml_data["host"]["dev_url"]+items["url"], headers=json.loads(items['headers']),
                               json=json.loads(items["payload"]))
        print(res.json()["code"])
        print(items["expected_result"])
        try:
            self.assertEqual(res.json()["code"], items["expected_result"])
        except Exception as e:
            logger.error("用例执行失败：{}".format(e))
            raise e


if __name__ == '__main__':
    unittest.main()
