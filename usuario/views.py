from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from editora.models import Editora

from .forms import UsuarioForm
from .models import Usuario

@login_required
def home(request):
    context = {

        'editoras_recentes': Editora.objects.order_by(
            '-id'
        ),

        'usuarios_recentes': Usuario.objects.order_by(
            '-date_joined'
        ),

    }

    return render(
        request,
        'index.html',
        context
    )

def register(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        form = UsuarioForm()
    return render(request, 'form/register.html', {'form': form})

# Create your views here.
