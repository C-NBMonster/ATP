from django.shortcuts import render
from . import models
# Create your views here.
#用例管理
def show_appFunc_swap(request):
    return render(request, 'app_project_01/case-swap.html')
def load_appFunc(request):
    case_info = models.cases.objects.all()
    return render(request, 'app_project_01/case-list.html', locals())


#app运行配置
def show_appFuncSet_swap(request):
    return render(request, 'app_project_01/app-runset-swap.html')
def load_appFuncSet(request):
    app_run = models.apprunset.objects.all()
    return render(request, 'app_project_01/app-runset-list.html', locals())
def add_appFuncSet(request):
    return render(request, 'app_project_01/app-runset-add.html')
def edit_appFuncSet(request):
    return render(request, 'app_project_01/app-runset-edit.html')
def runApp_history(request):
    return render(request, 'app_project_01/runApp-history-list.html')


#web运行配置
def show_webFuncSet_swap(request):
    return render(request, 'app_project_01/web-runset-swap.html')
def load_webFuncSet(request):
    web_run = models.webrunset.objects.all()
    return render(request, 'app_project_01/web-runset-list.html', locals())
def add_webFuncSet(request):
    return render(request, 'app_project_01/web-runset-add.html')
def edit_webFuncSet(request):
    return render(request, 'app_project_01/web-runset-edit.html')
def runWeb_history(request):
    return render(request, 'app_project_01/runWeb-history-list.html')


def show_interface_swap(request):
    return render(request, 'app_project_01/interface-swap.html')
def load_interface(request):
    return render(request, 'app_project_01/interface-list.html')

def show_report_swap(request):
    return render(request, 'app_project_01/result-swap.html')
def load_report(request):
    return render(request, 'app_project_01/result-list.html')