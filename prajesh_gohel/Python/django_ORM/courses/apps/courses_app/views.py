from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "courses": Course.objects.all()
    }

    return render(request, 'courses/index.html', context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        else:
            Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
            return redirect('/')

    print("*"*80)
    print("Someone tried to bypass the Post method, they have been redirected")
    print("*"*80)
    return redirect('/')

def confirm(request, id):
    context = {
        "course": Course.objects.get(id=int(id))
    }

    return render(request, 'courses/confirm.html', context)

def delete(request, id):
    delete_course = Course.objects.get(id=int(id))
    delete_course.delete()
    return redirect('/')

def comments(request, id):
    c = Course.objects.get(id=int(id))
    context = {
        "course": c,
        "comments": c.comments.all()
    }

    return render(request, 'courses/comments.html', context)

def add(request, id):
    errors = Course.objects.comment_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/comments/'+id+'/')

        else:
            create_comment = Course.objects.get(id=int(id))
            create_comment.comments.create(text=request.POST['comment'])
            create_comment.save()
            return redirect('/comments/'+id+'/')

    print("*"*80)
    print("Someone tried to bypass the Post method, they have been redirected")
    print("*"*80)
    return redirect('/')
