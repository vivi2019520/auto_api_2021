#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:conftest.py.py
@time:2021/05/25
"""

import pytest

from common.excel_handler import ExcelHandler
from common.request_handler import RequestHandler
from config.path import Config


@pytest.fixture(scope="session")
def recharge_fixture():

    req = RequestHandler()
    yield req
    req.close_session()
