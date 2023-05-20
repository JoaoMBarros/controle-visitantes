from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):

    context = {
        "nome_pagina" : "Início do dashboard",
    }

    return render(request, "index.html", context)