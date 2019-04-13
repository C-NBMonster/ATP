from django.contrib import admin

# Register your models here.
from . import models



class NewUser(admin.ModelAdmin):
    list_display = ['name', 'password', 'depart', 'email', 'sex', 'phone', 'joinTime', 'status']
    list_filter = ['name', 'joinTime', 'sex', 'depart']
    search_fields = ('name', 'joinTime', 'sex', 'depart')




admin.site.register(models.User, NewUser)