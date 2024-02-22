# Banco de dados no Django
# Default: SQLite3

from django.db import models


class Cadastro(models.Model):
    nome = models.CharField(max_length=50) #Tamanho maximo de 50 caracteres para nome (charfield = string)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=15)
    data = models.DateTimeField(auto_now_add=True) # Pega automaticamente a data e hora que o cadastro foi feito
    
    def __str__(self): #Metodo para mostrar detalhes do cadastro dentro do admin
        return f'{self.nome}, {self.email}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Formulário de contato' # Nome do formulario
        verbose_name_plural = 'Formulários de contato'
        ordering = ['-data'] # Como deve ser ordenado no banco - o hifen é para descrente 

""" Toda vez que mexer no banco, precisa fazer o comando:
terminal: python manage.py makemigrations
terminal: python manage.py migrate
Para criar essas informações na tabela"""
