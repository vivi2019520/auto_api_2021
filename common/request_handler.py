#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:request_handler.py
@time:2021/05/13
"""

import requests


class RequestHandler:

    def __init__(self):
        """session管理器"""
        self.session = requests.session()

    def request(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        result = self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)
        if result.json():
            return result.json()
        else:
            return result.text

    # def request(self,req):
    #     return self.session.request(**req)

    def close_session(self):
        """关闭session"""
        self.session.close()


# if __name__ == '__main__':
#     req = RequestHandler()
#     url = "http://47.112.173.188:7300/api/u/login"
#     payload = {"name":"vivi","password":"123456"}
#     # header = {
#     #     "Content-Type": "application/json;charset=UTF-8"
#     # }
#     response = req.request(method="post", url=url, json=payload)
#     print(response.json())
