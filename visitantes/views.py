from django.shortcuts import render, redirect
from visitantes.forms import VisitanteForm

def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():
            # Salva os dados do formulário no banco de dados, mas não faz o commit
            visitante = form.save(commit=False)

            # Define o campo "registrado_por" do visitante como o porteiro atualmente autenticado
            visitante.registrado_por = request.user.porteiro

            # Salva o visitante no banco de dados
            visitante.save()

            return redirect("index")

    # Cria um contexto contendo o nome da página e o formulário
    # Com o contexto se consegue utilizar o valor de cada chave diretamente no HTML
    context = {
        "nome_pagina" : "Registrar Visitante",
        "form" : form,
    }

    return render(request, "registrar_visitante.html", context)
