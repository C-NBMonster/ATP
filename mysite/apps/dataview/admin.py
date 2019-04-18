from django.contrib import admin
from . import models
# Register your models here.
class NewRunRecord(admin.ModelAdmin):
    list_display = ['proName', 'caseTotal', 'caseRan', 'runTimes', 'passed', 'failed', 'jump','CoverageRate', 'passRate']
    list_filter = ['proName', 'caseTotal', 'caseRan']
    search_fields = ('proName',)




admin.site.register(models.runRecord, NewRunRecord)
