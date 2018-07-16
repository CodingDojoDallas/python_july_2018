from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    if request.method == 'POST':
        print("*"*80)
        print(request.POST)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')

    else:
        return redirect('/')

def result(request):
    return render(request, 'survey/result.html')
