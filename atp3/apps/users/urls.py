# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/10/15 15:11
@desc: 
"""


from django.urls import path
from apps.users import views as uView

urlpatterns = [

    path(r'load_member/', uView.load_member),
    path(r'pop_memberInfo/', uView.pop_memberInfo),
    path(r'member_edit_get/', uView.member_edit_get),
    path(r'member_edit_save/', uView.member_edit_save),
    path(r'member_add/', uView.member_add),

    path(r'loadAdmin/', uView.loadAdmin),
    path(r'loadRole/', uView.loadRole),
    path(r'loadRule/', uView.loadRule),
    path(r'loadAdminGroup/', uView.loadAdminGroup),

]