from django.contrib import admin
from . import models
# Register your models here.
class Newcases(admin.ModelAdmin):
    list_display = ['uid','pro_name', 'module', 'case_name1', 'case_name2','para1', 'para2', 'para3', 'para4','para5', 'para6', 'para7', 'para8', 'para9', 'para10', 'para11', 'para12', 'createby', 'updateby', 'c_time', 'upt_time', 'run']
    list_filter = ['pro_name', 'module', 'case_name1']
    search_fields = ('pro_name','module', 'case_name1')

class NewAppRunset(admin.ModelAdmin):
    list_display = ['pro_name', 'pho_name', 'serverIP',  'createby', 'c_time', 'c_time', 'upt_time', 'status']
    list_filter = ['pro_name', 'pho_name', 'serverIP']
    search_fields = ('pro_name', 'pho_name', 'serverIP')

class NewWebRunset(admin.ModelAdmin):
    list_display = ['pro_name', 'browser_name', 'serverIP',  'createby', 'c_time', 'c_time', 'upt_time', 'status']
    list_filter = ['pro_name', 'browser_name', 'serverIP']
    search_fields = ('pro_name', 'browser_name', 'serverIP')

class NewRunHistory(admin.ModelAdmin):
    list_display = ['pro_name', 'pho_name', 'serverIP',  'excuteby', 'caseTotle', 'casePass', 'caseFail', 'caseJump', 'startTime', 'endTime']
    list_filter = ['pro_name', 'pho_name', 'serverIP']
    search_fields = ('pro_name', 'pho_name', 'serverIP')

class NewInterface(admin.ModelAdmin):
    list_display = ['c_name', 'r_type', 'result']
    list_filter = ['c_name', 'r_type', 'result']
    search_fields = ('c_name', 'r_type', 'result')

class NewReport(admin.ModelAdmin):
    list_display = ['pro_name', 'module', 'case_name', 'case_total','case_pass', 'case_fail', 'case_jump', 'start_time', 'end_time', 's_time', 'e_time', 'reson', 'result',]
    list_filter = ['pro_name', 'module', 'case_name']
    search_fields = ('pro_name', 'module', 'case_name')


admin.site.register(models.cases, Newcases)
admin.site.register(models.apprunset, NewAppRunset)
admin.site.register(models.webrunset, NewWebRunset)
admin.site.register(models.interface, NewInterface)
admin.site.register(models.runHistory, NewRunHistory)
admin.site.register(models.report, NewReport)