from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'time_display/index.html', context)
