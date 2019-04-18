# coding=utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JY_Android_AT
@file: forms.py
@time: 2019/3/27 11:31
@desc: 
"""


from django import forms

class machineAdd(forms.Form):
    uid = forms.CharField(max_length=10)
    phone_name = forms.CharField(max_length=30)
    m_name = forms.CharField(max_length=50)
    sys = forms.CharField(max_length=20, widget=forms.Select)
    sysverson = forms.CharField(max_length=15, widget=forms.DateInput)
    createby = forms.CharField(max_length=20)
    c_time = forms.DateTimeField()
    status = forms.CharField(max_length=10)