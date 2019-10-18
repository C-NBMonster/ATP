# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/10/15 15:08
@desc: 
"""

from django.urls import path
from apps.base import views as baseView


urlpatterns = [

    #手机信息
    path('pop_machineInfo/', baseView.pop_machineInfo),
    path('load_machineInfo/', baseView.load_machineInfo),
    path('machine_add', baseView.machine_add),
    path('machine_edit_get', baseView.machine_edit_get),
    path('machine_edit_save', baseView.machine_edit_save),
    path('machine_delete', baseView.machine_delete),
    #app信息
    path('load_appInfo/', baseView.load_appInfo),
    path('pop_appInfo/', baseView.pop_appInfo),
    path('add_appInfo/', baseView.add_appInfo),
    path('edit_appInfo_get/', baseView.edit_appInfo_get),
    path('edit_appInfo_save/', baseView.edit_appInfo_save),
    path('app_delete/', baseView.app_delete),
    #服务器信息
    path('load_serverInfo/', baseView.load_serverInfo),
    path('pop_serverInfo', baseView.pop_serverInfo),
    path('add_serverInfo/', baseView.add_serverInfo),
    path('edit_serverInfo_get/', baseView.edit_serverInfo_get),
    path('edit_serverInfo_save/', baseView.edit_serverInfo_save),
    path('server_delete/', baseView.server_delete),
]