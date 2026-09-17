from django import forms

from .models import Capitulo
from livros.models import Livro


class CapituloForm(forms.ModelForm):
    # Sobrescrevemos o campo "livro" só para trocar o texto da primeira
    # opção do menu (o Django usa "---------" por padrão).
    livro = forms.ModelChoiceField(
        queryset=Livro.objects.all().order_by('titulo'),
        empty_label='Selecione o livro',
        label='Livro',
        help_text='Escolha o livro ao qual este capítulo pertence.',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Capitulo
        fields = ['livro', 'titulo', 'num_de_pag', 'comentario']
        labels = {
            'titulo': 'Título',
            'num_de_pag': 'Número de páginas',
            'comentario': 'Comentário',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: O primeiro verso', 'maxlength': 200,}),

            'num_de_pag': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: 12','min': 1,}),

            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Observações sobre este capítulo...',}),
        }
