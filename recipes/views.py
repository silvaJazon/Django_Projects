from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def sobre(request):
    return HttpResponse('Sobre!')


def home(request):
    return HttpResponse('Home!')


def contact(request):
    return HttpResponse('Contact!')
