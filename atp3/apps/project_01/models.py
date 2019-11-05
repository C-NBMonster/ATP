from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
#from apps.base.models import Product
class cases(models.Model):
    #用例库
    uid      = models.IntegerField(default=None, blank=True) #用户id
    pro_name = models.CharField(max_length=20, blank=True) #项目名称
    module   = models.CharField(max_length=20, blank=True) #所属模块
    case_name1 = models.CharField(max_length=100, blank=True)
    case_name2 = models.CharField(max_length=100, blank=True)
    para1 = models.CharField(max_length=30, blank=True, default=None)
    para2 = models.CharField(max_length=20, blank=True, default=None)
    para3 = models.CharField(max_length=20, blank=True, default=None)
    para4 = models.CharField(max_length=20, blank=True, default=None)
    para5 = models.CharField(max_length=20, blank=True, default=None)
    para6 = models.CharField(max_length=20, blank=True, default=None)
    para7 = models.CharField(max_length=20, blank=True, default=None)
    para8 = models.CharField(max_length=20, blank=True, default=None)
    para9 = models.CharField(max_length=20, blank=True, default=None)
    para10 = models.CharField(max_length=20, blank=True, default=None)
    para11 = models.CharField(max_length=20, blank=True, default=None)
    para12 = models.CharField(max_length=20, blank=True, default=None)
    createby = models.CharField(max_length=20, blank=True, default=None)
    updateby = models.CharField(max_length=20, blank=True, default=None)
    c_time   = models.DateTimeField(auto_now_add=True, blank=True)
    upt_time = models.DateTimeField(auto_now_add=True, blank=True)
    sort     = models.IntegerField(default=None, blank=True) #用例执行顺序排序
    run      = models.CharField(max_length=20, blank=True, default=1) #是否运行

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "项目名称"
        verbose_name_plural = "用例库"



# Create your models here.
class apprunset(models.Model):
    #APP运行配置
    uid      = models.IntegerField(default=None, blank=True)
    pro_name = models.CharField(max_length=30, blank=True)
    pho_name = models.CharField(max_length=30, blank=True)
    serverIP = models.CharField(max_length=30, blank=True)
    createby = models.CharField(max_length=20, blank=True)
    c_time   = models.DateTimeField(auto_now_add=True, blank=True)
    upt_time = models.DateTimeField(auto_now_add=True, blank=True)
    status   = models.CharField(max_length=20, default='启用', blank=True)

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "项目名称"
        verbose_name_plural = "APP运行配置"

class webrunset(models.Model):
    #Web运行配置
    uid = models.IntegerField(blank=True, default=None)
    pro_name = models.CharField(max_length=20, blank=True)
    browser_name = models.CharField(max_length=30, blank=True)
    serverIP = models.CharField(max_length=20, blank=True)
    createby = models.CharField(max_length=20, blank=True)
    c_time   = models.DateTimeField(auto_now_add=True, blank=True)
    upt_time = models.DateTimeField(auto_now_add=True, blank=True)
    status   = models.CharField(max_length=20, default='启用', blank=True)

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "项目名称"
        verbose_name_plural = "Web运行配置"


class runHistory(models.Model):
    #运行历史
    uid      = models.IntegerField(blank=True, default=None)
    pro_name = models.CharField(max_length=20, blank=True)
    pho_name = models.CharField(max_length=30, blank=True)
    serverIP = models.CharField(max_length=20, blank=True)
    excuteby = models.CharField(max_length=20, blank=True)
    caseTotle= models.IntegerField(blank=True, default=None)
    casePass = models.IntegerField(blank=True, default=None)
    caseFail = models.IntegerField(blank=True, default=None)
    caseJump = models.IntegerField(blank=True, default=None)
    startTime= models.DateTimeField(auto_now_add=True, blank=True)
    endTime  = models.DateTimeField(auto_now_add=True, blank=True)
    type     = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-startTime"]
        verbose_name = "项目名称"
        verbose_name_plural = "运行历史"

