from django.shortcuts import render, HttpResponse, redirect
from ..login.models import *
from ..dashboard.models import *

def display(request, id):
    context = {
        'job': Job.objects.get(id=int(id))
    }

    return render(request, 'handy_helper_exam/display.html', context)
