from django.db import models


# Create your models here.
class machineinfo(models.Model):
    #手机设备信息
    sys = (
        ('android', "Android"),
        ('ios', "IOS"),
        ('windows', "Windows"),
    )
    def __str__(self):
        return self.phone_name
    uid = models.CharField(max_length=10, blank=True)
    phone_name = models.CharField(max_length=30, blank=True)
    m_name = models.CharField(max_length=50, blank=True)
    sys = models.CharField(max_length=20, choices=sys, default="Android", blank=True)
    sysverson = models.CharField(max_length=15, blank=True)
    createby = models.CharField(max_length=20, blank=True)
    c_time = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=10, default='启用', blank=True)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "手机信息"
        verbose_name_plural = "手机信息"

class appinfo(models.Model):
    #应用程序信息
    def __str__(self):
        return self.pro_name

    uid = models.CharField(max_length=10, blank=True)
    pro_name = models.CharField(max_length=50, blank=True)
    package  = models.CharField(max_length=100, blank=True)
    activity = models.CharField(max_length=100, blank=True)
    createby = models.CharField(max_length=20, blank=True)
    c_time   = models.DateTimeField(auto_now_add=True, blank=True)
    status   = models.CharField(max_length=10, default='启用', blank=True)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "APP信息"
        verbose_name_plural = "APP信息"

class serverinfo(models.Model):
    #(appium)服务器信息
    def __str__(self):
        return self.serverIP

    uid = models.CharField(max_length=10, blank=True)
    os  = models.CharField(max_length=20, blank=True)
    serverIP = models.CharField(max_length=30, blank=True)
    createby = models.CharField(max_length=20, blank=True)
    c_time   = models.DateTimeField(auto_now_add=True, blank=True)
    status   = models.CharField(max_length=10, default='启用', blank=True)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "服务器IP"
        verbose_name_plural = "服务器IP"
