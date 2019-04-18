# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/3/21 11:00
@desc: 
"""
from django.conf.urls import include, url
from django.urls import path
from apps.app_project_01 import  views as  pro01_View

urlpatterns = [

    # 用例管理
    path('show_appFunc_swap/', pro01_View.show_appFunc_swap),
    path('load_appFunc/', pro01_View.load_appFunc),
    # 运行app功能测试
    path('show_appFuncSet_swap/', pro01_View.show_appFuncSet_swap),
    path('load_appFuncSet/', pro01_View.load_appFuncSet),
    path('add_appFuncSet/', pro01_View.add_appFuncSet),
    path('edit_appFuncSet/', pro01_View.edit_appFuncSet),
    path('runApp_history/', pro01_View.runApp_history),
    # 运行web功能测试
    path('show_webFunc_swap/', pro01_View.show_webFuncSet_swap),
    path('load_webFuncSet/', pro01_View.load_webFuncSet),
    path('add_webFuncSet/', pro01_View.add_webFuncSet),
    path('edit_webFuncSet/', pro01_View.edit_webFuncSet),
    path('runWeb_history/', pro01_View.runWeb_history),

    # 运行interface功能测试
    path('show_interface_swap/', pro01_View.show_interface_swap),
    path('load_interface/', pro01_View.load_interface),
    # 测试报告
    path('show_report_swap/', pro01_View.show_report_swap),
    path('load_report/', pro01_View.load_report),


]