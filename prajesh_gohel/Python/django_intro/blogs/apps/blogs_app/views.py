from django.shortcuts import render, HttpResponse, redirect

def display(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    print(number)
    return HttpResponse("show method " + number)

def edit(request, number):
    print(number)
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request, number):
    print(number)
    return redirect('/')
