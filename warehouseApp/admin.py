from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'added_date')
    search_fields = ('name', 'description')