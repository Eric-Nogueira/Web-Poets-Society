from django import forms

from .models import Edicao


class EdicaoForm(forms.ModelForm):
    class Meta:
        model = Edicao
        fields = ['titulo', 'editora', 'data_publicacao', 'numero_paginas', 'livro', 'pdf']
        labels = {
            'titulo': 'Titulo',
            'data_publicacao': 'Data de publicacao',
            'numero_paginas': 'Numero de paginas',
            'pdf': 'Arquivo PDF',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numero_paginas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'livro': forms.Select(attrs={'class': 'form-select'}),
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        }
