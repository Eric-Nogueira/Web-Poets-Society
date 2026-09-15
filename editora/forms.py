from django import forms

from .models import Editora


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['endereco', 'ano_fundacao', 'resposavel']
        labels = {
            'endereco': 'Endereco',
            'ano_fundacao': 'Ano de fundacao',
            'resposavel': 'Responsavel',
        }
        widgets = {
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'ano_fundacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'resposavel': forms.Select(attrs={'class': 'form-select'}),
        }
