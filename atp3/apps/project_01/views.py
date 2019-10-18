from django.shortcuts import render

# Create your views here.
# coding=utf-8

from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from apps.project_01.models import cases
from apps.project_01.case import u2Main
import unittest
# Create your views here.
#用例管理


def load_cases(request, userid=538530):
    case_info = cases.objects.filter(uid=userid).order_by("-id")
    l_case=[]
    for case in case_info:
        l_case.append(case)
    return render(request, 'project_01/caseList.html', locals())


def appFunc_run(request):

    suit=unittest.TestSuite()
    suit.addTest(u2Main.createData("test_createData"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    return HttpResponse("运行开始")


def caseEdit_get(request):
    # 获取当前行的信息，并传到app-runset-edit.html
    edit_info = cases.objects.get(id=request.GET["id"])
    return render(request, 'project_01/caseEdit.html', locals())


def caseEdit_save(request, userid=538530):
    m = cases.objects
    m.create(uid=userid,
             pro_name=request.GET["proName"],
             pho_name=request.GET["phoneName"],
             serverIP=request.GET["serverIP"],
             createby="mirror",
             ).save()
    m.update()
    return redirect('/project_01/load_cases')


def caseDelete(request):
    cases.objects.get(id=request.GET["id"]).delete()
    return redirect("/project_01/load_cases")


def runApp_history(request, userid=538530):
    hTotal = models.runHistory.objects.count()
    if hTotal == 0:
        msg = "没有运行历史信息！"
        return render(request, 'project_01/ra-history.html', locals())
    else:
        models.runHistory.objects.update()
        rh_info = models.runHistory.objects.filter(uid=userid).order_by('-id')
        return render(request, 'project_01/ra-history.html', locals())

#app运行配置
def load_appRunSet(request, userid=538530):
    rTotal = models.apprunset.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if rTotal == 0:
        msg = "您尚未添加APP运行配置信息！"
        return render(request, 'project_01/appRunsetList.html', locals())
    else:
        models.apprunset.objects.update()
        app_run = models.apprunset.objects.filter(uid=userid).order_by('-id')
        return render(request, 'project_01/appRunsetList.html', locals())


def pop_add(request, userid=538530):
    return render(request, "project_01/appRunetAdd.html", locals())


def appRunSetAdd(request, userid=538530):
    m = models.apprunset.objects
    m.create(uid=userid,
             pro_name=request.GET["proName"],
             pho_name=request.GET["phoneName"],
             serverIP=request.GET["serverIP"],
             createby="mirror",
             ).save()
    m.update()
    return redirect("/project_01/load_appRunSet")

def appRunSetEdit_get(request, userid=538530):
    # 获取当前行的信息，并传到app-runset-edit.html
    edit_info = cases.objects.get(id=request.GET["id"])
    return render(request, 'project_01/appRunetEdit.html', locals())

def appRunSetEdit_save(request, userid=538530):
    m = cases.objects
    m.create(uid=userid,
             pro_name=request.GET["proName"],
             pho_name=request.GET["phoneName"],
             serverIP=request.GET["serverIP"],
             createby="mirror",
             ).save()
    m.update()
    return redirect('/project_01/load_appRunSet')



#web运行配置

def load_webFuncSet(request):
    web_run = models.webrunset.objects.all()
    return render(request, 'project_01/webRunsetList.html', locals())
def add_webFuncSet(request):
    return render(request, 'project_01/webRunsetAdd.html')
def edit_webFuncSet(request):
    return render(request, 'project_01/webRunsetEdit.html')
def runWeb_history(request):
    return render(request, 'project_01/rw-history.html')


#接口测试
def load_interface(request):
    return render(request, 'project_01/interfaceList.html')


def interfaceAdd(request):
    return render(request, 'project_01/interfaceAdd.html')


def interfaceEdit_get(request):
    return render(request, 'project_01/infterfaceEdit.html')

def interfaceEdit_save(request):
    return render(request, 'project_01/interfaceList.html')

def interface_delete(request):
    return render(request, 'project_01/interfaceList.html')


def load_report(request):
    return render(request, 'project_01/resultList.html')