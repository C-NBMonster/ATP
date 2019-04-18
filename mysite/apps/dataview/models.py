from django.db import models

# Create your models here.


class runRecord(models.Model):

    proName = models.CharField(max_length=20, blank=True)#项目名称
    caseTotal = models.CharField(max_length=6, blank=True)
    caseRan = models.CharField(max_length=10, blank=True) #已运行用例数
    runTimes = models.CharField(max_length=5, blank=True)#运行次数
    passed = models.CharField(max_length=5, blank=True)
    failed = models.CharField(max_length=5, blank=True)
    jump   = models.CharField(max_length=5, blank=True)
    CoverageRate = models.CharField(max_length=5, blank=True)
    passRate = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.proName

    class Meta:
        ordering = ["-proName"]
        verbose_name = "运行记录"
        verbose_name_plural = "运行记录"


