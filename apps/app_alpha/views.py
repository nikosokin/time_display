from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime

def index(request):
    
    return HttpResponse("<h1>Hello</b>")

def time_display(request):
    
    info = {
        "date" : strftime("%Y/%m/%d", localtime()),
        "time" : strftime("%I:%M %p", localtime())
    }

    return render(request, "app_alpha/index.html", info)


# Create your views here.
