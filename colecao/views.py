from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ColecaoForm


@login_required
def criar_colecao(request):
    """Mostra o formulario de cadastro de Colecao e salva quando enviado."""
    if request.method == 'POST':
        form = ColecaoForm(request.POST)
        if form.is_valid():
            colecao = form.save()
            messages.success(request, f'Colecao "{colecao.titulo}" criada com sucesso!')
            return redirect('colecao:criar')
    else:
        form = ColecaoForm()

    return render(request, 'form/colecao_form.html', {'form': form})
