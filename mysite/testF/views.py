from django.shortcuts import render
from . import models
import time
# Create your views here.


def testAdd(request):
    return render(request, 'testF/testAdd.html')

def machine_Tadd(request):
    p_name = request.GET["p_name"]
    m_name = request.GET["m_name"]
    platform = request.GET["platform"]
    s_version = request.GET["sys_version"]
    models.TD.objects.create(p1=538530,
                             p2=p_name,
                             p3=m_name,
                             p4=platform,
                             p5=s_version,
                             p6="mirror",
                             p7=time.strftime('%Y-%m-%d %H:%M:%S')
                             )

    # machine_info = models.machineinfo.objects.all()
    return testAdd(request)