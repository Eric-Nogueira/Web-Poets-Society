from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import ColecaoForm
from .models import Colecao

from rolepermissions.checkers import has_permission, has_object_permission


@login_required
def criar_colecao(request):
    if request.method == 'POST':
        form = ColecaoForm(request.POST)

        if form.is_valid():
            colecao = form.save()

            messages.success(
                request,
                f'Coleção "{colecao.titulo}" criada com sucesso!'
            )

            return redirect('colecao:criar')
    else:
        form = ColecaoForm()

    return render(
        request,
        'form/colecao_form.html',
        {'form': form}
    )


@login_required
def lista_colecoes(request):
    colecoes = Colecao.objects.order_by('titulo')

    return render(
        request,
        'view/colecoes.html',
        {'colecoes': colecoes}
    )


@login_required
def editar_colecao(request, colecao_id):
    colecao = get_object_or_404(
        Colecao,
        id=colecao_id
    )
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'editar_qualquer_colecao'):
            pass
        elif has_permission(user, 'editar_proprio_colecao') and has_object_permission('gerenciar_colecao', user, colecao):
            pass
        else:
            messages.error(request, 'Você não tem permissão para editar essa coleção.')
            return redirect('livros:lista')
        
        form = ColecaoForm(
            request.POST,
            instance=colecao
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f'Coleção "{colecao.titulo}" atualizada com sucesso!'
            )

            return redirect('colecao:lista')
    else:
        form = ColecaoForm(
            instance=colecao
        )

    return render(
        request,
        'form/editar_colecao.html',
        {
            'form': form,
            'colecao': colecao
        }
    )


@login_required
def deletar_colecao(request, colecao_id):
    colecao = get_object_or_404(
        Colecao,
        id=colecao_id
    )
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'excluir_qualquer_colecao'):
            pass
        elif has_permission(user, 'excluir_proprio_colecao') and has_object_permission('gerenciar_colecao', user, colecao):
            pass
        else:
            messages.error(request, 'Você não tem permissão para deletar essa coleção.')
            return redirect('livros:lista')
        colecao.delete()

        messages.success(
            request,
            'Coleção deletada com sucesso!'
        )

        return redirect('colecao:lista')

    return render(
        request,
        'form/deletar_colecao.html',
        {
            'colecao': colecao
        }
    )