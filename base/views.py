from django.shortcuts import render
from django.http import HttpResponse
from . forms import CadastroForm

# def "view". Cada uma delas podemos redirecionar para outras paginas
def inicio(request):
    return render(request, 'inicio.html') # render: renderiza o html


def cadastro(request):
    sucesso = False
    if request.method == 'GET': # GET: pegando informacoes do usuario e POST envia
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid(): # Verifica se as infomaçoes estão corretas
            sucesso = True # Se estiver tudo correto, sucesso altera pra True 
    contexto = { #Vale para o IF e para o else
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto) 
