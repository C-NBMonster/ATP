from django.shortcuts import render
from . import models
# Create your views here.
def show_member_list(request):
    memberInfo = models.User.objects.filter(status="已启用")
    return render(request, 'users/member-list.html', locals())
def member_add(request):
    return render(request, 'users/member-add.html')
def member_del(request):
    memberDel = models.User.objects.filter(status="已禁用")
    return render(request, 'users/member-del.html', locals())
def member_edit(request):
    return render(request, 'users/member-edit.html')
def member_password(request):
    return render(request, 'users/member-password.html')


def show_admin_list(request):
    return render(request, 'users/admin-list.html')
def admin_edit(request):
    return render(request, 'users/admin-edit.html')



def show_admin_role_list(request):
    return render(request, 'users/admin-role.html')
def admin_role_add(request):
    return render(request, 'users/role-add.html')
def admin_role_edit(request):
    return render(request, 'users/role-edit.html')


def show_admin_cate_list(request):
    return render(request, 'users/admin-cate.html')

def show_admin_rule_list(request):
    return render(request, 'users/admin-rule.html')
def admin_rule_add(request):
    return render(request, 'users/admin-rule-add.html')
def admin_rule_edit(request):
    return render(request, 'users/admin-rule-edit.html')
