from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Edicao

class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['titulo', 'editora', 'data_publicacao', 'numero_paginas', 'livro']