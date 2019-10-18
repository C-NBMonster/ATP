# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: urls.py
@time: 2019/10/15 14:47
@desc: 
"""

from django.urls import path
from apps.project_01 import views as p1View

urlpatterns = [

    # 用例管理
    path('load_cases/', p1View.load_cases),
    path('caseEdit_get/', p1View.caseEdit_get),
    path('caseEdit_save/', p1View.caseEdit_save),
    path('case_delete/', p1View.caseDelete),
    path('appFunc_run/', p1View.appFunc_run),
    path('runApp_history/', p1View.runApp_history),
    # 运行app功能测试
    path('load_appRunSet/', p1View.load_appRunSet),
    path('pop_add/', p1View.pop_add),
    path('appRunSetAdd/', p1View.appRunSetAdd),
    path('appRunSetEdit_get/', p1View.appRunSetEdit_get),
    path('appRunSetEdit_save/', p1View.appRunSetEdit_save),

    # 运行web功能测试
    path('load_webFuncSet/', p1View.load_webFuncSet),
    path('add_webFuncSet/', p1View.add_webFuncSet),
    path('edit_webFuncSet/', p1View.edit_webFuncSet),
    path('runWeb_history/', p1View.runWeb_history),

    # 运行interface功能测试
    path('load_interface/', p1View.load_interface),
    # 测试报告
    path('load_report/', p1View.load_report),
    path('load_report/', p1View.load_report),
]
