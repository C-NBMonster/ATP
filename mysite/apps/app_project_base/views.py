from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from . import models
from . import forms
import json
import time
from datetime import datetime
# Create your views here.
from common.mysql import conn_mysql
conn = conn_mysql()

def show_machineInfo_swap(request):
    return render(request, 'app_project_base/machine_swap.html')

@cache_page(60 * 15)
def load_machineInfo_list(request, userid='538530'):
    #sql = "select * from app_project_base_machineinfo where uid= '%s'" % userid
    # 以下语句用于处理MySQL的时间转化为json数据的序列化问题
    # json.JSONEncoder.default = lambda self, obj: (obj.strftime('%Y-%m-%d %H:%M:%S')
    #                                               if isinstance(obj, datetime) else None)
    # mInfo = conn.mysql_getrows(sql)
    machine_info = models.machineinfo.objects.all()
    return render(request, 'app_project_base/machine-list.html', locals())
    # return render(request, 'app_project_base/machine-list.html', {
    #     'machine_info': json.dumps(mInfo),
    # })

def pop_machineInfo(request):
    return render(request, 'app_project_base/machine-add.html')

def machine_edit(request):
    return render(request, 'app_project_base/machine-edit.html')
def machine_add(request):
    p_name = request.GET["pho_name"]
    m_name = request.GET["m_name"]
    platform = request.GET["plateform"]
    s_version = request.GET["sys_version"]
    print(s_version)
    models.machineinfo.objects.create(uid=538530,
                                      phone_name=p_name,
                                      m_name=m_name,
                                      sys=platform,
                                      sysverson=s_version,
                                      createby="mirror",
                                      # c_time=time.strftime('%Y-%m-%d %H:%M:%S')
                                      )
    return redirect("/indexApp/index")
    # machine_info = models.machineinfo.objects.all()
    # return render(request, 'app_project_base/machine-list.html', locals())
def testAdd(request):
    # a = request.GET['p_name']
    # b = request.GET['m_name']
    # c = request.GET['platform']
    # d = request.GET['s_version']
    # print(a, type(b))
    # models.machineinfo.objects.create(uid=538530,
    #                                   phone_name=a,
    #                                   m_name=b,
    #                                   sys=c,
    #                                   sysverson=d,
    #                                   createBy="mirror",
    #                                   c_time=time.strftime('%Y-%m-%d %H:%M:%S')
    #                                   )
    return render(request, 'app_project_base/machine-list.html')



def show_appInfo_swap(request):
    return render(request, 'app_project_base/appInfo_swap.html')

def load_appInfo_list(request):
    app_info = models.appinfo.objects.all()
    return render(request, 'app_project_base/appInfo-list.html', locals())

def add_appInfo(request):
    return render(request, 'app_project_base/appInfo-add.html')

def edit_appInfo(request):
    return render(request, 'app_project_base/appInfo-edit.html')


def show_serverInfo_swap(request):
    return render(request, 'app_project_base/serverInfo_swap.html')

def load_serverInfo_list(request):
    server_info = models.serverinfo.objects.all()
    return render(request, 'app_project_base/serverInfo-list.html', locals())

def add_serverInfo(request):
    pass
def edit_serverInfo(request):
    return render(request, 'app_project_base/serverInfo-edit.html')
