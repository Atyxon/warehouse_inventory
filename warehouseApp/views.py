from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from warehouseApp.models import Item

def main_view(request, page='home'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/page/login')
        else:
            messages.error(request, 'Bad passes')
            return redirect('/page/wrong_passes')
    items = Item.objects.all()
    return render(request, 'index.html', {'page': page, 'items' : items})

def logout_view(request):
    logout(request)
    return redirect('/page/logout')