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
from apps.indexApp import views as indexView

urlpatterns = [

    path(r'index/', indexView.index),
    path('login/', indexView.login),
    path('logout/', indexView.logout),

]