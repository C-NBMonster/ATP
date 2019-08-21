from django.db import models
from django.contrib import admin
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=gender, default="男")
    phone= models.CharField(max_length=20, default=None)
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50)
    depart = models.CharField(max_length=30, default='测试部')
    joinTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='已启用')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-joinTime"]
        verbose_name = "用户"
        verbose_name_plural = "用户"