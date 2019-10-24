from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import models as amodels
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def load_member(request):
    #获取用户信息
    uTotal = amodels.User.objects.count()
    #如果查询结果为空,django是会报错的，所以要添加以下判断
    if uTotal == 0:
        msg="没有用户信息！"
        return render(request, 'users/memberList.html', locals())
    else:
        user_info = amodels.User.objects.all().order_by('-id')
        return render(request, 'users/memberList.html', locals())


def pop_memberInfo(request):
    return render(request, 'users/memberAdd.html')


def member_edit_get(request, userid='538530'):
    #获取当前行的信息，并传到machine_edit.html
    edit_info = amodels.User.objects.get(id=request.GET["id"])
    return render(request, 'users/memberEdit.html', locals())

def member_edit_save(request):
    #保存编辑信息
    amodels.User.objects.filter(id=request.GET["id"]).update(
        email    = request.GET["username"],
        username = request.GET["m_name"],
        password = request.GET["pass"],
        is_active= request.GET["enable"],
    )
    return redirect('/users/load_member')


def member_add(request, userId=538530):
    #添加用户信息
    m = amodels.User.objects
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
    return redirect('/base/load_member')

def member_delete(request):
    amodels.User.objects.get(id=request.GET["id"]).delete()
    return redirect('/base/load_member')

def loadAdmin(request):
    # 获取用户信息
    uTotal = amodels.User.objects.filter(is_superuser=True).count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if uTotal == 0:
        msg = "没有用户信息！"
        return render(request, 'users/adminList.html', locals())
    else:
        user_info = amodels.User.objects.all().order_by('-id')
        return render(request, 'users/adminList.html', locals())


def loadAdminGroup(request):
    #admin用户组
    uTotal = amodels.Group.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if uTotal == 0:
        msg = "没有用户信息！"
        return render(request, 'users/adminGroup.html', locals())
    else:
        user_info = amodels.User.objects.all().order_by('-id')
        return render(request, 'users/adminGroup.html', locals())

def loadRule(request):
    #规则管理
    uTotal = amodels.Permission.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if uTotal == 0:
        msg = "没有规则信息！"
        return render(request, 'users/ruleList.html', locals())
    else:
        user_info = amodels.User.objects.all().order_by('-id')
        return render(request, 'users/ruleList.html', locals())

def loadRole(request):
    #admin规则
    uTotal = amodels.Permission.objects.count()
    # 如果查询结果为空,django是会报错的，所以要添加以下判断
    if uTotal == 0:
        msg = "没有用户信息！"
        return render(request, 'users/roleList.html', locals())
    else:
        user_info = amodels.User.objects.all().order_by('-id')
        return render(request, 'users/roleList.html', locals())


