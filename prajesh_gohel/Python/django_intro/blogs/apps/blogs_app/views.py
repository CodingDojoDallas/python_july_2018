from django.shortcuts import render, HttpResponse, redirect

def display(request):
    response = "Placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    return render(request, "blogs/index.html")

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    print(number)
    return HttpResponse("show method " + number)

def edit(request, number):
    print(number)
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request, number):
    print(number)
    return redirect('/')
