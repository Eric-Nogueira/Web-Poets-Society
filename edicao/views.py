from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import EdicaoForm
from .models import Edicao

def register_edicao(request):
    if request.method == 'POST':
        form = EdicaoForm(request.POST)
        if form.is_valid():
            edicao = form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = EdicaoForm()
    return render(request, 'form/register_edicao.html', {'form': form})