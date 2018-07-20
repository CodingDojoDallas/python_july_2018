from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from ..users.models import *
import bcrypt

def main(request):
    if request.session['logged_in'] == False:
        return redirect('/')

    context = {
        'user': User.objects.get(email = request.session['email']),
        'quotes': Quote.objects.all().order_by('-created_at'),
    }

    return render(request, 'quote_dash_exam/main_page.html', context)

def post(request):
    errors = Quote.objects.simple_validator(request.POST)

    if request.method == 'POST':
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('/quotes')

        Quote.objects.create(author = request.POST['author'], quote = request.POST['quote'], user = User.objects.get(email = request.session['email']))
        return redirect('/quotes')

    return redirect('/quotes')

def destroy(request, id):
    delete = Quote.objects.get(id = int(id))
    delete.delete()
    return redirect('/quotes')

def log_out(request):
    del request.session['email']
    request.session['logged_in'] = False
    return redirect('/')
