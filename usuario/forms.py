from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'Data_Nascimento'
        )


class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'Data_Nascimento',
            'is_active',
        )

        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'Data_Nascimento': 'Data de nascimento',
            'is_active': 'Usuário ativo',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'Data_Nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'is_active': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }