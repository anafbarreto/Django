from django import forms

#Classe + nome para o formulário
class CadastroForm(forms.Form):
    nome = forms.CharField() #Campo nome do tipo texto (charfield)
    email = forms.EmailField() #Campo email com as validações de @ 
    senha= forms.CharField(widget=forms.PasswordInput) #Campo senha do tipo texto com a informação ocultada da senha
    