from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'logged_in' not in request.session:
        request.session['logged_in'] = False

    return render(request, 'handy_helper_exam/index.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/')

        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['email'] = request.POST['email']
            request.session['logged_in'] = True
            return redirect('/dashboard')

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
            return redirect('/dashboard')

    return redirect('/')
