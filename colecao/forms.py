from django import forms

from .models import Colecao


class ColecaoForm(forms.ModelForm):
    class Meta:
        model = Colecao
        fields = ['titulo', 'colecoes_filhas']
        labels = {
            'titulo': 'Título',
            'colecoes_filhas': 'Coleções filhas',
        }
        help_texts = {
            'colecoes_filhas': (
                'Opcional. Segure Ctrl (ou Cmd no Mac) para selecionar mais '
                'de uma coleção que ficará "dentro" desta.'
            ),
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Poesia Contemporânea',
                'maxlength': 100,
            }),
            'colecoes_filhas': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 5}),
        }
