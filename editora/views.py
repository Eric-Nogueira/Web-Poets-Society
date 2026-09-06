from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

from .forms import EditoraForm
from .models import Editora

def register_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            editora = form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = EditoraForm()
    return render(request, 'form/register_editora.html', {'form': form})