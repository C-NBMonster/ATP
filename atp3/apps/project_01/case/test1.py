# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: u2Main.py
@time: 2019/7/19 11:46
@desc:
"""
import unittest
import time
import random
from mysql_pubtwo import MysqlUtiltwo
from oracle_pub import OracleUtil
from excel_pub import ExcelUtil
from InterfaceClass import APITest
from openpyxl import load_workbook
import uiautomator2 as u2
from API_Para import API_Parameters






def readData():
    Excel = ExcelUtil("./userinfos.xlsx", "a1")
    #造数据
    info = Excel.next()

    registered=[]
    for i in range(0,len(info)-1):
        if info[i] not in registered:
            registered.append(info[i])


    for i in range(0, len(registered)):
        ac = int(registered[i]["ACCOUNT_NO"])
        if ac % 2 != 0:
            #print(registered[i]["ACCOUNT_NO"])
            print(registered[i]["IDENT"])


def tt():
    d = u2.connect("721QEBR925Q45")
    d.app_start("com.giveu.shoppingmall")
    time.sleep(5)
    d.click(964, 1221)
    time.sleep(8)
    print(4)
readData()


