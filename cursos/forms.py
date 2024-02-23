from typing import Any
from django import forms
from cursos.models import Curso
from datetime import date

class CursoForm(forms.ModelForm):
    def clean_data(self): # Validação da data, não ter cadastro no passado
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.validation_error('Data inválida')
        return data
    class Meta:
        model = Curso
        fields = '__all__' #  Todos os campos do model