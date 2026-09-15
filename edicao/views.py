from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import EdicaoForm


@login_required
def register_edicao(request):
    if request.method == 'POST':
        # O formulario tem upload de PDF, entao precisa receber request.FILES.
        form = EdicaoForm(request.POST, request.FILES)
        if form.is_valid():
            edicao = form.save()
            messages.success(request, f'Edicao "{edicao.titulo}" cadastrada com sucesso!')
            return redirect('home')
    else:
        form = EdicaoForm()
    return render(request, 'form/register_edicao.html', {'form': form})
