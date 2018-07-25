from django.shortcuts import render, HttpResponse, redirect
from ..login.models import *
from .models import *

def index(request):
    context = {
        'user': User.objects.get(email=request.session['email']),
        'jobs': Job.objects.all(),
        'added_jobs': Job.objects.filter(user_jobs=User.objects.get(email=request.session['email'])),
    }

    return render(request, 'handy_helper_exam/dash.html', context)

def logout(request):
    del request.session['email']
    request.session['logged_in'] = False
    return redirect('/')

def destroy(request, id):
    job = Job.objects.get(id=int(id))
    job.delete()
    return redirect('/dashboard')

def add(request, id):
    this_user = User.objects.get(email=request.session['email'])
    this_job = Job.objects.get(id=int(id))
    this_job.user_jobs.add(this_user)
    return redirect('/dashboard')
