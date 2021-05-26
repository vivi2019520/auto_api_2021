#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:db_handler.py
@time:2021/05/13
"""

import pymysql
from common.logger_handler import logger


class DBHandler:

    def __init__(self, host, port, user, password, database, charset, **kwargs):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                    cursorclass=pymysql.cursors.DictCursor, charset=charset, **kwargs)

        self.cursor = self.conn.cursor()

    def select_sql(self, sql, res_one=True):
        """查询操作"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        self.cursor.execute(sql)
        if res_one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def execute_sql(self, sql):
        """新增/插入/删除操作"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping(reconnect=True)
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.error("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()
