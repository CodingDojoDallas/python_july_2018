from django.shortcuts import render, HttpResponse, redirect
from ..dashboard.models import *

def editpage(request, id):
    context = {
        "job": Job.objects.get(id=int(id))
    }

    return render(request, 'handy_helper_exam/edit.html', context)

def update(request, id):
    errors = Job.objects.job_validation(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/edit/'+id+'/')

        else:
            edit_job = Job.objects.get(id=int(id))
            edit_job.title = request.POST['title']
            edit_job.desc = request.POST['desc']
            edit_job.location = request.POST['location']
            edit_job.save()
            return redirect('/dashboard')

    return redirect('/edit/'+id+'/')
