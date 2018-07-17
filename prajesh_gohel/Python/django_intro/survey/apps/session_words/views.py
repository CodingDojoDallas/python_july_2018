from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
def index(request):
    print("cool cool")
    if 'word' not in request.session:
        request.session['word'] = []

    return render(request, 'session_words/index.html')

def process(request):
    print("yayay")
    print(request.session['word'])
    if request.method == "POST":
        print(request.POST)
        temp_list = request.session['word']
        if 'big_font' in request.POST:
            big_font = 100

        else:
            big_font = 12

        print(big_font)
        temp_list.append({'word': request.POST['word'], 'color': request.POST['color'], 'big_font': big_font, 'time': strftime("%-I:%M:%S, %B %d %Y", gmtime())})
        request.session['word'] = temp_list
        return redirect('/words')

    return redirect('/words')

def reset(request):
    request.session.clear()
    print("Deleted")
    return redirect('/words')
