from django.shortcuts import render
from django.http import HttpResponse


# def "view". Cada uma delas podemos redirecionar para outras paginas
def inicio(request):
    return render(request, 'inicio.html') # render: renderiza o html


def cadastro(request):
    return render(request, 'cadastro.html') 