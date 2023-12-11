from django.shortcuts import render
from visitantes.models import Visitantes


def index(request):
    try:
        todos_visitantes = Visitantes.objects.all().order_by('-horario_chegada', )
    except Visitantes.DoesNotExist:
        todos_visitantes = []

    context = {
        "nome_pagina": "Pagina Inicial",
        "todos_visitantes": todos_visitantes,
    }
    return render(request, "index.html", context)
