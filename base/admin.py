# Registrar em quais tabelas o admin vai ter acesso

from django.contrib import admin
from .models import Cadastro

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin): 
    list_display = ['nome', 'email', 'data']
    search_fields = ['nome', 'email'] #Pesquisa por nome e email
    list_filter = ['data'] #Filtro por data
    list_per_page = 10
