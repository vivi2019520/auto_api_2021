#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:test_login.py
@time:2021/05/13
"""
import json
from common.excel_handler import ExcelHandler
from common.logger_handler import logger
from config.path import Config
from common.yaml_handler import yaml_data
import pytest


class TestLogin:
    excel = ExcelHandler(Config.case_data_path)
    data = excel.read_excel("login")

    @pytest.mark.parametrize("data", data)
    def test_login(self, data, login_fixture):
        logger.info('*' * 88)
        logger.info("当前是第{}条用例：{}".format(data['case_id'], data['case_title']))
        logger.info("当前用例的测试数据：{}".format(data))
        res = login_fixture.request(method=data["method"], url=yaml_data["host"]["dev_url"] + data["url"],
                                    headers=json.loads(data['headers']), json=json.loads(data["payload"]))

        try:
            assert res["code"] == data["expected_result"]
        except Exception as e:
            logger.error("用例执行失败：{}".format(e))
            raise e


if __name__ == '__main__':
    pytest.main()
