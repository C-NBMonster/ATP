from django.shortcuts import render

# Create your views here.

# coding = utf-8
from django.shortcuts import render
from django.shortcuts import redirect

from apps.users import models as um
from apps.base import models as baseView
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt,requires_csrf_token,csrf_protect
from common.mysql import conn_mysql
conn = conn_mysql()
# Create your views here.
import  json, time
from _datetime import datetime
from time import mktime


def index(request):
    return render(request, 'index/home.html')


def rightContents(request):
    return render(request, 'index/welcome.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            return redirect('/index/index/')
            # try:
            #     user = um.UserInfo.objects.get(name=username)
            #     print(user)
            #     if user.password == password:
            #         return redirect('/index/index/')
            #     else:
            #         message = "密码不正确"
            # except:
            #     message = "用户不存在"
        return render(request, 'index/login.html', {"message": message})
    return render(request, 'index/login.html')


@login_required
def logout(request):
    return redirect('/index/login')


def welcome(request):
    return render(request, 'index/welcome.html')




