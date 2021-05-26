#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:conftest.py.py
@time:2021/05/25
"""

import pytest
from common.request_handler import RequestHandler
from common.yaml_handler import yaml_data
from jsonpath import jsonpath


@pytest.fixture(scope="session")
def token_fixture():
    req = RequestHandler()
    res = req.request(method="post", url=yaml_data["host"]["dev_url"] + "/member/login",
                      headers={"X-Lemonban-Media-Type": "lemonban.v2"}, json=yaml_data["user"])
    token_type = jsonpath(res, "$..token_type")[0]
    token_result = jsonpath(res, "$..token")[0]
    final_token = token_type + " " + token_result
    return final_token

