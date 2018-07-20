from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import datetime
import bcrypt

def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False

    if 'email' in request.session:
        del request.session['email']
        request.session['logged_in'] = False

    return render(request, 'wall/index.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], birthday=datetime.datetime.strptime(request.POST['birthday'], "%Y-%m-%d"), password=pw_hash)
            request.session['email'] = request.POST['email']
            request.session['logged_in'] = True
            return redirect('/wall')

    return redirect('/')

def verify(request):
    errors = User.objects.login_validator(request.POST)
    user = User.objects.filter(email=request.POST['email'])

    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        elif not bcrypt.checkpw(request.POST['passlog'].encode(), user[0].password.encode()):
            messages.error(request, "Login failed")
            return redirect('/')

        else:
            request.session['email'] = request.POST['email']
            request.session['logged_in'] = True
            return redirect('/wall')

def wall(request):
    if request.session['logged_in'] == False:
        return redirect('/')

    context = {
        "user": User.objects.get(email=request.session['email']),
        "messages": Message.objects.all().order_by("-created_at"),
        "comments": Comment.objects.all()
    }

    return render(request, 'wall/wall.html', context)

def post(request):
    if request.method == 'POST':
        Message.objects.create(user=User.objects.get(email=request.session['email']), message=request.POST['message'])
        return redirect('/wall')

    return redirect('/wall')

# def comment(request):
#     if request.method == 'POST':
#

def log_out(request):
    del request.session['email']
    request.session['logged_in'] = False
    return redirect('/')
