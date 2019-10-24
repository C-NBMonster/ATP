
from django.views.decorators.cache import cache_page
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.db import transaction
from django.contrib.auth.decorators import login_required

from . import models

import time
import json


# Create your views here.
from common.mysql import conn_mysql
conn = conn_mysql()


#@cache_page(60 * 15) --加缓存时间
def load_machineInfo(request, userid='538530'):
    #获取机器信息
    mTotal = models.machineinfo.objects.count()
    #如果查询结果为空,django是会报错的，所以要添加以下判断
    if mTotal == 0:
        msg="您尚未添加机器信息！"
        return render(request, 'base/machineList.html', locals())
    else:
        machine_info = models.machineinfo.objects.filter(uid=userid).order_by('-id')
        return render(request, 'base/machineList.html', locals())



def pop_machineInfo(request):
    return render(request, 'base/machineAdd.html')

def machine_edit_get(request, userid='538530'):
    #获取当前行的信息，并传到machine_edit.html
    edit_info = models.machineinfo.objects.get(id=request.GET["id"])

    return render(request, 'base/machineEdit.html', locals())

def machine_edit_save(request):
    #保存编辑信息
    models.machineinfo.objects.filter(id=request.GET["id"]).update(
    phone_name=request.GET["pho_name"],
    m_name=request.GET["m_name"],
    sys=request.GET["platform"],
    sysverson=request.GET["sys_version"],
    status=request.GET["enable"],
    )
    return redirect('/base/load_machInfo')


def machine_add(request, userId=538530):
    #添加机器信息
    m = models.machineinfo.objects
    m.create(uid=userId,
             phone_name=request.GET["pho_name"],
             m_name=request.GET["m_name"],
             sys=request.GET["plateform"],
             sysverson=request.GET["sys_version"],
             createby="mirror",
              # c_time=time.strftime('%Y-%m-%d %H:%M:%S') mysql自动生成
              ).save()
    m.update()
    #return render(request, 'base/machine-list.html', {"msg": "添加机器成功！"})
    #return HttpResponseRedirect('/base/load_machineInfo_list')
    return redirect('/base/load_machineInfo')

def machine_delete(request):
    models.machineinfo.objects.get(id=request.GET["id"]).delete()
    return redirect('/base/load_machineInfo')


def load_appInfo(request, userid=538530):
    aTotal = models.appinfo.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if aTotal == 0:
        msg = "您尚未添加APP信息！"
        return render(request, 'base/appInfoList.html', locals())
    else:
        app_info = models.appinfo.objects.filter(uid=userid).order_by('-id')
        return render(request, 'base/appInfoList.html', locals())

def pop_appInfo(request):
    return render(request, 'base/appInfoAdd.html')


def add_appInfo(request, userid=538530):
    # 添加app信息
    m = models.appinfo.objects
    m.create(uid=userid,
             pro_name=request.GET["pro_name"],
             package =request.GET["pName"],
             activity=request.GET["activity"],
             createby="mirror",
             ).save()
    m.update()
    return redirect("/base/load_appInfo")


def edit_appInfo_get(request):
    # 获取当前行的信息，并传到machine_edit.html
    app_edit_info = models.appinfo.objects.get(id=request.GET["id"])
    return render(request, 'base/appInfoEdit.html', locals())


def edit_appInfo_save(request):
    models.appinfo.objects.filter(id=request.GET["id"]).update(
        pro_name = request.GET["pro_name"],
        package  = request.GET["pName"],
        activity = request.GET["activity"],
        status   = request.GET["enable"],
    )
    return redirect('/base/load_appInfo')

def app_delete(request):
    models.appinfo.objects.get(id=request.GET["id"]).delete()
    return redirect('/base/load_appInfo')


def load_serverInfo(request, userid=538530):
    sTotal = models.serverinfo.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if sTotal == 0:
        msg = "您尚未添加服务器信息！"
        return render(request, 'base/serverInfoList.html', locals())
    else:
        server_info = models.serverinfo.objects.filter(uid=userid).order_by('-id')
        return render(request, 'base/serverInfoList.html', locals())

def pop_serverInfo(request):
    return render(request, 'base/serverInfoAdd.html')

def add_serverInfo(request, userid=538530):
    # 添加app信息
    m = models.serverinfo.objects
    m.create(uid=userid,
             os=request.GET["os"],
             serverIP = request.GET["serverIP"],
             createby="mirror",
             ).save()
    m.update()
    return redirect('/base/load_serverInfo')


def edit_serverInfo_get(request):
    # 获取当前行的信息，并传到machine_edit.html
    server_edit_info = models.serverinfo.objects.get(id=request.GET["id"])
    return render(request, 'base/serverInfoList.html', locals())


def edit_serverInfo_save(request):
    models.serverinfo.objects.filter(id=request.GET["id"]).update(
        os       = request.GET["os"],
        serverIP = request.GET["serverIP"],
        status   = request.GET["enable"],
    )
    return redirect('/base/load_serverInfo')


def server_delete(request):
    models.serverinfo.objects.get(id=request.GET["id"]).delete()
    return redirect('/base/load_serverInfo')


