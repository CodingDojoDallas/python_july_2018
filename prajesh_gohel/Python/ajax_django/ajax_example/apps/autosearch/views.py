from django.shortcuts import render, HttpResponse, redirect
from .models import *

def autosearch(request):
    context = {
        'users': User.objects.filter(name=request.POST['starts_with'])
    }
    return render(request, 'ajax_example/autosearch.html', context)
