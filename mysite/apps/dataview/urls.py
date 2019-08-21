# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/5/13 10:46
@desc: 
"""
from django.urls import path
from apps.dataview import views as dView

urlpatterns = [

    path(r'load_dataview/', dView.load_dataview),

]
