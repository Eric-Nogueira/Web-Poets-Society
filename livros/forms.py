from django import forms

from .models import Livro
from usuario.models import Usuario
from colecao.models import Colecao

# Gêneros comuns para o site. Como o campo "genero" do model é só um texto
# (CharField), essa lista é apenas para o menu suspenso do formulário — o
# banco continua guardando o valor como texto.
GENEROS = [
    ('', 'Selecione'),
    ('Poesia', 'Poesia'),
    ('Conto', 'Conto'),
    ('Crônica', 'Crônica'),
    ('Romance', 'Romance'),
    ('Ficção', 'Ficção'),
    ('Ensaio', 'Ensaio'),
    ('Drama', 'Drama'),
    ('Outro', 'Outro'),
]


class LivroForm(forms.ModelForm):
    # Estes dois campos abaixo NÃO existem no model Livro. Eles servem para
    # o usuário escolher, na hora de criar o livro, quais autores e qual
    # coleção já existentes se relacionam com ele. A view (em views.py) é
    # quem pega essas escolhas e cria os registros de Livro_Usuario e
    # Livro_Colecao depois de salvar o livro.
    autores = forms.ModelMultipleChoiceField(
        queryset=Usuario.objects.all().order_by('username'),
        required=False,
        label='Autor(es)',
        help_text='Opcional. Segure Ctrl (ou Cmd no Mac) para selecionar mais de um autor.',
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'size': 4}),
    )
    colecao = forms.ModelChoiceField(
        queryset=Colecao.objects.all().order_by('titulo'),
        required=False,
        label='Coleção',
        help_text='Opcional. Associa o livro a uma coleção já existente.',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Livro
        fields = ['titulo', 'genero']
        labels = {
            'titulo': 'Título',
            'genero': 'Gênero',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Folhas de Outono',
                'maxlength': 100,
            }),
            'genero': forms.Select(choices=GENEROS, attrs={'class': 'form-select'}),
        }
