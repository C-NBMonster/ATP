"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from testF import views as Tview
from apps.app_project_base import views as baseView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('testAdd/', Tview.testAdd),
    path('machine_add/', baseView.machine_add),
    path('machine_edit/', baseView.machine_edit),
    url(r'indexApp/', include('indexApp.urls')),
    url(r'app_project_base/', include('app_project_base.urls')),
    url(r'app_project_01/', include('app_project_01.urls')),
    url(r'dataview/', include('dataview.urls')),
    url(r'users/', include('users.urls')),
    url(r'testF/', include('testF.urls')),
    path('machine_add/', baseView.machine_add),
]
