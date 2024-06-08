from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from warehouseApp.forms import ItemForm
from warehouseApp.models import Item, User

def main_view(request, page='home'):
    theme = request.COOKIES.get('theme', 'light')
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
    return render(request, 'index.html', {'page': page, 'items': items, 'theme': theme})
def set_cookie_view(request):
    cookie_value = request.GET.get('value',
                                   'bright')  # Retrieve 'value' from GET parameters, default to 'default_value'
    response = HttpResponseRedirect('/page/settings')
    response.set_cookie(
        key='theme',
        value=cookie_value,
        max_age=9999999,
        expires=None,
        path='/',
        domain=None,
        secure=False,
        httponly=False,
        samesite='Lax',
    )
    return response


def logout_view(request):
    logout(request)
    return redirect('/page/logout')

def item_list(request):
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()

    return render(request, 'index.html', {'items': items, 'page': 'home', 'query': query})

def search_items(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = Item.objects.all()

    results = [{'name': item.name, 'description': item.description, 'quantity': item.quantity, 'price': item.price} for item in items]
    return JsonResponse(results, safe=False)

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
