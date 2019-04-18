# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/3/21 11:02
@desc: 
"""
from django.conf.urls import include, url
from django.urls import path
from apps.app_project_base import views as baseView
from testF import  views as Tview

urlpatterns = [

    #手机信息
    path('show_machineInfo_swap/', baseView.show_machineInfo_swap),
    path('pop_machineInfo/', baseView.pop_machineInfo),
    path('load_machineInfo_list/', baseView.load_machineInfo_list),
    # path('machine_add/', baseView.machine_add),
    # path('machine_edit/', baseView.machine_edit),
    # path('testAdd/', baseView.testAdd),
    # path("testAdd/",Tview.testAdd),
    # path("machine_Tadd",Tview.machine_Tadd),
    #app信息
    path('show_appInfo_swap/', baseView.show_appInfo_swap),
    path('add_appInfo/', baseView.add_appInfo),
    path('edit_appInfo/', baseView.edit_appInfo),
    path('load_appInfo_list/', baseView.load_appInfo_list),
    #服务器信息
    path('show_serverInfo_swap/', baseView.show_serverInfo_swap),
    path('load_serverInfo_list/', baseView.load_serverInfo_list),
    path('add_serverInfo/', baseView.add_serverInfo),
    path('edit_serverInfo/', baseView.edit_serverInfo),

]