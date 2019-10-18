from django.shortcuts import render,redirect

# Create your views here.
def load_dataview(request):
    return render(request, 'dataview/dataview.html')

