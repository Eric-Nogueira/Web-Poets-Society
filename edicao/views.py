from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import EdicaoForm
from .models import Edicao

from rolepermissions.checkers import has_permission, has_object_permission

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
    user = request.user
    
    if has_permission(user, 'editar_qualquer_edicao'):
        pass
    
    elif has_permission(user, 'editar_proprio_edicao') and has_object_permission('gerenciar_edicao', user, edicao):
        pass
    
    else:
        messages.error(request, 'Você não tem permissão para editar essa edição.')
        return redirect('livros:lista')

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
    user = request.user
    
    if request.method == 'POST':
        if has_permission(user, 'excluir_proprio_edicao') or (has_permission(user, 'excluir_propria_edicao') and has_object_permission('gerenciar_edicao', user, edicao)):
            edicao.delete()
        else:
            messages.error(request, 'Você não tem permissão para deletar essa edição.')
        
        return redirect('home')

    return render(
        request,
        'form/deletar_edicao.html',
        {
            'edicao': edicao
        }
    )