from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro

# def "view". Cada uma delas podemos redirecionar para outras paginas
def inicio(request):
    return render(request, 'inicio.html') # render: renderiza o html


def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None) # Verifica se está preenchido ou vazio
    if form.is_valid(): # Verifica se as infomaçoes estão corretas
        sucesso = True # Se estiver tudo correto, sucesso altera pra True 
        form.save()   
    contexto = { #Vale para o IF e para o else
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto) 
