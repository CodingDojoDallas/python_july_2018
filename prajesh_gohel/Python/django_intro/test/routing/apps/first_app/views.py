from django.shortcuts import render, HttpResponse, redirect
 # the index function is called when root is visited
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "routing/index.html", context)

def test(request):
    response = "Hello, I am test"
    return HttpResponse(response)
