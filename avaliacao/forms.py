from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['nota', 'comentario', 'livro']
        labels = {
            'nota': 'Nota',
            'comentario': 'Comentário',
            'livro': 'Livro',
        }
        widgets = {
            'nota': forms.TextInput(attrs={'class': 'form-control', 'min': 0, 'max': 25}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'},),
            'livro': forms.Select(attrs={'class': 'form-select'}),
        }