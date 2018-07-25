from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..dashboard.models import *
from ..login.models import *

def add(request):
    return render(request, 'handy_helper_exam/addJob.html')

def insert(request):
    errors = Job.objects.job_validation(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/addJob')

        else:
            Job.objects.create(title = request.POST['title'], desc = request.POST['desc'], location = request.POST['location'], user = User.objects.get(email = request.session['email']))
            return redirect('/dashboard')

    return redirect('/addJob')
