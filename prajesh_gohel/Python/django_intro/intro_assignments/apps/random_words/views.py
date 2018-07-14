from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def generate(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    return render(request, "intro_assignments/index.html")

def process(request):
    if request.method == 'POST':
        print("*"*80)
        print(request.POST)
        print("\n")
        words = get_random_string(length=10)
        request.session['string'] = words
        print(request.session['string'])
        request.session['counter'] += 1
        print(request.session['counter'])
        print("\n")
        print("*"*80)
        return redirect('/')

    else:
        return redirect('/')

def reset(request):
    del request.session['counter']
    return redirect('/')
