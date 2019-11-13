# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/10/15 15:10
@desc: 
"""

from django.urls import path
from apps.index import views as indexView

urlpatterns = [

    path(r'', indexView.index),
    path(r'rightContents/', indexView.rightContents),
    path('login/', indexView.login),
    path('logout/', indexView.logout),
    path('welcome/', indexView.welcome),
]