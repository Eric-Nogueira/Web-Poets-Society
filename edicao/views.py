from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import EdicaoForm
from .models import Edicao


@login_required
def register_edicao(request):
    if request.method == 'POST':
        form = EdicaoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            edicao = form.save()

            messages.success(
                request,
                f'Edicao "{edicao.titulo}" cadastrada com sucesso!'
            )

            return redirect('home')
    else:
        form = EdicaoForm()

    return render(
        request,
        'form/register_edicao.html',
        {'form': form}
    )


@login_required
def editar_edicao(request, edicao_id):
    edicao = get_object_or_404(Edicao, id=edicao_id)

    if request.method == 'POST':
        form = EdicaoForm(
            request.POST,
            request.FILES,
            instance=edicao
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EdicaoForm(instance=edicao)

    return render(
        request,
        'form/editar_edicao.html',
        {
            'form': form,
            'edicao': edicao
        }
    )


@login_required
def deletar_edicao(request, edicao_id):
    edicao = get_object_or_404(Edicao, id=edicao_id)

    if request.method == 'POST':
        edicao.delete()
        return redirect('home')

    return render(
        request,
        'form/deletar_edicao.html',
        {
            'edicao': edicao
        }
    )