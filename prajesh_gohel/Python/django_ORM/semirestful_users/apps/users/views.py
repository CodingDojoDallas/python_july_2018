from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "users": User.objects.all()
    }

    return render(request, 'semirestful_users/index.html', context)

def new(request):
    return render(request, 'semirestful_users/new.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/new')

        else:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            return redirect('/')

    return redirect('/new')

def delete(request, id):
    delete_user = User.objects.get(id=int(id))
    delete_user.delete()
    return redirect('/')

def display(request, id):
    context = {
        "user": User.objects.get(id=int(id))
    }

    return render(request, 'semirestful_users/display.html', context)

def edit(request, id):
    context = {
        "user": User.objects.get(id=int(id))
    }

    return render(request, 'semirestful_users/edit.html', context)

def update(request, id):
    errors = User.objects.edit_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/'+id+'/edit')

        else:
            edit_user = User.objects.get(id=int(id))
            edit_user.first_name = request.POST['first_name']
            edit_user.last_name = request.POST['last_name']
            edit_user.email = request.POST['email']
            edit_user.save()
            return redirect('/')

    return redirect('/'+id+'/edit')
