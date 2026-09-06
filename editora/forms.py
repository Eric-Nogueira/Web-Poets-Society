from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Editora

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['endereco', 'ano_fundacao', 'resposavel']