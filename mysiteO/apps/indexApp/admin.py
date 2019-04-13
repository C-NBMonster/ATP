from django.contrib import admin

# Register your models here.
from . import models


# class NewUser(admin.ModelAdmin):
#     list_display = ['name', 'password', 'email', 'sex', 'c_time']
#     list_filter = ['name', 'c_time', 'sex']
#     search_fields = ('name', 'c_time', 'sex')
#
#
# admin.site.register(models.User, NewUser)