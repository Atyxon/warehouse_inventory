from django.shortcuts import render
from django.http import HttpResponse


def main_view(request):
    return HttpResponse("Witaj, jestem widokiem na domyślnym adresie!")
