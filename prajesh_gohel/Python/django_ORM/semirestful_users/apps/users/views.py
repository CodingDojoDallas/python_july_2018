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
