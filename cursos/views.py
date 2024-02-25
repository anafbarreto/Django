from django.shortcuts import render
from cursos.forms import CursoForm
from cursos.models import Curso
from django.views.decorators.cache import cache_page # para usar o cache

# Create your views here.

@cache_page(30) # Isso faz com que o site fique em cache por 30 segundos antes de exibir atualizações que foram feitas na base de dados
def criar_curso(request):
    Cursos= Curso.objects.all() #Para mostrar todos os cursos cadastrados e exibir na tela de cadastro junto com o contexto
    form = CursoForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
        'cursos': Cursos
    }
    return render(request, 'criar_curso.html', contexto)


def exibir_cursos(request): # Exibe todos os cursos na tela de cursos
   cursos = Curso.objects.all()
   contexto = {
       'cursos': cursos
   }
   return render(request, 'exibir_curso.html', contexto)
