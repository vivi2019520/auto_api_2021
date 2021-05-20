#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ITester软件测试小栈
@file:db_handler.py
@time:2021/05/13
"""

import pymysql


class DBHandler:

    def __init__(self, host, port, user, password, database, charset, **kwargs):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,database=database,
                                    cursorclass=pymysql.cursors.DictCursor, charset=charset, **kwargs)

        self.cursor = self.conn.cursor()

    def execute_sql(self,sql,res_one=True):
        self.cursor.execute(sql)
        self.conn.commit()
        if res_one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