class interface(models.Model):
    #运行配置
    request_type=(
        ('get', 'get'),
        ('post', 'post'),
        )
    uid    = models.IntegerField(blank=True, default=None)
    project = models.CharField(max_length=50, blank=True)
    caseName = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=150, blank=True)
    reqType   = models.CharField(max_length=10, choices=request_type, default='get', blank=True)
    parameter = models.CharField(max_length=300, blank=True)
    checkPoint= models.CharField(max_length=200, blank=True)
    result = models.CharField(max_length=10, blank=True)
    tester = models.CharField(max_length=10, blank=True)
    createTime = models.DateTimeField(blank=True, default=timezone.now)
    updateTime = models.DateTimeField(blank=True, default=timezone.now)  #auto_add_now简直见鬼，必须用timezone.now或者datetime
    isRun = models.CharField(max_length=10, blank=True)
    operation = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.caseName

    class Meta:
        # ordering = ["-c_time"]
        verbose_name = "用例名称"
        verbose_name_plural = "接口测试"

class report(models.Model):
    #运行测试报告
    uid       = models.IntegerField(blank=True, default=None)
    pro_name  = models.CharField(max_length=100, blank=True)
    module    = models.CharField(max_length=20, blank=True)
    case_name = models.CharField(max_length=100, blank=True)
    case_total= models.CharField(max_length=10, blank=True)
    case_pass = models.CharField(max_length=10, blank=True)
    case_fail = models.CharField(max_length=10, blank=True)
    case_jump = models.CharField(max_length=10, blank=True)
    start_time= models.DateTimeField(auto_now_add=True, blank=True) #开始时间
    end_time  = models.DateTimeField(auto_now_add=True, blank=True)#总运行时间
    s_time    = models.DateTimeField(auto_now_add=True, blank=True)  # 单用例开始时间
    e_time    = models.DateTimeField(auto_now_add=True, blank=True)  # 单用例运行结束时间
    reson     = models.CharField(max_length=1000, blank=True)
    result    = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-s_time"]
        verbose_name = "项目名称"
        verbose_name_plural = "测试报告"


class case_login(models.Model):
    #运行测试报告
    uid       = models.IntegerField(blank=True, default=None)
    pro_name  = models.CharField(max_length=100, blank=True)
    module    = models.CharField(max_length=20, blank=True)
    case_name = models.CharField(max_length=100, blank=True)
    case_total= models.CharField(max_length=10, blank=True)
    case_pass = models.CharField(max_length=10, blank=True)
    case_fail = models.CharField(max_length=10, blank=True)
    case_jump = models.CharField(max_length=10, blank=True)
    start_time= models.DateTimeField(auto_now_add=True, blank=True) #开始时间
    end_time  = models.DateTimeField(auto_now_add=True, blank=True)#总运行时间
    s_time    = models.DateTimeField(auto_now_add=True, blank=True)  # 单用例开始时间
    e_time    = models.DateTimeField(auto_now_add=True, blank=True)  # 单用例运行结束时间
    reson     = models.CharField(max_length=1000, blank=True)
    result    = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.pro_name

    class Meta:
        ordering = ["-s_time"]
        verbose_name = "项目名称"
        verbose_name_plural = "测试报告"


class Appcase(models.Model):
    #Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)  # 关联产品id
    appcasename = models.CharField('用例名称', max_length=200)  # 测试用例名称
    apptestresult = models.BooleanField('测试结果')  # 测试结果
    apptester = models.CharField('测试负责人', max_length=16)  # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间-自动获取当前时间

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    Appcase = models.ForeignKey('Appcase', on_delete=models.CASCADE)  # 关联接口id
    appteststep = models.CharField('测试步聚', max_length=200)  # 测试步聚
    apptestobjname = models.CharField('测试对象名称描述', max_length=200)  # 测试对象名称描述
    appfindmethod = models.CharField('定位方式', max_length=200)  # 定位方式
    appevelement = models.CharField('控件元素', max_length=800)  # 控件元素
    appoptmethod = models.CharField('操作方法', max_length=200)  # 操作方法
    apptestdata = models.CharField('测试数据', max_length=200, null=True)  # 测试数据
    appassertdata = models.CharField('验证数据', max_length=200)  # 验证数据
    apptestresult = models.BooleanField('测试结果')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间-自动获取当前时间

    def __str__(self):
        return self.appteststep