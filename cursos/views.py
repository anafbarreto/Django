from django.shortcuts import render
from cursos.forms import CursoForm
from rest_framework import generics
from cursos.serializers import ItemSerializer
from cursos.models import Curso


# Create your views here.
def criar_curso(request):
    form = CursoForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_curso.html', contexto)


def exibir_cursos(request):
   cursos = Curso.objects.all()
   contexto = {
       'cursos': cursos
   }
   return render(request, 'exibir_curso.html', contexto)
