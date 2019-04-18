from django.contrib import admin

# Register your models here.
from . import models


class NewAppInfo(admin.ModelAdmin):
    list_display = ['pro_name', 'package', 'createby', 'c_time', 'status']
    list_filter = ['pro_name', 'package', 'createby']
    search_fields = ('pro_name',)

class NewMachineInfo(admin.ModelAdmin):
    list_display = ['phone_name', 'm_name', 'sys', 'sysverson', 'c_time', 'status']
    list_filter = ['phone_name', 'm_name', 'sys']
    search_fields = ('phone_name',)

class NewServerInfo(admin.ModelAdmin):
    list_display = ['wind_sys', 'serverIP', 'createby', 'c_time', 'status']
    list_filter = ['wind_sys', 'serverIP', 'createby']
    search_fields = ('wind_sys', 'serverIP', 'createby')



admin.site.register(models.machineinfo, NewMachineInfo)
admin.site.register(models.appinfo, NewAppInfo)
admin.site.register(models.serverinfo, NewServerInfo)
