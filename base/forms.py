from django import forms
from base.models import Cadastro

"""
Na primeira versão do formulario, preenchi os dados um por um aqui nesse arquivo forms.py
Com a evolução do desenvolvimento, esses campos estavam se repetindo em varios outros arquivos
Com o objeto de otimizar o codigo e usar as possibilidades do Django, optei por usar o forms.ModelForm
Então o codigo inicial 
   class CadastroForm(forms.Form):
    nome = forms.CharField() #Campo nome do tipo texto (charfield)
    email = forms.EmailField() #Campo email com as validações de @ 
    senha= forms.CharField(widget=forms.PasswordInput) #Campo senha do tipo texto com a informação ocultada da senha

Vai assumir os dados definidos no models.py (banco de dados)
"""

# Dados do formulario que já estão no models(banco de dados)
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__' # Todos os campos, mas pode ser preenchido um por um tbm
        


