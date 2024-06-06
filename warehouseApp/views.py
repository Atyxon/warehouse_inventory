from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from warehouseApp.forms import ItemForm
from warehouseApp.models import Item, User


def main_view(request, page='home'):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        Users = User.objects.get(name=username)
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

def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory.html', {'items': items})

def add_item(request):
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'page': 'home', 'items' : items})
    else:
        form = ItemForm()
    return render(request, 'index.html', {'form': form, 'page': 'add_item'})