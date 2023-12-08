from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "nome_pagina": "Pagina Inicial",
    }
    return render(request, "index.html", context)


