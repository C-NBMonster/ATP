from django.db import models
import datetime
# Create your models here.

class TD(models.Model):
    p1 = models.IntegerField(blank=True)
    p2 = models.CharField(max_length=20, blank=True)
    p3 = models.CharField(max_length=20, blank=True)
    p4 = models.CharField(max_length=20, blank=True)
    p5 = models.CharField(max_length=20, blank=True)
    p6 = models.CharField(max_length=20, blank=True)
    p7 = models.DateTimeField(blank=True, default=datetime.datetime.now() )

    def __self__(self):
        return self.p1

    class Meta():
        ordering=['-p1']
        verbose_name = "测试插入"
