# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: add.py
@time: 2019/6/26 19:34
@desc: 
"""
import time, datetime
import pymysql.cursors
import random
from excel_pub import ExcelUtil
mysql_info = {"host": 'localhost',
              "port": 3306,
              "user": 'root',
              "passwd": 'cjx123456',
              "db": 'atp',
              "charset": 'utf8'}


class MysqlUtil():
    '''
    mysql数据库相关操作
    连接数据库信息：mysql_info
    创建游标：mysql_execute
    查询某个字段对应的字符串：mysql_getstring
    查询一组数据：mysql_getrows
    关闭mysql连接：mysql_close
    '''

    def __init__(self, mysql_info=mysql_info):
        self.Excel = ExcelUtil("D:\\5435.xlsx", "ai")
        self.db_info = mysql_info
        u'''连接池方式'''
        self.conn = MysqlUtil.__getConnect(self.db_info)

    @staticmethod
    def __getConnect(db_info):
        '''静态方法，从连接池中取出连接'''
        try:
            conn = pymysql.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db'],
                                   charset=db_info['charset'])
            return conn
        except Exception as a:
            print("数据库连接异常：%s" % a)

    def mysql_execute(self, sql):
        '''执行sql语句'''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
        except Exception as a:
            self.conn.rollback()  # sql执行异常后回滚
            print("执行SQL语句出现异常：%s" % a)
        else:
            cur.close()
            self.conn.commit()  # sql无异常时提交

    def cdata(self):

        constT = 500
        phoneO = 15433331001
        info = self.Excel.next()
        st = []
        #for i in range(0, constT):
        for k in info:
            tt = int(k["ACCOUNT_NO"])
            ti = k["IDENT"]
            print(k)

                    #st = 'INSERT INTO CD(phone,bankNo,ident) VALUES (' + str(phoneO) + str(tt)+str(ti)+ ')'
                # if ti[-1] == "X":
                #     pass
                # else:
                #     sql = st+str(ti)+ ')'
                    #self.mysql_execute(st)
            #phoneO = phoneO + 2


        # for j in info:
        #     if j["IDENT"][-1] == "X":
        #         print("身份证尾号是X")
        #     else:
        #         tt = int(j["IDENT"])
        #         sql = 'INSERT INTO CD(ident) VALUES(' + str(tt) + ')'
        #         self.mysql_execute(sql)
        # print("ident Done!")

if __name__ == "__main__":
    cda = MysqlUtil()
    cda.cdata()
