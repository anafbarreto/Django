"""
A pasta projeto_womakers contém a estrutura de URLs do projeto
Pra manter mais organizado, o ideal é cada pasta tenha um arquivo urls.py com suas
rotas e subrotas.
Depois preencher o URL geral com o caminho pra essa pasta aqui.
"""

from django.urls import path
from cursos.views import criar_curso
from cursos.views import exibir_cursos

app_name = 'cursos'
urlpatterns = [
    path('criar_curso/', criar_curso, name='criar_curso'),
    path('cursos_disponiveis/', exibir_cursos, name='Cursos disponiveis'),
]