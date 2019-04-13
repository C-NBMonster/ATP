from django.shortcuts import render
from . import models
# Create your views here.


def show_dataview(request):
    dataView = models.runRecord.objects.all()
    return render(request, 'dataview/run-dataview-list.html', locals())


