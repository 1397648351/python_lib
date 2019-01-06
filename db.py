# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2018/12/27 23:13
# @Author : WuZe
# @Desc   :
# ==================================================

import pymysql.cursors


class DB:
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "db": "base",
        "charset": "utf8"
    }

    def __init__(self):
        self.version = '1.0'

    @classmethod
    def doTrans(cls, sqlList):
        """
        执行事务
        :param sqlList: sql集合
        :return: 影响行数
        """
        i = 0
        connection = pymysql.connect(**cls.config)
        cur = connection.cursor()
        try:
            for sql in sqlList:
                cur.execute(sql)
                i = i + 1
            connection.commit()
        except Exception as e:
            print 'error:', sqlList[i]
            i = 0
            connection.rollback()
            raise e
        finally:
            connection.close()
        return i

    @classmethod
    def execute(cls, sql):
        """
        执行一条sql
        :param sql: 需要执行的sql
        :return: 影响行数
        """
        connection = pymysql.connect(**cls.config)
        cur = connection.cursor()
        try:
            num = cur.execute(sql)
            connection.commit()
        except Exception as e:
            num = 0
            connection.rollback()
            raise e
        finally:
            connection.close()
        return num

    @classmethod
    def fetchall(cls, sql):
        """
        根据sql返回集合
        :param sql: 需要执行的sql
        :return: 集合
        """
        # print cls.config
        connection = pymysql.connect(**cls.config)
        cur = connection.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except Exception as e:
            raise e
        finally:
            connection.close()

    @classmethod
    def fetchone(cls, sql):
        """
        根据sql返回第一个
        :param sql: 需要执行的sql
        :return: 结果
        """
        connection = pymysql.connect(**cls.config)
        cur = connection.cursor()
        try:
            cur.execute(sql)
            result = cur.fetchone()
            return result
        except Exception as e:
            raise e
        finally:
            connection.close()
