# coding = utf-8
from django.shortcuts import render
from django.shortcuts import redirect

from apps.users import models as um
from apps.app_project_base import models as baseView
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt,requires_csrf_token,csrf_protect
from common.mysql import conn_mysql
conn = conn_mysql()
# Create your views here.
import  json
from _datetime import datetime
from time import mktime

def index(request):
    pass
    return render(request, 'indexApp/indexcontents.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        print(username,password)
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            return redirect('/indexApp/index/')
            # try:
            #     user = um.User.objects.get(name=username)
            #     if user.password == password:
            #         return redirect('/indexApp/index/')
            #     else:
            #         message = "密码不正确"
            # except:
            #     message = "用户不存在"
        return render(request, 'indexApp/login.html', {"message": message})
    return render(request, 'indexApp/login.html')


@login_required
def logout(request):
    pass
    return render(request, 'indexApp/login.html')

