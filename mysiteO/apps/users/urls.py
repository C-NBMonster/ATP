# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/3/21 10:57
@desc: 
"""
from django.conf.urls import include, url
from django.urls import path
from apps.users import views as userView

urlpatterns = [

        #用户管理
    path('show_member_list/', userView.show_member_list),
    path('member_add/', userView.member_add),
    path('member_del/', userView.member_del),
    path('member_edit/', userView.member_edit),
    path('member_password/', userView.member_password),
    #系统用户
    path('show_admin_list/', userView.show_admin_list),
    path('admin_edit/', userView.admin_edit),
    path('admin_role_add/', userView.admin_role_add),
    path('admin_role_edit/', userView.admin_role_edit),
    path('show_admin_role_list/', userView.show_admin_role_list),
    path('show_admin_cate_list/', userView.show_admin_cate_list),
    path('show_admin_rule_list/', userView.show_admin_rule_list),
    path('admin_rule_add/', userView.admin_rule_add),
    path('admin_rule_edit/', userView.admin_rule_edit),

]