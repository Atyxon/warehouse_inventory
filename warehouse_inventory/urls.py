"""
URL configuration for warehouse_inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from warehouseApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('page/<str:page>', views.main_view, name='main_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('admin/', admin.site.urls),
    path('add/', views.add_item, name='add_item'),
    path('set-cookie/', views.set_cookie_view, name='set_cookie'),
    path('search/', views.search_items, name='search_items'),
]

urlpatterns += staticfiles_urlpatterns()
