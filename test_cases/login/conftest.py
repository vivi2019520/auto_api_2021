#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:conftest.py.py
@time:2021/05/25
"""

import pytest

from common.request_handler import RequestHandler


@pytest.fixture(scope="session")
def login_fixture():
    req = RequestHandler()
    yield req
    req.close_session()
