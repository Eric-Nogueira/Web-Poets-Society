from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .forms import EditoraForm
from .models import Editora

from rolepermissions.checkers import has_object_permission, has_permission


@login_required
def register_editora(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)

        if form.is_valid():
            editora = form.save()
            messages.success(
                request,
                f'Editora "{editora}" cadastrada com sucesso!'
            )
            return redirect('home')
    else:
        form = EditoraForm()

    return render(
        request,
        'form/register_editora.html',
        {'form': form}
    )


@login_required
def editar_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'editar_qualquer_editora'):
            pass
        elif has_permission(user, 'editar_proprio_editora') and has_object_permission('gerenciar_editora', user, editora):
            pass
        else:
            messages.error(request, 'Você não tem permissão para editar este perfil.')
            return redirect('home')
        form = EditoraForm(
            request.POST,
            instance=editora
        )

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditoraForm(instance=editora)

    return render(
        request,
        'form/editar_editora.html',
        {
            'form': form,
            'editora': editora
        }
    )


@login_required
def deletar_editora(request, editora_id):
    editora = get_object_or_404(Editora, id=editora_id)
    user = request.user

    if request.method == 'POST':
        if has_permission(user, 'excluir_qualquer_editora'):
            pass
        elif has_permission(user, 'excluir_proprio_editora') and has_object_permission('gerenciar_editora', user, editora):
            pass
        else:
            messages.error(request, 'Você não tem permissão para excluir este perfil.')
            return redirect('home')
        editora.delete()
        return redirect('home')

    return render(
        request,
        'form/deletar_editora.html',
        {
            'editora': editora
        }
    )